# -*- coding: utf-8 -*-
import io, os

base = io.open("index.html", "r", encoding="utf-8").read()

ROXO = """
:root{--rosa-bebe:#2C1836;--rosa-claro:#F4C9DC;--rosa-forte:#FF8FBB;--roxo:#D9B8F0;--roxo-escuro:#311a3d;--texto-claro:#E9DAE6;--texto-titulo:#FBEFF6;--branco:#1A0C21;}
body{background:#211029!important;color:#E9DAE6!important}
.bg-blush{background:linear-gradient(180deg,#2C1836,#211029)!important}
.bg-white{background:#1A0C21!important;color:#E9DAE6!important}
.bg-roxo{background:#341d40!important;color:#F0E2EE!important}
.sec-title{color:#FBEFF6!important}.sec-sub{color:#CBB7CB!important}
.hero h1{color:#FBEFF6!important}.hero h1 em{color:#FF8FBB!important}
.hero p,.scroll-hint{color:#CBB7CB!important}
.eyebrow,.bg-roxo .eyebrow{color:#FF9EC4!important}
.btn{background:#FF8FBB!important;color:#3a121f!important;box-shadow:0 12px 28px rgba(255,143,187,.32)!important}
.reason{background:rgba(255,255,255,.05)!important;border-color:rgba(255,143,190,.20)!important}
.reason h3{color:#FFB3D1!important}.reason p{color:#D8C6D8!important}
.qual li,.deliver li{background:rgba(255,255,255,.05)!important;border-color:rgba(255,143,190,.16)!important;color:#E4D4E4!important}
.qual-card{background:rgba(255,143,190,.12)!important;border-color:rgba(255,143,190,.4)!important;color:#FBEFF6!important}
.wpp{background:rgba(255,255,255,.06)!important}.wpp::after{border-right-color:rgba(255,255,255,.06)!important}
.wpp .name{color:#FF9EC4!important}.wpp p{color:#E4D4E4!important}.wpp .meta{color:#B49BB8!important}
.step .num{background:#FF8FBB!important;color:#3a121f!important}.step p{color:#D8C6D8!important}
.stat-num{color:#FBEFF6!important}.stat-lbl{color:#CBB7CB!important}.stat-ic{color:#FF9EC4!important}
.price-card .price-cta,.price-card .big{color:#FBEFF6!important}.price-card .cash{color:#D9C7DA!important}.price-card .parcela{color:#FF9EC4!important}
.badges{color:#CBB7CB!important}
.oferta-sep .price-card{background:#311a3d!important;border-color:#FF8FBB!important;box-shadow:0 18px 50px rgba(33,16,41,.55)!important}
details{background:rgba(255,255,255,.045)!important;border-color:rgba(255,255,255,.08)!important}
summary{color:#F3E7F0!important}summary::after{color:#FF9EC4!important}details .ans{color:#C6B2C6!important}
.brandmark{color:#FF9EC4!important}.btn-whats{background:#341d40!important}
"""

VERDE = """
:root{--rosa-bebe:#1C3528;--rosa-claro:#CFE8D8;--rosa-forte:#EBC571;--roxo:#CFE8D8;--roxo-escuro:#1E3A2C;--texto-claro:#ECE6D6;--texto-titulo:#FAF7EC;--branco:#112019;}
body{background:#15281F!important;color:#ECE6D6!important}
.bg-blush{background:linear-gradient(180deg,#1C3528,#15281F)!important}
.bg-white{background:#112019!important;color:#ECE6D6!important}
.bg-roxo{background:#1E3A2C!important;color:#EAF3EA!important}
.sec-title{color:#FAF7EC!important}.sec-sub{color:#BFCDBF!important}
.hero h1{color:#FAF7EC!important}.hero h1 em{color:#EBC571!important}
.hero p,.scroll-hint{color:#C2D0C2!important}
.eyebrow,.bg-roxo .eyebrow{color:#EBC571!important}
.btn{background:#F47A5A!important;color:#3a1d12!important;box-shadow:0 12px 28px rgba(244,122,90,.35)!important}
.reason{background:rgba(255,255,255,.05)!important;border-color:rgba(235,197,113,.22)!important}
.reason h3{color:#EBC571!important}.reason p{color:#D7D0C2!important}
.qual li,.deliver li{background:rgba(255,255,255,.05)!important;border-color:rgba(235,197,113,.18)!important;color:#E4DCCB!important}
.qual-card{background:rgba(235,197,113,.12)!important;border-color:rgba(235,197,113,.4)!important;color:#FAF7EC!important}
.wpp{background:rgba(255,255,255,.06)!important}.wpp::after{border-right-color:rgba(255,255,255,.06)!important}
.wpp .name{color:#EBC571!important}.wpp p{color:#E4DCCB!important}.wpp .meta{color:#9DB3A2!important}
.step .num{background:#EBC571!important;color:#3a1d12!important}.step p{color:#D7D0C2!important}
.stat-num{color:#FAF7EC!important}.stat-lbl{color:#C2D0C2!important}.stat-ic{color:#EBC571!important}
.price-card .price-cta,.price-card .big{color:#FAF7EC!important}.price-card .cash{color:#C9DCCB!important}.price-card .parcela{color:#EBC571!important}
.badges{color:#C2D0C2!important}
.oferta-sep .price-card{background:#1E3A2C!important;border-color:#EBC571!important;box-shadow:0 18px 50px rgba(20,40,30,.5)!important}
details{background:rgba(255,255,255,.045)!important;border-color:rgba(255,255,255,.08)!important}
summary{color:#F2EEDF!important}summary::after{color:#EBC571!important}details .ans{color:#C2BCAE!important}
.brandmark{color:#EBC571!important}.btn-whats{background:#1E3A2C!important}
"""

AZUL = """
:root{--rosa-bebe:#1B2746;--rosa-claro:#F4C9DC;--rosa-forte:#FF8FB6;--roxo:#CBD6F2;--roxo-escuro:#1E2A4A;--texto-claro:#E5E2EC;--texto-titulo:#FBF6FB;--branco:#121A30;}
body{background:#161E36!important;color:#E5E2EC!important}
.bg-blush{background:linear-gradient(180deg,#1B2746,#161E36)!important}
.bg-white{background:#121A30!important;color:#E5E2EC!important}
.bg-roxo{background:#1E2A4A!important;color:#E9EAF4!important}
.sec-title{color:#FBF6FB!important}.sec-sub{color:#BCC2D6!important}
.hero h1{color:#FBF6FB!important}.hero h1 em{color:#FF8FB6!important}
.hero p,.scroll-hint{color:#BEC4D8!important}
.eyebrow,.bg-roxo .eyebrow{color:#FF92BE!important}
.btn{background:#F76FA3!important;color:#3a121f!important;box-shadow:0 12px 28px rgba(247,111,163,.35)!important}
.reason{background:rgba(255,255,255,.05)!important;border-color:rgba(255,143,182,.20)!important}
.reason h3{color:#FF9EC4!important}.reason p{color:#CDD2E2!important}
.qual li,.deliver li{background:rgba(255,255,255,.05)!important;border-color:rgba(255,143,182,.16)!important;color:#DCDFEC!important}
.qual-card{background:rgba(255,143,182,.12)!important;border-color:rgba(255,143,182,.4)!important;color:#FBF6FB!important}
.wpp{background:rgba(255,255,255,.06)!important}.wpp::after{border-right-color:rgba(255,255,255,.06)!important}
.wpp .name{color:#FF9EC4!important}.wpp p{color:#DCDFEC!important}.wpp .meta{color:#9AA4C0!important}
.step .num{background:#FF8FB6!important;color:#3a121f!important}.step p{color:#CDD2E2!important}
.stat-num{color:#FBF6FB!important}.stat-lbl{color:#BEC4D8!important}.stat-ic{color:#FF92BE!important}
.price-card .price-cta,.price-card .big{color:#FBF6FB!important}.price-card .cash{color:#C7CFE6!important}.price-card .parcela{color:#FF9EC4!important}
.badges{color:#BEC4D8!important}
.oferta-sep .price-card{background:#1E2A4A!important;border-color:#FF8FB6!important;box-shadow:0 18px 50px rgba(10,16,34,.55)!important}
details{background:rgba(255,255,255,.045)!important;border-color:rgba(255,255,255,.08)!important}
summary{color:#EFEAF2!important}summary::after{color:#FF92BE!important}details .ans{color:#BCC0D2!important}
.brandmark{color:#FF92BE!important}.btn-whats{background:#1E2A4A!important}
"""

variants = {"roxo": ROXO, "verde": VERDE, "azul": AZUL}

os.makedirs("previews", exist_ok=True)
for name, css in variants.items():
    inject = '\n<style id="palette-preview">' + css + '</style>\n</head>'
    out = base.replace("</head>", inject, 1)
    io.open(os.path.join("previews", name + ".html"), "w", encoding="utf-8").write(out)
    print("gerado previews/%s.html (%d KB)" % (name, len(out)//1024))

print("ok")
