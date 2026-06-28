# -*- coding: utf-8 -*-
import io, re, base64
from PIL import Image

doc = io.open("index.html", "r", encoding="utf-8").read()
bak = io.open("_index_preadjust.bak", "r", encoding="utf-8").read()

URI = re.compile(r'data:image/[a-z]+;base64,[^"]+')

# ---- foto original do HERO (amamentação) vinda do backup pré-erro ----
bh = bak[bak.find("<!-- DOBRA 1 : HEADLINE -->"):bak.find("<!-- SITUAÇÕES -->")]
HERO_URI = URI.search(bh).group(0)
print("hero original recuperado:", len(HERO_URI)//1024, "KB")

# ---- foto verde da Day (regenerada) ----
im = Image.open("D:/CLAUDE/fotos-day/DAY_9400.JPG").convert("RGB")
w,h=im.size; side=min(w,h); left=(w-side)//2; top=int((h-side)*0.38)
im=im.crop((left,top,left+side,top+side)).resize((680,680),Image.LANCZOS)
buf=io.BytesIO(); im.save(buf,"JPEG",quality=82)
DAY_URI="data:image/jpeg;base64,"+base64.b64encode(buf.getvalue()).decode()

# ---- 1) corrige HERO (estava com a foto da Day) ----
h_reg = doc[doc.find("<!-- DOBRA 1 : HEADLINE -->"):doc.find("<!-- SITUAÇÕES -->")]
old_hero = URI.search(h_reg).group(0)
doc = doc.replace(old_hero, HERO_URI, 1)
print("hero corrigido (era %dKB)"%(len(old_hero)//1024))

# ---- 2) coloca Day verde na AUTORIDADE ----
a_reg = doc[doc.find("<!-- DOBRA 11 : AUTORIDADE -->"):doc.find("<!-- O QUE VOCÊ VAI APRENDER -->")]
old_au = URI.search(a_reg).group(0)
doc = doc.replace(old_au, DAY_URI, 1)
print("autoridade agora com Day verde (era %dKB)"%(len(old_au)//1024))

# ---- 3) move as 3 fotinhas do BÔNUS para "O que você vai aprender" ----
cs = doc.find('<div class="compose-photos reveal">'); ce = doc.find("</div>", cs)+len("</div>")
compose = doc[cs:ce]
img1 = re.search(r'<img[^>]+>', compose).group(0)
doc = doc.replace("\n    "+compose, "", 1)   # remove do bonus (com a indentacao que inserimos)
APH = '<h2 class="sec-title reveal">O que você vai aprender no Guia da Pega</h2>'
doc = doc.replace(APH, APH+"\n    "+compose, 1)
print("compose movido para aprender")

# ---- 4) imagem pequena de amamentação no BÔNUS (placeholder limpo, sem watermark) ----
SUB = '<p class="sec-sub reveal">Materiais extras para te apoiar em cada fase da amamentação.</p>'
doc = doc.replace(SUB, SUB+'\n    <div class="bonus-foto reveal">'+img1+'</div>', 1)

# ---- 5) destacar a palavra "bônus" (eyebrow vira badge) ----
doc = doc.replace('<span class="eyebrow reveal">Bônus exclusivos</span>',
                  '<span class="eyebrow bonus-eyebrow reveal">Bônus exclusivos</span>', 1)

# ---- 6) hero scroll-hint com destaque + pulse; tag verde no topo da linha; mobile padronizado ----
EXTRA = '''
/* scroll-hint em destaque, pulsando */
.scroll-hint{display:inline-block;color:#FFD0E2!important;background:rgba(255,143,182,.14);border:1px solid rgba(255,143,182,.4);padding:9px 18px;border-radius:999px;box-shadow:0 6px 20px rgba(255,143,182,.20);opacity:1;animation:hintpulse 1.7s ease-in-out infinite}
@keyframes hintpulse{0%,100%{transform:translateY(0);box-shadow:0 6px 18px rgba(255,143,182,.18)}50%{transform:translateY(3px);box-shadow:0 12px 28px rgba(255,143,182,.34)}}
@media(prefers-reduced-motion:reduce){.scroll-hint{animation:none}}
/* badge BÔNUS em destaque */
.bonus-eyebrow{font-size:.92rem!important;letter-spacing:.18em;color:#06331b!important;background:#21C161;padding:7px 16px;border-radius:999px;box-shadow:0 8px 22px rgba(33,193,97,.3)}
/* foto amamentacao no bonus */
.bonus-foto{display:flex;justify-content:center;margin:24px 0 4px}
.bonus-foto img{width:210px;height:150px;object-fit:cover;border-radius:18px;border:2px solid rgba(255,143,182,.4);box-shadow:0 12px 30px rgba(10,16,34,.35)}
/* tag INCLUSO: toda verde, em cima da linha do box; cards padronizados */
.bonus-card{padding-top:30px;min-height:104px}
.bonus-tag{position:absolute;top:-12px;left:50%;transform:translateX(-50%);right:auto;margin:0;background:#21C161!important;color:#06331b!important;box-shadow:0 4px 12px rgba(10,16,34,.4)}
.bonus-grid .bonus-card:nth-child(1) .bonus-tag,.bonus-grid .bonus-card:nth-child(2) .bonus-tag,.bonus-grid .bonus-card:nth-child(3) .bonus-tag,.bonus-grid .bonus-card:nth-child(4) .bonus-tag{background:#21C161;color:#06331b}
@media(max-width:679px){.bonus-grid{grid-template-columns:1fr}.bonus-card{min-height:0}}
'''
i = doc.rfind("</style>")
doc = doc[:i] + EXTRA + doc[i:]

io.open("index.html","w",encoding="utf-8").write(doc)
print("tamanho final: %d KB"%(len(doc)//1024))
print("compose em aprender:", doc.find(compose) < doc.find('Bônus exclusivos'))
print("bonus-foto:", "bonus-foto" in doc)
print("hintpulse:", "hintpulse" in doc)
