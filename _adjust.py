# -*- coding: utf-8 -*-
import io, base64
from PIL import Image

doc = io.open("index.html", "r", encoding="utf-8").read()
bak = io.open("_index_prerebuild.bak", "r", encoding="utf-8").read()

# ---------- 1) nova foto da Day (DAY_9400, fundo verde) ----------
im = Image.open("D:/CLAUDE/fotos-day/DAY_9400.JPG").convert("RGB")
w, h = im.size
side = min(w, h)
left = (w - side) // 2
top = int((h - side) * 0.38)  # sobe um pouco pra centralizar o rosto
im = im.crop((left, top, left + side, top + side)).resize((680, 680), Image.LANCZOS)
buf = io.BytesIO(); im.save(buf, "JPEG", quality=82)
newb64 = base64.b64encode(buf.getvalue()).decode()

a = doc.find("auth-grid")
s = doc.find("data:image/jpeg;base64,", a) + len("data:image/jpeg;base64,")
e = doc.find('"', s)
doc = doc[:s] + newb64 + doc[e:]
print("foto Day trocada (novo b64 %d KB)" % (len(newb64)//1024))

# ---------- 2) compose-photos (3 fotos amamentacao) do backup ----------
cs = bak.find('<div class="compose-photos reveal">')
ce = bak.find("</div>", cs) + len("</div>")
compose = bak[cs:ce]
print("compose-photos extraido:", len(compose)//1024, "KB")

# insere no bonus, depois do subtitulo
SUB = '<p class="sec-sub reveal">Materiais extras para te apoiar em cada fase da amamentação.</p>'
assert SUB in doc, "subtitulo bonus nao encontrado"
doc = doc.replace(SUB, SUB + "\n    " + compose)

# ---------- 3) bonus: tag para fora do .bonus-tt (vira filho direto do card) ----------
doc = doc.replace('<div class="bonus-card reveal"><span class="bonus-ic">',
                  '<div class="bonus-card reveal"><span class="bonus-tag">Incluso</span><span class="bonus-ic">')
doc = doc.replace('<div class="bonus-tt"><span class="bonus-tag">Incluso</span>',
                  '<div class="bonus-tt">')

# ---------- 4) FAQ: mover acompanhamento WhatsApp para o final ----------
ACOMP = '      <details class="reveal"><summary>Esse curso tem acompanhamento no WhatsApp?</summary><div class="ans">Não. Ele é a versão Pocket do curso Técnica Dos Anjos: aqui você aprende especificamente essa técnica para já aplicar agora. Se quiser, depois você pode adquirir o acompanhamento à parte.</div></details>'
COMO = '      <details class="reveal"><summary>Como acesso meu produto?</summary><div class="ans">O curso fica em uma plataforma do Manual do Recém-Nascido. Você recebe o acesso por e-mail e WhatsApp 🙂</div></details>'
assert ACOMP in doc and COMO in doc, "FAQ alvo nao encontrado"
doc = doc.replace(ACOMP + "\n", "")          # remove do topo
doc = doc.replace(COMO, COMO + "\n" + ACOMP) # recoloca por ultimo

# ---------- 5) CSS extra (antes do </style> do tema-final) ----------
EXTRA = '''
/* situacoes: topicos a esquerda */
.voice{text-align:left}
/* checklist: check centralizado e maior */
.deliver li{align-items:center}
.deliver .check{flex:0 0 30px;width:30px;height:30px;font-size:1rem}
/* bonus: tag no canto superior direito + cores alternadas */
.bonus-card{position:relative;padding-top:36px}
.bonus-tag{position:absolute;top:12px;right:14px;margin:0}
.compose-photos{display:flex;justify-content:center;margin:26px 0 6px}
.bonus-grid .bonus-card:nth-child(1) .bonus-tag{background:#21C161;color:#0f1830}
.bonus-grid .bonus-card:nth-child(2) .bonus-tag{background:#FF8FB6;color:#3a121f}
.bonus-grid .bonus-card:nth-child(3) .bonus-tag{background:#EBC571;color:#3a2a08}
.bonus-grid .bonus-card:nth-child(4) .bonus-tag{background:#5DC5E0;color:#0a2630}
.bonus-grid .bonus-card:nth-child(1) .bonus-ic{background:rgba(33,193,97,.16);color:#4FE08C}
.bonus-grid .bonus-card:nth-child(2) .bonus-ic{background:rgba(255,143,182,.16);color:#FF9EC4}
.bonus-grid .bonus-card:nth-child(3) .bonus-ic{background:rgba(235,197,113,.16);color:#EBC571}
.bonus-grid .bonus-card:nth-child(4) .bonus-ic{background:rgba(93,197,224,.16);color:#7FD3E8}
.bonus-grid .bonus-card:nth-child(1){border-color:rgba(33,193,97,.32)}
.bonus-grid .bonus-card:nth-child(2){border-color:rgba(255,143,182,.32)}
.bonus-grid .bonus-card:nth-child(3){border-color:rgba(235,197,113,.32)}
.bonus-grid .bonus-card:nth-child(4){border-color:rgba(93,197,224,.32)}
'''
i = doc.rfind("</style>")
doc = doc[:i] + EXTRA + doc[i:]

io.open("index.html", "w", encoding="utf-8").write(doc)
print("tamanho final: %d KB" % (len(doc)//1024))
print("compose no bonus:", doc.count("compose-photos"))
print("bonus-tag fora do tt:", '<div class="bonus-card reveal"><span class="bonus-tag">' in doc)
print("acompanhamento por ultimo:", doc.rfind("acompanhamento no WhatsApp") > doc.rfind("Como acesso meu produto"))
