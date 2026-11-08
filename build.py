"""Gera as páginas estáticas do site (pt-BR em /, English em /en/), o sitemap e o robots.

Uso: python build.py
Só usa a biblioteca padrão. O resultado fica na raiz do repositório, pronto para o GitHub Pages.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://otavioprocopio.github.io/great-cotw-one-site"
DOWNLOAD = "https://github.com/OtavioProcopio/great-cotw-one-site/releases/latest"

# Preencha antes de abrir a loja (aparecem na Privacidade e nos Termos).
CONTROLLER = "Otávio Procópio"
CONTACT_EMAIL = ""  # ex.: "suporte@seudominio.com.br"
LICENSE_HOST = ""  # ex.: "Hetzner Online (Alemanha)"

LEGAL_PATHS = {
    "pt": {"privacy": "privacidade/", "terms": "termos/"},
    "en": {"privacy": "en/privacy/", "terms": "en/terms/"},
}

T = {
    "pt": {
        "lang": "pt-BR",
        "path": "/",
        "title": "Great COTW One – mapa de animais, editor de save e equipamentos para theHunter: Call of the Wild",
        "desc": "Veja onde cada grupo de animais passa e a que horas, edite seus animais, monte o equipamento certo para cada caça e acompanhe o perfil inteiro do theHunter: Call of the Wild. Em português, English e Español.",
        "keywords": "theHunter Call of the Wild, COTW, mapa de animais, editor de save, great one, diamante, rota dos animais, equipamento, melhor arma por animal, rastreador de grupos",
        "og_locale": "pt_BR",
        "nav": [("#recursos", "Recursos"), ("#equipamentos", "Equipamentos"), ("#seguro", "Seguro"), ("#premium", "Premium"), ("#faq", "Perguntas")],
        "cta": "Baixar para Windows",
        "cta2": "Ver como funciona",
        "badge": "Projeto de fã · Windows 10 e 11 · 100% single-player",
        "h1": "Pare de caçar no escuro.",
        "lead": "O <strong>Great COTW One</strong> lê o seu save do <em>theHunter: Call of the Wild</em> e mostra <strong>onde cada grupo de animais passa, a que horas</strong>, qual arma e munição servem para cada bicho e tudo o que você já conquistou. Sem planilha, sem código, em português.",
        "hero_alt": "Mapa de zonas do Great COTW One com a rota de um grupo de animais",
        "trust": ["Backup antes de toda gravação", "Nunca grava com o jogo aberto", "Nenhum arquivo do jogo no app", "Funciona sem internet"],
        "feat_h": "Tudo o que o jogo não te mostra",
        "feat_sub": "O app lê o seu save e a sua instalação do jogo e transforma tudo em telas simples.",
        "features": [
            ("mapa", "Mapa de zonas e rastreador de grupos", "Veja onde os animais comem, bebem e descansam, no mapa do próprio jogo. Escolha um grupo e o app desenha a rota do dia, com o horário de cada parada e onde ele deve estar agora.", "Mapa de zonas com a rota de um grupo"),
            ("animais", "Wiki dos animais", "Todas as reservas e espécies, com onde cada animal vive, quantos você tem no save (machos, fêmeas, Great Ones, maior peso e pontuação) e os seus melhores abates.", "Wiki dos animais com a ficha de cada espécie"),
            ("perfil", "Perfil e conquistas", "Nível, abates, precisão de tiro, tiro mais longe, troféus e as conquistas da Steam, com filtro e busca.", "Perfil do caçador com conquistas"),
            ("missoes", "Missões por reserva", "Quanto falta em cada reserva, o que está em andamento e a lista de missões com o texto do próprio jogo.", "Missões por reserva"),
        ],
        "eq_h": "Equipamento certo para cada caça",
        "eq_sub": "A página de Equipamentos mostra tudo o que o seu perfil guarda e responde a pergunta de todo caçador: <em>o que eu levo para esse animal?</em>",
        "eq_points": [
            ("Arsenal completo", "Armas, munição, miras, iscas e equipamentos de campo com ícone do seu jogo, o que você tem, o que falta e o nível que libera cada item."),
            ("Ficha e ranking das armas", "Tiros, acertos, precisão, abates, abates de um tiro, recorde e tiro mais longe de cada arma. Ordene por abates, precisão ou recorde."),
            ("Montador por animal", "Escolha a reserva e o animal. O app usa a classe de caça do animal e as classes que cada munição recomenda no próprio jogo e sugere o melhor do seu arsenal, mais o que vale comprar."),
            ("Conjuntos salvos", "Veja os seus loadouts, qual está ativo e quais itens faltam em cada um."),
        ],
        "eq_shots": [("equipamentos-advisor", "O que levar para o alce: arma, munição e mira"), ("equipamentos-kit", "Kit para a reserva inteira com iscas, extras e peso total")],
        "eq_note": "As telas usam dados de exemplo. No app você vê o seu arsenal e os ícones do seu jogo.",
        "safe_h": "Seguro por design",
        "safe_sub": "Mexer em save dá medo. Por isso cada regra abaixo é testada e vale para tudo o que o app grava.",
        "safe": [
            ("Backup automático", "Uma cópia completa antes de qualquer gravação. Os backups nunca são apagados e você volta ao momento anterior com um clique."),
            ("Jogo fechado", "O app confere se o jogo está aberto e se recusa a gravar enquanto estiver."),
            ("Mostra antes, confere depois", "Toda mudança é exibida para você confirmar e relida em seguida para verificar byte a byte."),
            ("Só single-player", "Nada de multiplayer e nada de automação do jogo."),
            ("Sem arquivos do jogo", "Nenhum arquivo, imagem ou dado do jogo vai no instalador: o app lê a sua instalação na hora."),
        ],
        "prem_h": "Grátis para ver. Premium para mudar.",
        "prem_sub": "Tudo o que lê o seu jogo é de graça. O Premium é o que grava nele.",
        "free": "Grátis",
        "premium": "Premium",
        "rows": [
            ("Mapa com rota e horário de cada grupo", True, True),
            ("Ver as zonas que ainda faltam", True, True),
            ("Wiki dos animais, perfil, conquistas e missões", True, True),
            ("Arsenal, ranking das armas e Montador por animal", True, True),
            ("Backups e voltar a qualquer momento", True, True),
            ("Liberar as zonas no jogo (por reserva, animal ou necessidade)", False, True),
            ("Editar peso, pontuação, sexo e Great One dos animais", False, True),
            ("Entregar itens, liberar na loja, ajustar munição e dinheiro", False, True),
        ],
        "price_m": "R$ 15",
        "per_m": "por mês",
        "price_y": "R$ 75",
        "per_y": "por ano · 58% mais barato",
        "prem_note": "A licença é uma chave que você cola no app. Ele a confere sem internet e a ativação não envia nenhum dado seu. Ao vencer, o app volta ao modo gratuito sem apagar nada. A loja do Premium ainda vai abrir.",
        "faq_h": "Perguntas frequentes",
        "faq": [
            ("O Great COTW One é seguro para o meu save?", "Sim. O app guarda uma cópia completa antes de qualquer gravação, nunca grava com o jogo aberto, mostra o que vai mudar antes de aplicar e relê o arquivo depois para conferir. Você pode voltar ao momento anterior com um clique."),
            ("Dá ban ou afeta o multiplayer?", "O app é só para single-player e não automatiza o jogo. Não use as edições em saves ligados a modos online."),
            ("Preciso de internet?", "Não. O app lê o seu save e o jogo instalado direto do computador. A licença Premium também é conferida sem internet."),
            ("Funciona com quais versões do jogo?", "Com o theHunter: Call of the Wild instalado pela Steam, no Windows 10 ou 11, e pelo menos uma partida salva. Os mapas de Askiy Ridge e Intisuyu ainda estão por confirmar."),
            ("O Windows avisou que o programa não é seguro. E agora?", "O instalador ainda não tem assinatura digital paga, então o SmartScreen desconfia de qualquer programa novo. Clique em Mais informações e depois em Executar assim mesmo."),
            ("Quais idiomas?", "Português, English e Español, escolhidos em Ajustes. Nomes de animais, missões e conquistas acompanham o idioma."),
            ("O que é grátis e o que é Premium?", "Tudo o que lê o seu jogo é grátis: mapa, animais, perfil, missões, equipamentos e backups. O Premium é o que grava: liberar zonas, editar animais e entregar itens."),
        ],
        "final_h": "Pronto para caçar com informação?",
        "final_p": "Baixe, abra e deixe o app achar o seu save sozinho. A instalação é só para o seu usuário e não pede senha de administrador.",
        "foot_disc": "Great COTW One é um projeto de fã, sem ligação com a Expansive Worlds nem com a Avalanche Studios. theHunter: Call of the Wild é marca dos seus donos. As imagens do app usam dados de exemplo.",
        "other_lang": ("en/", "English"),
        "other_hreflang": "en",
        "schema_desc": "Mapa de zonas, rastreador de grupos de animais, editor de save e montador de equipamento para theHunter: Call of the Wild.",
    },
    "en": {
        "lang": "en",
        "path": "/en/",
        "title": "Great COTW One – animal map, save editor and loadout builder for theHunter: Call of the Wild",
        "desc": "See where every animal group goes and when, edit your animals, build the right loadout for each hunt and track your whole theHunter: Call of the Wild profile. In English, Português and Español.",
        "keywords": "theHunter Call of the Wild, COTW, animal map, save editor, great one, diamond, animal routes, loadout, best weapon per animal, animal group tracker",
        "og_locale": "en_US",
        "nav": [("#features", "Features"), ("#gear", "Equipment"), ("#safe", "Safe"), ("#premium", "Premium"), ("#faq", "FAQ")],
        "cta": "Download for Windows",
        "cta2": "See how it works",
        "badge": "Fan project · Windows 10 and 11 · 100% single-player",
        "h1": "Stop hunting in the dark.",
        "lead": "<strong>Great COTW One</strong> reads your <em>theHunter: Call of the Wild</em> save and shows <strong>where each animal group goes and when</strong>, which weapon and ammo fit each animal, and everything you have achieved. No spreadsheets, no code.",
        "hero_alt": "Great COTW One zone map showing the route of an animal group",
        "trust": ["Backup before every write", "Never writes with the game open", "No game files inside the app", "Works offline"],
        "feat_h": "Everything the game does not show you",
        "feat_sub": "The app reads your save and your game install and turns it all into simple screens.",
        "features": [
            ("mapa", "Zone map and group tracker", "See where animals eat, drink and rest, on the game's own map. Pick a group and the app draws the day's route with the time of every stop and where it should be right now.", "Zone map with a group route"),
            ("animais", "Animal wiki", "Every reserve and species, where each animal lives, how many you have in your save (males, females, Great Ones, top weight and score) and your best harvests.", "Animal wiki with a species sheet"),
            ("perfil", "Profile and achievements", "Level, kills, accuracy, longest shot, trophies and Steam achievements, with filter and search.", "Hunter profile with achievements"),
            ("missoes", "Missions per reserve", "How much is left in each reserve, what is in progress and the mission list with the game's own text.", "Missions per reserve"),
        ],
        "eq_h": "The right gear for every hunt",
        "eq_sub": "The Equipment page shows everything your profile holds and answers every hunter's question: <em>what do I bring for this animal?</em>",
        "eq_points": [
            ("Full arsenal", "Weapons, ammo, sights, lures and field gear with icons from your own game, what you own, what is missing and the level that unlocks each item."),
            ("Weapon sheet and ranking", "Shots, hits, accuracy, kills, one-shot kills, record and longest shot for each weapon. Sort by kills, accuracy or record."),
            ("Loadout builder per animal", "Pick the reserve and the animal. The app uses the animal's hunting class and the classes each ammo recommends in the game itself, and suggests the best from your arsenal plus what is worth buying."),
            ("Saved loadouts", "See your loadouts, which one is active and what items are missing in each."),
        ],
        "eq_shots": [("equipamentos-advisor", "What to bring for the moose: weapon, ammo and scope"), ("equipamentos-kit", "Whole-reserve kit with lures, extras and total weight")],
        "eq_note": "Screens use sample data. In the app you see your own arsenal and your game's icons.",
        "safe_h": "Safe by design",
        "safe_sub": "Touching a save is scary. So every rule below is tested and applies to everything the app writes.",
        "safe": [
            ("Automatic backup", "A full copy before any write. Backups are never deleted and you can go back to the previous moment with one click."),
            ("Game closed", "The app checks whether the game is running and refuses to write while it is."),
            ("Preview, then verify", "Every change is shown for you to confirm and then re-read to verify, byte by byte."),
            ("Single-player only", "No multiplayer and no game automation."),
            ("No game files", "No game file, image or data ships in the installer: the app reads your install on the spot."),
        ],
        "prem_h": "Free to look. Premium to change.",
        "prem_sub": "Everything that reads your game is free. Premium is what writes to it.",
        "free": "Free",
        "premium": "Premium",
        "rows": [
            ("Map with route and time of every group", True, True),
            ("See the zones you have not found yet", True, True),
            ("Animal wiki, profile, achievements and missions", True, True),
            ("Arsenal, weapon ranking and per-animal builder", True, True),
            ("Backups and go back at any time", True, True),
            ("Unlock zones in the game (per reserve, animal or need)", False, True),
            ("Edit weight, score, sex and Great One of your animals", False, True),
            ("Give items, unlock in the store, adjust ammo and cash", False, True),
        ],
        "price_m": "R$ 15",
        "per_m": "per month",
        "price_y": "R$ 75",
        "per_y": "per year · 58% cheaper",
        "prem_note": "The license is a key you paste in the app. It checks it offline and activation sends none of your data. When it expires the app returns to free mode without deleting anything. The Premium store has not opened yet.",
        "faq_h": "Frequently asked questions",
        "faq": [
            ("Is Great COTW One safe for my save?", "Yes. The app keeps a full copy before any write, never writes with the game open, shows what will change before applying it and re-reads the file afterwards to check. You can go back with one click."),
            ("Can it get me banned or affect multiplayer?", "The app is single-player only and does not automate the game. Do not use the edits on saves tied to online modes."),
            ("Do I need internet?", "No. The app reads your save and installed game straight from your computer. The Premium license is also checked offline."),
            ("Which game versions work?", "theHunter: Call of the Wild installed through Steam, on Windows 10 or 11, with at least one saved game. The Askiy Ridge and Intisuyu maps are still to be confirmed."),
            ("Windows warned that the program is not safe. Now what?", "The installer does not have a paid digital signature yet, so SmartScreen distrusts any new program. Click More info and then Run anyway."),
            ("Which languages?", "English, Português and Español, chosen in Settings. Animal, mission and achievement names follow the language."),
            ("What is free and what is Premium?", "Everything that reads your game is free: map, animals, profile, missions, equipment and backups. Premium is what writes: unlocking zones, editing animals and giving items."),
        ],
        "final_h": "Ready to hunt with information?",
        "final_p": "Download, open and let the app find your save on its own. Installation is per-user and needs no administrator password.",
        "foot_disc": "Great COTW One is a fan project, not affiliated with Expansive Worlds or Avalanche Studios. theHunter: Call of the Wild is a trademark of its owners. App images use sample data.",
        "other_lang": ("../", "Português"),
        "other_hreflang": "pt-BR",
        "schema_desc": "Zone map, animal group tracker, save editor and loadout builder for theHunter: Call of the Wild.",
    },
}

CSS_LINK = '<link rel="stylesheet" href="{base}assets/style.css">'

CHECK = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DASH = '<span class="no" aria-label="no">—</span>'


def e(s: str) -> str:
    return html.escape(s, quote=True)


def img(base: str, name: str, alt: str, eager: bool = False, w: int = 1920, h: int = 1200) -> str:
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="{base}assets/img/{name}.png" alt="{e(alt)}" width="{w}" height="{h}" {load}>'


def page(code: str) -> str:
    t = T[code]
    base = "" if code == "pt" else "../"
    prefix = "" if code == "pt" else "en/"  # prints no idioma da página
    url = SITE + t["path"]
    other_url = SITE + ("/en/" if code == "pt" else "/")
    ids = [n[0][1:] for n in t["nav"]]
    jsonld = [
        {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": "Great COTW One",
            "applicationCategory": "GameApplication",
            "operatingSystem": "Windows 10, Windows 11",
            "description": t["schema_desc"],
            "url": url,
            "downloadUrl": DOWNLOAD,
            "inLanguage": ["pt-BR", "en", "es"],
            "image": SITE + "/assets/og.png",
            "offers": [
                {"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "BRL"},
                {"@type": "Offer", "name": "Premium monthly", "price": "15", "priceCurrency": "BRL"},
                {"@type": "Offer", "name": "Premium yearly", "price": "75", "priceCurrency": "BRL"},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]
            ],
        },
    ]
    nav = "".join(f'<a href="{h}">{e(n)}</a>' for h, n in t["nav"]) + guide_links(code, "" if code == "pt" else "../")
    ol, oname = t["other_lang"]
    feats = ""
    for i, (shot, title, text, alt) in enumerate(t["features"]):
        flip = " flip" if i % 2 else ""
        feats += f'<article class="feat{flip}"><div class="feat-text"><h3>{e(title)}</h3><p>{e(text)}</p></div><figure class="shot">{img(base, prefix + shot, alt)}</figure></article>'
    points = "".join(f"<li><h3>{e(a)}</h3><p>{e(b)}</p></li>" for a, b in t["eq_points"])
    shots = "".join(f'<figure class="shot">{img(base, prefix + s, a)}</figure>' for s, a in t["eq_shots"])
    safe = "".join(f"<li>{CHECK}<div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>" for a, b in t["safe"])
    rows = "".join(
        f'<tr><th scope="row">{e(n)}</th><td>{CHECK if f else DASH}</td><td>{CHECK if p else DASH}</td></tr>' for n, f, p in t["rows"]
    )
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    trust = "".join(f"<li>{CHECK}{e(x)}</li>" for x in t["trust"])
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<meta name="keywords" content="{e(t['keywords'])}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0b0f0c">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{t['lang']}" href="{url}">
<link rel="alternate" hreflang="{t['other_hreflang']}" href="{other_url}">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="icon" type="image/png" sizes="32x32" href="{base}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{base}assets/icon-128.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Great COTW One">
<meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(t['title'])}">
<meta name="twitter:description" content="{e(t['desc'])}">
<meta name="twitter:image" content="{SITE}/assets/og.png">
{CSS_LINK.format(base=base)}
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top">
  <a class="brand" href="{base or './'}"><img src="{base}assets/icon-128.png" alt="" width="32" height="32"><span>Great COTW One</span></a>
  <nav aria-label="menu">{nav}</nav>
  <a class="lang" href="{ol}" hreflang="{t['other_hreflang']}">{oname}</a>
</header>
<main>
<section class="hero">
  <p class="badge">{e(t['badge'])}</p>
  <h1>{e(t['h1'])}</h1>
  <p class="lead">{t['lead']}</p>
  <div class="cta-row">
    <a class="btn primary" href="{DOWNLOAD}" rel="noopener">{e(t['cta'])}</a>
    <a class="btn ghost" href="#{ids[0]}">{e(t['cta2'])}</a>
  </div>
  <ul class="trust">{trust}</ul>
  <figure class="hero-shot">{img(base, prefix + 'mapa', t['hero_alt'], eager=True)}</figure>
</section>

<section id="{ids[0]}" class="block">
  <h2>{e(t['feat_h'])}</h2>
  <p class="sub">{e(t['feat_sub'])}</p>
  {feats}
</section>

<section id="{ids[1]}" class="block alt">
  <h2>{e(t['eq_h'])}</h2>
  <p class="sub">{t['eq_sub']}</p>
  <ul class="points">{points}</ul>
  <div class="shots">{shots}</div>
  <p class="note">{e(t['eq_note'])}</p>
</section>

<section id="{ids[2]}" class="block">
  <h2>{e(t['safe_h'])}</h2>
  <p class="sub">{e(t['safe_sub'])}</p>
  <ul class="safe">{safe}</ul>
</section>

<section id="{ids[3]}" class="block alt">
  <h2>{e(t['prem_h'])}</h2>
  <p class="sub">{e(t['prem_sub'])}</p>
  <div class="table-wrap"><table>
    <thead><tr><th></th><th scope="col">{e(t['free'])}</th><th scope="col" class="pro">{e(t['premium'])}</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
  <div class="prices">
    <div class="price"><strong>{t['price_m']}</strong><span>{e(t['per_m'])}</span></div>
    <div class="price best"><strong>{t['price_y']}</strong><span>{e(t['per_y'])}</span></div>
  </div>
  <p class="note">{e(t['prem_note'])}</p>
</section>

<section id="{ids[4]}" class="block">
  <h2>{e(t['faq_h'])}</h2>
  <div class="faq">{faq}</div>
</section>

<section class="final">
  <h2>{e(t['final_h'])}</h2>
  <p>{e(t['final_p'])}</p>
  <a class="btn primary big" href="{DOWNLOAD}" rel="noopener">{e(t['cta'])}</a>
</section>
</main>
<footer>
  <p class="links">{guide_links(code, "" if code == "pt" else "../", " · ")} · {legal_links(code, "" if code == "pt" else "../")}</p>
  <p class="disc">{e(t['foot_disc'])}</p>
</footer>
</body>
</html>
"""


def guide_links(code: str, root: str, sep: str = "") -> str:
    """Links para o guia de animais e de reservas."""
    items = {"pt": [("animais/", "Animais"), ("reservas/", "Reservas")], "en": [("en/animals/", "Animals"), ("en/reserves/", "Reserves")]}[code]
    return sep.join(f'<a href="{root}{p}">{n}</a>' for p, n in items)


def legal_links(code: str, root: str) -> str:
    """Links do rodapé para Privacidade e Termos; `root` é o caminho até a raiz do site."""
    paths = LEGAL_PATHS[code]
    names = {"pt": ("Privacidade", "Termos de uso"), "en": ("Privacy", "Terms of use")}[code]
    return f'<a href="{root}{paths["privacy"]}">{names[0]}</a> · <a href="{root}{paths["terms"]}">{names[1]}</a>'


def fill(text: str, code: str) -> str:
    """Troca os campos {controller}, {contact} e {host} pelos valores do topo do arquivo."""
    contact = CONTACT_EMAIL or ("o e-mail de suporte publicado neste site" if code == "pt" else "the support e-mail published on this site")
    host = LICENSE_HOST or ("a hospedagem do servidor, informada aqui quando a loja abrir" if code == "pt" else "the server host, listed here when the store opens")
    return text.format(controller=CONTROLLER, contact=contact, host=host)


def legal_page(code: str, kind: str) -> str:
    """Página de Privacidade ou Termos, no mesmo visual do site."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("legal", ROOT / "legal.py")
    assert spec and spec.loader
    legal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(legal)

    sections = (legal.PRIVACY if kind == "privacy" else legal.TERMS)[code]
    title = {
        ("pt", "privacy"): "Política de Privacidade",
        ("pt", "terms"): "Termos de Uso",
        ("en", "privacy"): "Privacy Policy",
        ("en", "terms"): "Terms of Use",
    }[(code, kind)]
    path = LEGAL_PATHS[code][kind]
    base = "../" * path.count("/")
    other_code = "en" if code == "pt" else "pt"
    other_path = LEGAL_PATHS[other_code][kind]
    updated = legal.UPDATED if code == "pt" else legal.UPDATED_EN
    body = ""
    for heading, parts in sections:
        body += f"<h2>{e(heading)}</h2>"
        for part in parts:
            if isinstance(part, list):
                body += "<ul>" + "".join(f"<li>{e(fill(x, code))}</li>" for x in part) + "</ul>"
            else:
                body += f"<p>{e(fill(part, code))}</p>"
    home = base + ("" if code == "pt" else "en/")
    back = "Voltar ao início" if code == "pt" else "Back to home"
    stamp = ("Última atualização: " if code == "pt" else "Last updated: ") + updated
    lang = "pt-BR" if code == "pt" else "en"
    other_lang = "en" if code == "pt" else "pt-BR"
    other_name = "English" if code == "pt" else "Português"
    desc = f"{title} do Great COTW One." if code == "pt" else f"Great COTW One {title}."
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} – Great COTW One</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#0b0f0c">
<link rel="canonical" href="{SITE}/{path}">
<link rel="alternate" hreflang="{lang}" href="{SITE}/{path}">
<link rel="alternate" hreflang="{other_lang}" href="{SITE}/{other_path}">
<link rel="icon" type="image/png" sizes="32x32" href="{base}assets/favicon-32.png">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<header class="top">
  <a class="brand" href="{home}"><img src="{base}assets/icon-128.png" alt="" width="32" height="32"><span>Great COTW One</span></a>
  <a class="lang" href="{base}{other_path}" hreflang="{other_lang}">{other_name}</a>
</header>
<main class="legal">
  <h1>{e(title)}</h1>
  {body}
  <p class="note">{e(stamp)}</p>
  <p><a href="{home}">{back}</a></p>
</main>
<footer><p class="links">{legal_links(code, base)}</p></footer>
</body>
</html>
"""


def main() -> None:
    (ROOT / "index.html").write_text(page("pt"), encoding="utf-8", newline="\n")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page("en"), encoding="utf-8", newline="\n")
    for code, kinds in LEGAL_PATHS.items():
        for kind, path in kinds.items():
            (ROOT / path).mkdir(parents=True, exist_ok=True)
            (ROOT / path / "index.html").write_text(legal_page(code, kind), encoding="utf-8", newline="\n")
    import importlib.util

    spec = importlib.util.spec_from_file_location("content", ROOT / "content.py")
    assert spec and spec.loader
    content = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(content)
    guide_paths = content.build(SITE, DOWNLOAD, legal_links)
    urls = [SITE + "/", SITE + "/en/"]
    sm = "".join(
        f'  <url><loc>{u}</loc><xhtml:link rel="alternate" hreflang="pt-BR" href="{SITE}/"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}/en/"/></url>\n'
        for u in urls
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + sm
        + "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for p in guide_paths)
        + "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for kinds in LEGAL_PATHS.values() for p in kinds.values())
        + "</urlset>\n",
        encoding="utf-8",
        newline="\n",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8", newline="\n")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    main()
