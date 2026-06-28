# -*- coding: utf-8 -*-
import io, base64
from PIL import Image

doc = io.open("index.html", "r", encoding="utf-8").read()

# ---- processa imagem do Drive: corta marca d'agua (canto inf esq) ----
im = Image.open("_bonus_src.img").convert("RGB")
w, h = im.size  # 1143x800
im = im.crop((255, 0, w, h))            # remove faixa esquerda (onde fica "LIKLUC")
im.thumbnail((760, 760), Image.LANCZOS)
buf = io.BytesIO(); im.save(buf, "JPEG", quality=83)
bonus_uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
print("imagem bonus pronta (sem watermark): %dx%d, %dKB" % (im.size[0], im.size[1], len(bonus_uri)//1024))

# ---- troca SOMENTE o src do bonus-foto (nao mexe nas 3 fotos do 'aprender') ----
bf = doc.find('class="bonus-foto')
s = doc.find('src="', bf) + 5
e = doc.find('"', s)
doc = doc[:s] + bonus_uri + doc[e:]
print("bonus-foto trocada pela imagem do Drive")

# ---- CSS: blob na foto da Day, tamanhos no mobile, acabamento do bonus ----
EXTRA = '''
/* foto Day com acabamento blob (igual topo) */
.day-img{border-radius:var(--blob)}
/* bonus-foto com acabamento do topo, maior, sem filtro/borda */
.bonus-foto img{width:100%!important;max-width:330px!important;height:auto!important;aspect-ratio:4/3!important;object-fit:cover!important;border-radius:var(--blob)!important;box-shadow:var(--sombra-forte)!important;border:none!important;filter:none!important}
/* mobile: topo e Day menores */
@media(max-width:779px){
  .hero-photo{max-width:290px;margin:0 auto}
  .day-img{max-width:230px}
  .bonus-foto img{max-width:260px!important}
}
'''
i = doc.rfind("</style>")
doc = doc[:i] + EXTRA + doc[i:]

io.open("index.html", "w", encoding="utf-8").write(doc)
print("tamanho final: %d KB" % (len(doc)//1024))
print("day-img blob:", ".day-img{border-radius:var(--blob)}" in doc)
print("bonus uri aplicada 1x:", doc.count(bonus_uri))
