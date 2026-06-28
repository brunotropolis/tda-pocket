# -*- coding: utf-8 -*-
import io

base = io.open("index.html", "r", encoding="utf-8").read()

M_HERO  = "<!-- DOBRA 1 : HEADLINE -->"
M_PROVA = "<!-- DOBRA 2 : PROVA SOCIAL -->"
M_AUTOR = "<!-- DOBRA 11 : AUTORIDADE -->"
M_OFERTA= "<!-- DOBRA 11b : OFERTA -->"

PRE  = base[:base.find(M_HERO)]
POST = base[base.find("<footer>"):]
hero = base[base.find(M_HERO):base.find(M_PROVA)]
autor= base[base.find(M_AUTOR):base.find(M_OFERTA)]

# ---- HERO edits ----
hero = hero.replace(
  '<span class="eyebrow">Técnica Dos Anjos Pocket</span>',
  '<span class="eyebrow">Guia da Pega</span>')
hero = hero.replace(
  '<h1>Amamentar dói? Descubra o que está errado na pega e amamente <em>sem dor</em>.</h1>',
  '<h1>Amamentar dói? Existe um jeito de facilitar a pega para o seu bebê, e a dor pode ir embora <em>já na próxima mamada</em>.</h1>')
hero = hero.replace(
  '<p>Sem fissura, sem bico de silicone e com a certeza de que seu bebê está mamando de verdade.</p>',
  '<p>Sem fissura, sem bico de silicone, com a certeza de que ele está mamando de verdade e ficando satisfeito.</p>')
hero = hero.replace(
  'role pra entender o que está acontecendo ↓',
  'role para entender ↓')

# ---- AUTOR edits ----
autor = autor.replace(
  '<h2 class="sec-title reveal">Dayane Dos Anjos</h2>',
  '<h2 class="sec-title reveal">Dayane Dos Anjos</h2>\n    <p class="sec-sub reveal">Consultora de amamentação, sono e cuidados com o bebê</p>')
autor = autor.replace(
  '<p>Sou mãe, consultora de amamentação, criadora de conteúdo digital sobre cuidados com os bebês, que sou completamente apaixonada.</p>',
  '<p>As primeiras semanas decidem o sucesso da amamentação, mas é justamente quando a mãe fica sozinha, sem uma orientação clara e objetiva. Quando a dor, a insegurança e o cansaço tomam conta, o desmame precoce acaba ganhando espaço em muitas famílias.</p>')
autor = autor.replace(
  '<p>Eu vivi tudo isso que você está vivendo, por isso quero que seja diferente com você. Procuro todos os dias auxiliar milhares de mamães com um conteúdo rico e informativo, para que possam ter uma maternidade mais tranquila e saudável.</p>',
  '<p>Foi por isso que a Day criou um jeito de facilitar a pega para o bebê: para a dor aliviar na hora, e para o bebê passar a mamar de verdade, tirando mais leite, em menos tempo, e ficando satisfeito por intervalos mais longos.</p>')
autor = autor.replace(
  '<p>Através do Técnica Dos Anjos Pocket oriento as mães para terem sucesso na amamentação, para amamentarem sem dor, de forma efetiva, e vejam seus bebês saírem do seio bem alimentados, saciados e relaxados, e assim cresçam fortes e saudáveis com o melhor alimento do mundo: o leite da mamãe.</p>',
  '')

AV = '<span class="avatar"><svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><rect width="48" height="48" rx="24" fill="#D94D8C"/><g fill="#fff"><circle cx="19" cy="18" r="6.5"/><path d="M8 41c0-6.6 4.9-11 11-11s11 4.4 11 11z"/><circle cx="33" cy="25" r="4.5" opacity=".85"/><path d="M26.5 41c0-3.8 2.9-6.5 6.5-6.5s6.5 2.7 6.5 6.5z" opacity=".85"/></g></svg></span>'

SITUACOES = '''<!-- SITUAÇÕES -->
<section class="section bg-roxo">
  <div class="narrow center">
    <h2 class="sec-title reveal">Você está vivendo alguma dessas situações?</h2>
    <div class="voices">
      <p class="voice reveal">A amamentação dói, e toda mamada já começa com aquele aperto só de pensar.</p>
      <p class="voice reveal">Seu bico é pequeno, plano ou invertido, e o bebê escorrega na hora de pegar.</p>
      <p class="voice reveal">Apareceu um calo ou bolha no lábio do bebê.</p>
      <p class="voice reveal">As mamadas são longas e parecem não ter fim.</p>
      <p class="voice reveal">Ele larga o peito e em pouco tempo já quer de novo, parece que nunca sacia.</p>
    </div>
    <div class="qual-card reveal" style="margin-top:30px">Se você se identificou, fica tranquila. Não é culpa sua, nem do seu bebê, e muito menos do seu leite. Seu bebê só precisa de ajuda para pegar o seio de uma maneira que o fará mamar com mais facilidade.</div>
  </div>
</section>

'''

CAMINHO = '''<!-- EXISTE UM CAMINHO -->
<section class="section bg-white">
  <div class="wrap center">
    <span class="eyebrow reveal">Existe um caminho</span>
    <h2 class="sec-title reveal">Tem um jeito de ofertar o peito para o bebê que deixa todos esses problemas para trás</h2>
    <p class="sec-sub reveal">Em poucos minutos você vai aprender a deixar a amamentação confortável para os dois. A partir daí:</p>
    <ul class="deliver" style="text-align:left">
      <li class="reveal"><span class="check">✓</span> O bebê extrai mais leite em menos tempo</li>
      <li class="reveal"><span class="check">✓</span> Os lábios dele ficam relaxados, por isso os calos cicatrizam e não voltam</li>
      <li class="reveal"><span class="check">✓</span> Ele fica saciado por mais tempo e aumenta o intervalo entre as mamadas</li>
      <li class="reveal"><span class="check">✓</span> A dor vai embora, mesmo com o seio machucado, porque o bebê passa a sugar do jeito que não machuca</li>
    </ul>
  </div>
</section>

'''

APRENDER = '''<!-- O QUE VOCÊ VAI APRENDER -->
<section class="section bg-blush">
  <div class="wrap center">
    <span class="eyebrow reveal">O que você leva</span>
    <h2 class="sec-title reveal">O que você vai aprender no Guia da Pega</h2>
    <ul class="deliver" style="text-align:left">
      <li class="reveal"><span class="check">✓</span> Como oferecer o peito de um jeito fácil para o bebê pegar</li>
      <li class="reveal"><span class="check">✓</span> Como fazer ele mamar de forma efetiva, tirando mais leite em menos tempo</li>
      <li class="reveal"><span class="check">✓</span> Como trocar a fissura e a dor pela tranquilidade de amamentar do jeito que você sonhou</li>
      <li class="reveal"><span class="check">✓</span> O que fazer para os calos do bebê pararem de inchar e cicatrizarem em poucos dias</li>
    </ul>
  </div>
</section>

'''

DEPOIMENTOS = '''<!-- DEPOIMENTOS -->
<section class="section bg-white">
  <div class="wrap center">
    <h2 class="sec-title reveal">Você não está sozinha nisso</h2>
    <p class="sec-sub reveal">Confira o que elas estão dizendo:</p>
    <div class="wpp-grid">
      <div class="wpp reveal"><div class="wpp-head">''' + AV + '''<span class="name">Bruna · mãe do Theo (RN)</span></div><p>Me diziam que dor era normal e que eu tinha que aguentar. Aprendi a oferecer o peito de um jeito que o Theo pega com facilidade, e hoje amamento tranquila, sem medo da próxima mamada.</p><span class="meta">09:14<span class="ck">✓✓</span></span></div>
      <div class="wpp reveal"><div class="wpp-head">''' + AV + '''<span class="name">Jéssica · mãe do Bento (1 mês)</span></div><p>Achei que ia depender do bico de silicone para sempre. Depois que aprendi a facilitar a pega, ele passou a mamar direto no peito e larguei o silicone.</p><span class="meta">21:37<span class="ck">✓✓</span></span></div>
      <div class="wpp reveal"><div class="wpp-head">''' + AV + '''<span class="name">Mariana · mãe da Aurora (5 semanas)</span></div><p>A Aurora mamava o tempo todo e mesmo assim não ganhava peso. Quando aprendi a facilitar a pega, ela passou a tirar muito mais leite em cada mamada e voltou a engordar com o meu leite.</p><span class="meta">14:02<span class="ck">✓✓</span></span></div>
      <div class="wpp reveal"><div class="wpp-head">''' + AV + '''<span class="name">Pati · mãe do Davi (3 semanas)</span></div><p>Meus seios estavam em carne viva, com fissura. Poucos dias depois de mudar a forma de oferecer o peito, a dor passou e cicatrizou. Agora o Davi mama sem me machucar.</p><span class="meta">07:48<span class="ck">✓✓</span></span></div>
    </div>
  </div>
</section>

'''

BONUS = '''<!-- BÔNUS -->
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
</section>

'''

PRECO = '''<!-- PREÇO -->
<section class="section bg-roxo" id="investimento">
  <div class="narrow center">
    <h2 class="sec-title reveal">Hoje o Guia da Pega sai por apenas:</h2>
    <div class="price-card reveal">
      <div class="price-cta">Corrija a amamentação com uma condição super especial</div>
      <div class="big">R$ 67</div>
      <div class="cash">à vista no Pix</div>
      <div class="parcela">ou 12x de R$ 6,89</div>
      <a href="#" class="btn full">Quero amamentar sem dor</a>
      <div class="badges"><span>✓ Acesso imediato</span><span>✓ Garantia de 7 dias</span><span>✓ Compra 100% segura</span></div>
    </div>
    <div class="howbox reveal">
      <h3 class="how-title">Como funciona</h3>
      <div class="how-steps">
        <div class="how-step"><span class="how-n">1</span><p>Você faz a compra com acesso imediato</p></div>
        <div class="how-step"><span class="how-n">2</span><p>O acesso chega no seu e-mail na hora</p></div>
        <div class="how-step"><span class="how-n">3</span><p>Você assiste e já aplica na próxima mamada</p></div>
      </div>
    </div>
  </div>
</section>

'''

SINCERA = '''<!-- POSSO SER SINCERA -->
<section class="section bg-blush">
  <div class="narrow letter">
    <p class="lead reveal">Posso ser sincera com você?</p>
    <p class="reveal">Você provavelmente já foi numa consultora ou enfermeira, já comprou um ebook, já assistiu vídeo no YouTube. Muita gente tentou te ajudar, e mesmo assim você continua amamentando com dor, no sufoco, sem saber se o bebê mamou direito.</p>
    <p class="reveal">O problema não é você não ter tentado. É que ninguém te mostrou, de um jeito simples, como resolver a amamentação do seu bebê de uma vez por todas.</p>
    <p class="reveal">Aqui é o contrário: em poucos minutos você vê exatamente o que fazer, e já aplica na próxima mamada. São só 30 minutos, direto ao ponto, com o passo a passo mostrado com bebê de verdade.</p>
    <div class="center" style="margin-top:30px"><a href="#investimento" class="btn">Quero amamentar sem dor</a></div>
  </div>
</section>

'''

FAQ = '''<!-- FAQ -->
<section class="section bg-white">
  <div class="narrow">
    <h2 class="sec-title center reveal">Perguntas frequentes</h2>
    <div class="faq">
      <details class="reveal"><summary>Esse curso tem acompanhamento no WhatsApp?</summary><div class="ans">Não. Ele é a versão Pocket do curso Técnica Dos Anjos: aqui você aprende especificamente essa técnica para já aplicar agora. Se quiser, depois você pode adquirir o acompanhamento à parte.</div></details>
      <details class="reveal"><summary>Consigo aplicar mesmo sendo um curso online e não presencial?</summary><div class="ans">Sim, e muitas vezes funciona até melhor. Um profissional presencial te ensina uma vez; mas quem vai colocar em prática nas próximas mamadas é você. O curso te mostra exatamente como fazer isso, você pode rever quantas vezes quiser, paga muito menos e não precisa esperar marcação: resolve agora, na próxima mamada.</div></details>
      <details class="reveal"><summary>Pega correta é a famosa boca de peixinho?</summary><div class="ans">A pega correta não se resume à boca de peixinho. Há muito mais para se atentar por fora e por dentro da boca do bebê, e é exatamente isso que você aprende no Guia da Pega.</div></details>
      <details class="reveal"><summary>Dá mesmo para ajustar a pega já na próxima mamada?</summary><div class="ans">Sim! Você assiste ao conteúdo e já coloca em prática. Como o curso ensina a facilitar a pega para o bebê, você vai ver ele pegar com mais facilidade e mamar melhor. Aplicando o passo a passo com atenção, os resultados vêm rápido, e a cada mamada fica melhor.</div></details>
      <details class="reveal"><summary>Qual é a forma de pagamento?</summary><div class="ans">Cartão, Pix ou boleto. No cartão você pode parcelar em até 12x.</div></details>
      <details class="reveal"><summary>Qual é o prazo de acesso do curso?</summary><div class="ans">Acesso por 12 meses, 100% online. Você pode assistir quantas vezes quiser nesse período.</div></details>
      <details class="reveal"><summary>Como funciona o prazo de garantia?</summary><div class="ans">É o período para você pedir o reembolso integral caso o produto não seja satisfatório. Solicitando pela plataforma Greenn em até 7 dias da compra, o reembolso é processado automaticamente em até 5 dias.</div></details>
      <details class="reveal"><summary>Como acesso meu produto?</summary><div class="ans">O curso fica em uma plataforma do Manual do Recém-Nascido. Você recebe o acesso por e-mail e WhatsApp 🙂</div></details>
    </div>
  </div>
</section>

'''

body = hero + "\n" + SITUACOES + CAMINHO + autor + "\n" + APRENDER + DEPOIMENTOS + BONUS + PRECO + SINCERA + FAQ
doc = PRE + body + POST

doc = doc.replace("Técnica Dos Anjos Pocket", "Guia da Pega")
doc = doc.replace("site%20da%20T%C3%A9cnica%20Dos%20Anjos%20Pocket%20e%20quero",
                  "site%20do%20Guia%20da%20Pega%20e%20quero")

io.open("index.html", "w", encoding="utf-8").write(doc)

# checks
print("tamanho final: %d KB" % (len(doc)//1024))
for needle in ["facilitar a pega para o seu bebê", "Você está vivendo alguma dessas situações",
               "deixa todos esses problemas", "O que você vai aprender no Guia da Pega",
               "Você não está sozinha", "leite empedra (ingurgitamento)",
               "Hoje o Guia da Pega sai", "Posso ser sincera", "versão Pocket do curso Técnica Dos Anjos"]:
    print(("OK " if needle in doc else "FALTA ") + needle)
print("ainda tem 'Técnica Dos Anjos Pocket'? ", "Técnica Dos Anjos Pocket" in doc)
print("ainda tem 'pega rasa'/'Posição errada'? ", ("pega rasa" in doc) or ("Posição errada" in doc))
print("ainda tem 'gestante'? ", "gestante" in doc)
print("ocorrencias 'Guia da Pega':", doc.count("Guia da Pega"))
print("secoes <section:", doc.count("<section"))
