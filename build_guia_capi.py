# -*- coding: utf-8 -*-
"""
Cria/atualiza o workflow n8n "GUIA DA PEGA | Meta CAPI".
Webhook (POST /webhook/guia-capi) recebe eventos do site tdapocket (sendBeacon)
e reenvia pra Meta Conversions API dos 2 pixels do Guia da Pega, com event_id
pra deduplicar com o pixel do navegador. Isolado do GTM/Contabo da agencia.
Token: META_TOKEN_ADS (funciona p/ CAPI; trocar por dedicados depois).
"""
import json, urllib.request

N8N = 'https://n8n-n8n.xktssy.easypanel.host'
env = {}
for ln in open('D:/CLAUDE/.env.meta', encoding='utf-8'):
    ln = ln.strip()
    if '=' in ln and not ln.startswith('#'):
        k, v = ln.split('=', 1); env[k] = v
KEY = env['N8N_API_KEY']
CAPI_TOKEN = env['META_TOKEN_ADS']

def api(method, path, body=None):
    req = urllib.request.Request(N8N + path,
        data=json.dumps(body).encode() if body is not None else None, method=method,
        headers={'X-N8N-API-KEY': KEY, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

CODE = r'''
let raw = $('Webhook').first().json;
let body = raw.body;
if (typeof body === 'string') { try { body = JSON.parse(body); } catch(e) { body = {}; } }
body = body || {};
if (!body.event_name) return [{ json: { skip: true, reason: 'no event_name' } }];

const headers = raw.headers || {};
let ip = '';
const xff = headers['x-forwarded-for'] || headers['X-Forwarded-For'] || '';
if (xff) ip = String(xff).split(',')[0].trim();
if (!ip) ip = headers['x-real-ip'] || headers['cf-connecting-ip'] || '';

const PIXELS = ['1662179248394613', '1339270591500008'];
const TOKEN = '__CAPI_TOKEN__';

const ud = { client_user_agent: body.user_agent || headers['user-agent'] || '' };
if (ip) ud.client_ip_address = ip;
if (body.fbp) ud.fbp = body.fbp;
if (body.fbc) ud.fbc = body.fbc;

const ev = {
  event_name: body.event_name,
  event_time: parseInt(body.event_time) || Math.floor(Date.now()/1000),
  event_id: body.event_id || '',
  action_source: 'website',
  event_source_url: body.event_source_url || '',
  user_data: ud,
};
if (body.custom_data && typeof body.custom_data === 'object' && Object.keys(body.custom_data).length) {
  ev.custom_data = body.custom_data;
}

const out = [];
for (const PIXEL of PIXELS) {
  const url = 'https://graph.facebook.com/v21.0/' + PIXEL + '/events?access_token=' + TOKEN;
  try {
    const resp = await this.helpers.httpRequest({ method: 'POST', url, body: { data: [ev] }, json: true });
    out.push({ json: { ok: true, pixel: PIXEL, event: body.event_name, received: resp.events_received, fbtrace: resp.fbtrace_id } });
  } catch (e) {
    out.push({ json: { ok: false, pixel: PIXEL, event: body.event_name, err: (e.message || String(e)).slice(0, 300) } });
  }
}
return out;
'''.replace('__CAPI_TOKEN__', CAPI_TOKEN)

wf = {
  "name": "GUIA DA PEGA | Meta CAPI",
  "nodes": [
    {
      "parameters": {"httpMethod": "POST", "path": "guia-capi", "responseMode": "onReceived", "options": {}},
      "id": "webhook-guia-capi", "name": "Webhook", "type": "n8n-nodes-base.webhook",
      "typeVersion": 2, "position": [260, 300], "webhookId": "guia-capi"
    },
    {
      "parameters": {"jsCode": CODE},
      "id": "capi-code", "name": "CAPI", "type": "n8n-nodes-base.code",
      "typeVersion": 2, "position": [520, 300]
    }
  ],
  "connections": {"Webhook": {"main": [[{"node": "CAPI", "type": "main", "index": 0}]]}},
  "settings": {"executionOrder": "v1"}
}

existing = None
for w in api('GET', '/api/v1/workflows?limit=250').get('data', []):
    if w['name'] == 'GUIA DA PEGA | Meta CAPI':
        existing = w['id']; break

if existing:
    try: api('POST', f'/api/v1/workflows/{existing}/deactivate')
    except Exception as e: print('deact:', e)
    api('PUT', f'/api/v1/workflows/{existing}', wf)
    wid = existing
    print('atualizado', wid)
else:
    created = api('POST', '/api/v1/workflows', wf)
    wid = created['id']
    print('criado', wid)

api('POST', f'/api/v1/workflows/{wid}/activate')
print('ativo. URL: ' + N8N + '/webhook/guia-capi')
