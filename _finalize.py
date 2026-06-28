# -*- coding: utf-8 -*-
import io

doc = io.open("index.html", "r", encoding="utf-8").read()

# ---------- 1) novo BÔNUS com iconografia ----------
IC1 = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8.4 12.4l2.5 2.5 4.7-5.2"/></svg>'
IC2 = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-6.5-4.2-6.5-9A3.5 3.5 0 0112 8a3.5 3.5 0 016.5 2c0 4.8-6.5 10-6.5 10z"/></svg>'
IC3 = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.5s5.5 6 5.5 10.5a5.5 5.5 0 11-11 0C6.5 9.5 12 3.5 12 3.5z"/><path d="M12 11v5M9.5 13.5h5"/></svg>'
IC4 = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 4.6-3.1 7.7-7 9-3.9-1.3-7-4.4-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>'

OLD_BONUS = '''<!-- BÔNUS -->
<section class="section bg-blush">
  <div class="wrap center">
    <span class="eyebrow reveal">De brinde</span>
    <h2 class="sec-title reveal">Você ainda leva junto:</h2>
    <ul class="deliver" style="text-align:left">
      <li class="reveal"><span class="check">✓</span> Como saber se o bebê está mamando bem de verdade</li>
      <li class="reveal"><span class="check">✓</span> O que fazer com fissura e seios machucados para amamentar sem dor</li>
      <li class="reveal"><span class="check">✓</span> Como aumentar a produção de leite</li>
      <li class="reveal"><span class="check">✓</span> O que fazer quando o leite empedra (ingurgitamento)</li>
    </ul>
  </div>
</section>'''

NEW_BONUS = '''<!-- BÔNUS -->
<section class="section bg-blush">
  <div class="wrap center">
    <span class="eyebrow reveal">Bônus exclusivos</span>
    <h2 class="sec-title reveal">Você ainda leva junto:</h2>
    <p class="sec-sub reveal">Materiais extras para te apoiar em cada fase da amamentação.</p>
    <div class="bonus-grid">
      <div class="bonus-card reveal"><span class="bonus-ic">''' + IC1 + '''</span><div class="bonus-tt"><span class="bonus-tag">Incluso</span>Como saber se o bebê está mamando bem de verdade</div></div>
      <div class="bonus-card reveal"><span class="bonus-ic">''' + IC2 + '''</span><div class="bonus-tt"><span class="bonus-tag">Incluso</span>O que fazer com fissura e seios machucados para amamentar sem dor</div></div>
      <div class="bonus-card reveal"><span class="bonus-ic">''' + IC3 + '''</span><div class="bonus-tt"><span class="bonus-tag">Incluso</span>Como aumentar a produção de leite</div></div>
      <div class="bonus-card reveal"><span class="bonus-ic">''' + IC4 + '''</span><div class="bonus-tt"><span class="bonus-tag">Incluso</span>O que fazer quando o leite empedra (ingurgitamento)</div></div>
    </div>
  </div>
</section>'''

assert OLD_BONUS in doc, "bloco de bonus antigo nao encontrado"
doc = doc.replace(OLD_BONUS, NEW_BONUS)

# ---------- 2) tema azul definitivo + botao verde pulsando + estilo do bonus ----------
TEMA = '''
<style id="tema-final">
:root{--rosa-bebe:#1B2746;--rosa-claro:#F4C9DC;--rosa-forte:#FF8FB6;--roxo:#CBD6F2;--roxo-escuro:#1E2A4A;--texto-claro:#E5E2EC;--texto-titulo:#FBF6FB;--branco:#121A30;}
body{background:#161E36;color:#E5E2EC}
.bg-blush{background:linear-gradient(180deg,#1B2746,#161E36)}
.bg-white{background:#121A30;color:#E5E2EC}
.bg-roxo{background:#1E2A4A;color:#E9EAF4}
.sec-title{color:#FBF6FB}.sec-sub{color:#BCC2D6}
.hero h1{color:#FBF6FB}.hero h1 em{color:#FF8FB6}
.hero p,.scroll-hint{color:#BEC4D8}
.eyebrow,.bg-roxo .eyebrow{color:#FF92BE}
.reason{background:rgba(255,255,255,.05);border-color:rgba(255,143,182,.20)}
.reason h3{color:#FF9EC4}.reason p{color:#CDD2E2}
.qual li,.deliver li{background:rgba(255,255,255,.05);border-color:rgba(255,143,182,.16);color:#DCDFEC}
.qual-card{background:rgba(255,143,182,.12);border-color:rgba(255,143,182,.4);color:#FBF6FB}
.wpp{background:rgba(255,255,255,.06)}.wpp::after{border-right-color:rgba(255,255,255,.06)}
.wpp .name{color:#FF9EC4}.wpp p{color:#DCDFEC}.wpp .meta{color:#9AA4C0}
.stat-num{color:#FBF6FB}.stat-lbl{color:#BEC4D8}.stat-ic{color:#FF92BE}
.price-card{background:rgba(255,255,255,.04)}
.price-card .price-cta,.price-card .big{color:#FBF6FB}.price-card .cash{color:#C7CFE6}.price-card .parcela{color:#FF9EC4}
.badges{color:#BEC4D8}
.how-step p{color:#DCE2F2}.how-title{color:#fff}
details{background:rgba(255,255,255,.045);border-color:rgba(255,255,255,.08)}
summary{color:#EFEAF2}summary::after{color:#FF92BE}details .ans{color:#BCC0D2}
.letter .lead{color:#FF9EC4}.letter p{color:#CDD2E2}
.brandmark{color:#FF92BE}.btn-whats{background:#1E2A4A}
footer{background:#121A30;color:#9AA4C0}

/* botao de compra: verde + pulsando */
.btn{background:#21C161;color:#06331b;box-shadow:0 12px 28px rgba(33,193,97,.40);animation:pulsa 1.8s ease-in-out infinite}
.btn:hover{transform:translateY(-2px) scale(1.03);box-shadow:0 16px 40px rgba(33,193,97,.55)}
@keyframes pulsa{0%,100%{transform:scale(1)}50%{transform:scale(1.045)}}
@media(prefers-reduced-motion:reduce){.btn{animation:none}}

/* bonus com peso + iconografia */
.bonus-grid{display:grid;gap:16px;margin-top:30px;text-align:left}
@media(min-width:680px){.bonus-grid{grid-template-columns:1fr 1fr}}
.bonus-card{display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.055);border:1px solid rgba(255,143,182,.28);border-radius:18px;padding:20px 22px;box-shadow:0 10px 30px rgba(10,16,34,.25)}
.bonus-ic{flex:0 0 auto;width:50px;height:50px;border-radius:14px;display:grid;place-items:center;background:rgba(255,143,182,.14);color:#FF9EC4}
.bonus-ic svg{width:27px;height:27px}
.bonus-tt{font-family:'Fraunces',serif;font-weight:600;font-size:1.06rem;color:#FBF6FB;line-height:1.32}
.bonus-tag{display:inline-block;margin:0 0 6px;font-family:'Quicksand',sans-serif;font-size:.6rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#06331b;background:#21C161;padding:3px 9px;border-radius:6px}
</style>
</head>'''

doc = doc.replace("</head>", TEMA, 1)

io.open("index.html", "w", encoding="utf-8").write(doc)
print("tamanho final: %d KB" % (len(doc)//1024))
print("tema-final inserido:", "tema-final" in doc)
print("bonus-card:", doc.count("bonus-card"))
print("pulsa keyframes:", "@keyframes pulsa" in doc)
print("btn verde:", "#21C161" in doc)
