# -*- coding: utf-8 -*-
import io, re, base64, os
from PIL import Image

d = io.open("index.html", "r", encoding="utf-8").read()
os.makedirs("assets", exist_ok=True)

def to_webp(uri, path, maxw, q=82):
    raw = base64.b64decode(uri.split("base64,", 1)[1])
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(path, "WEBP", quality=q, method=6)
    return im.size, os.path.getsize(path)

def first_img_tag(region_start, region_end, after=0):
    i = d.find("<img", max(region_start, after))
    if i < 0 or (region_end and i > region_end): return None
    return i, d[i:d.find(">", i) + 1]

def alt_of(tag):
    m = re.search(r'alt="([^"]*)"', tag); return m.group(1) if m else ""

def datauri_of(tag):
    return re.search(r'data:image/[a-z]+;base64,[^"]+', tag).group(0)

repl = []  # (old_tag, new_tag)
total_before = 0

# HERO (LCP) - eager + fetchpriority
s = d.find("<!-- DOBRA 1"); e = d.find("<!-- SITUA")
i, tag = first_img_tag(s, e)
uri = datauri_of(tag); total_before += len(uri)
sz, by = to_webp(uri, "assets/hero.webp", 1000, 82)
new = '<img class="hero-img" src="assets/hero.webp" alt="%s" fetchpriority="high" decoding="async">' % alt_of(tag)
repl.append((tag, new)); print("hero.webp %s %dKB" % (sz, by // 1024))

# AUTORIDADE (Day) - lazy
s = d.find("<!-- DOBRA 11"); e = d.find("<!-- O QUE")
i, tag = first_img_tag(s, e)
uri = datauri_of(tag); total_before += len(uri)
sz, by = to_webp(uri, "assets/day.webp", 640, 82)
new = '<img class="day-img" src="assets/day.webp" alt="%s" loading="lazy" decoding="async">' % alt_of(tag)
repl.append((tag, new)); print("day.webp %s %dKB" % (sz, by // 1024))

# APRENDER compose (3) - lazy
s = d.find("<!-- O QUE"); e = d.find("<!-- DEPOIMENTOS")
pos = s
for n in (1, 2, 3):
    i, tag = first_img_tag(s, e, after=pos)
    uri = datauri_of(tag); total_before += len(uri)
    sz, by = to_webp(uri, "assets/leva%d.webp" % n, 260, 82)
    new = '<img src="assets/leva%d.webp" alt="Mãe amamentando o bebê" loading="lazy" decoding="async">' % n
    repl.append((tag, new)); pos = i + len(tag); print("leva%d.webp %s %dKB" % (n, sz, by // 1024))

# BONUS - lazy
s = d.find("<!-- BÔNUS"); e = d.find("<!-- PREÇO")
i, tag = first_img_tag(s, e)
uri = datauri_of(tag); total_before += len(uri)
sz, by = to_webp(uri, "assets/bonus.webp", 720, 82)
new = '<img src="assets/bonus.webp" alt="Mãe amamentando o bebê com tranquilidade" loading="lazy" decoding="async">'
repl.append((tag, new)); print("bonus.webp %s %dKB" % (sz, by // 1024))

for old, new in repl:
    assert old in d, "tag nao encontrada"
    d = d.replace(old, new, 1)

# preload do hero
d = d.replace("</title>", '</title>\n<link rel="preload" as="image" href="assets/hero.webp" fetchpriority="high">', 1)

# ---- ajustes CSS (bonus altura igual, badges com contorno, botao 1 linha) ----
EXTRA = '''
.btn{white-space:nowrap}
@media(max-width:679px){ .bonus-card{min-height:134px} }
@media(max-width:779px){
  .badges{flex-direction:column;align-items:center;gap:10px}
  .badges span{display:block;width:240px;max-width:82%;box-sizing:border-box;text-align:left;border:1px solid rgba(255,143,182,.32);border-radius:10px;padding:9px 16px}
}
@media(max-width:479px){ .btn{padding:16px 22px;font-size:1rem;letter-spacing:0} }
'''
i = d.rfind("</style>")
d = d[:i] + EXTRA + d[i:]

io.open("index.html", "w", encoding="utf-8").write(d)
print("HTML antes ~%dKB de imagens base64 -> agora %d KB total" % (total_before // 1024, len(d) // 1024))
print("imagens externas:", os.listdir("assets"))
