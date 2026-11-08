"""Páginas de conteúdo: guia de animais e de reservas (pt-BR e English).

Lê `data/game.json` (gerado pelo exemplo `site_data` do repositório do app a partir do jogo instalado)
e escreve uma página por espécie, uma por reserva e os índices. Só a biblioteca padrão.
"""

from __future__ import annotations

import html
import importlib.util
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


fur_name = _load("furs").fur_name

DATA_DATE = {"pt": "novembro de 2026", "en": "November 2026"}

L = {
    "pt": {
        "lang": "pt-BR",
        "animals": "animais/",
        "reserves": "reservas/",
        "animals_t": "Animais",
        "reserves_t": "Reservas",
        "home": "Início",
        "other": ("en", "English"),
        "class": "Classe",
        "diamond": "Diamante a partir de",
        "points": "pontos",
        "where": "Onde encontrar",
        "medals": "Pontuação das medalhas (macho)",
        "medal_names": ("Bronze", "Prata", "Ouro", "Diamante", "Máximo"),
        "medal_note": "Pontuação mínima de cada medalha. Diamante é a partir de 90% da faixa de pontos do macho.",
        "no_medal": "Esta espécie não tem medalha por pontuação.",
        "weight": "Peso",
        "male": "Macho",
        "female": "Fêmea",
        "great_one": "Great One",
        "furs": "Pelagens e chances",
        "fur": "Pelagem",
        "rarity": "Raridade",
        "chance": "Chance",
        "rarities": ("Comum", "Incomum", "Rara", "Muito rara"),
        "fur_note": "Chance de cada pelagem num animal novo, pelo peso de sorteio do próprio jogo. Pelagens de Great One e de missão ficam de fora.",
        "go_yes": "Esta espécie tem Great One.",
        "go_furs": "pelagens exclusivas de Great One",
        "cta_h": "Ache esses animais no seu save",
        "cta_p": "O Great COTW One lê o seu save e mostra onde cada grupo passa, a que horas, quais diamantes e pelagens raras estão vivos agora, e qual arma do seu arsenal serve para cada bicho. Grátis para ver.",
        "cta": "Baixar grátis para Windows",
        "source": "Números tirados dos arquivos do próprio jogo ({date}). Projeto de fã, sem ligação com a Expansive Worlds ou a Avalanche Studios.",
        "species": "Espécie",
        "rarest": "Pelagem mais rara",
        "in_reserves": "Reservas",
        "search": "Buscar animal",
        "idx_animals_h": "Todos os animais de theHunter: Call of the Wild",
        "idx_animals_p": "Classe de cada animal, pontuação para diamante, peso, chance de cada pelagem e em quais reservas ele vive. Clique num animal para ver a ficha completa.",
        "idx_animals_title": "Lista de animais de theHunter: Call of the Wild – classe, diamante e pelagens raras",
        "idx_reserves_h": "Reservas de theHunter: Call of the Wild",
        "idx_reserves_p": "Os animais de cada reserva, com a classe e a pontuação para diamante, para você planejar a caçada.",
        "idx_reserves_title": "Reservas de theHunter: Call of the Wild – animais, classes e diamantes",
        "n_species": "espécies",
        "class_word": "classe",
        "sp_title": "{name} em theHunter: Call of the Wild – diamante, peso, pelagens e onde encontrar",
        "sp_desc": "{name} (classe {cls}): {diamond}peso, chance de cada pelagem rara e as reservas onde vive em theHunter: Call of the Wild.",
        "sp_diamond_desc": "diamante a partir de {d} pontos, ",
        "sp_intro": "{name} é um animal de classe {cls} em theHunter: Call of the Wild e vive em {n} {res_word}: {res}.",
        "res_word": ("reserva", "reservas"),
        "q_diamond": "Qual a pontuação de diamante do {name}?",
        "a_diamond": "O {name} macho é diamante a partir de {d} pontos (o máximo é {m}).",
        "q_where": "Onde encontrar {name} em theHunter: Call of the Wild?",
        "a_where": "{name} vive em: {res}.",
        "q_rare": "Qual a pelagem mais rara do {name}?",
        "a_rare": "{fur}, com cerca de {chance} de chance por animal.",
        "rs_title": "{name} – animais, classes e diamantes | theHunter: Call of the Wild",
        "rs_desc": "Os {n} animais de {name} em theHunter: Call of the Wild, com a classe, a pontuação de diamante e a pelagem mais rara de cada um.",
        "rs_intro": "{name} tem {n} espécies de caça. Veja a classe de cada uma, a partir de quantos pontos ela é diamante e qual a pelagem mais rara.",
        "classes_h": "Classes de animais",
        "classes_p": "A classe (1 a 9) diz o tamanho do animal. Cada munição do jogo indica as classes para as quais ela serve: use uma munição da classe certa para abater de forma limpa.",
        "one_in": "1 em {n}",
    },
    "en": {
        "lang": "en",
        "animals": "en/animals/",
        "reserves": "en/reserves/",
        "animals_t": "Animals",
        "reserves_t": "Reserves",
        "home": "Home",
        "other": ("pt", "Português"),
        "class": "Class",
        "diamond": "Diamond from",
        "points": "points",
        "where": "Where to find",
        "medals": "Trophy score by medal (male)",
        "medal_names": ("Bronze", "Silver", "Gold", "Diamond", "Max"),
        "medal_note": "Minimum score for each medal. Diamond starts at 90% of the male score range.",
        "no_medal": "This species has no score-based medal.",
        "weight": "Weight",
        "male": "Male",
        "female": "Female",
        "great_one": "Great One",
        "furs": "Furs and odds",
        "fur": "Fur",
        "rarity": "Rarity",
        "chance": "Chance",
        "rarities": ("Common", "Uncommon", "Rare", "Very rare"),
        "fur_note": "Chance of each fur on a new animal, from the game's own spawn weights. Great One and mission-only furs are left out.",
        "go_yes": "This species has a Great One.",
        "go_furs": "Great One-only furs",
        "cta_h": "Find these animals in your save",
        "cta_p": "Great COTW One reads your save and shows where every herd goes and when, which diamonds and rare furs are alive right now, and which gun in your arsenal fits each animal. Free to view.",
        "cta": "Download free for Windows",
        "source": "Numbers taken from the game's own files ({date}). Fan project, not affiliated with Expansive Worlds or Avalanche Studios.",
        "species": "Species",
        "rarest": "Rarest fur",
        "in_reserves": "Reserves",
        "search": "Search animal",
        "idx_animals_h": "Every animal in theHunter: Call of the Wild",
        "idx_animals_p": "Class, diamond score, weight, fur odds and reserves for every animal. Click an animal for its full page.",
        "idx_animals_title": "theHunter: Call of the Wild animal list – class, diamond score and rare furs",
        "idx_reserves_h": "theHunter: Call of the Wild reserves",
        "idx_reserves_p": "The animals of each reserve, with class and diamond score, to plan your hunt.",
        "idx_reserves_title": "theHunter: Call of the Wild reserves – animals, classes and diamonds",
        "n_species": "species",
        "class_word": "class",
        "sp_title": "{name} in theHunter: Call of the Wild – diamond score, weight, furs and where to find",
        "sp_desc": "{name} (class {cls}): {diamond}weight, rare fur odds and the reserves where it lives in theHunter: Call of the Wild.",
        "sp_diamond_desc": "diamond from {d} points, ",
        "sp_intro": "The {name} is a class {cls} animal in theHunter: Call of the Wild and lives in {n} {res_word}: {res}.",
        "res_word": ("reserve", "reserves"),
        "q_diamond": "What is the diamond score for the {name}?",
        "a_diamond": "A male {name} is a diamond from {d} points (the maximum is {m}).",
        "q_where": "Where to find the {name} in theHunter: Call of the Wild?",
        "a_where": "The {name} lives in: {res}.",
        "q_rare": "What is the rarest {name} fur?",
        "a_rare": "{fur}, at about {chance} per animal.",
        "rs_title": "{name} – animals, classes and diamonds | theHunter: Call of the Wild",
        "rs_desc": "The {n} animals of {name} in theHunter: Call of the Wild, with the class, diamond score and rarest fur of each.",
        "rs_intro": "{name} has {n} huntable species. See each one's class, the score it needs to be a diamond and its rarest fur.",
        "classes_h": "Animal classes",
        "classes_p": "The class (1 to 9) tells the animal's size. Every round in the game lists the classes it suits: use the right class for a clean harvest.",
        "one_in": "1 in {n}",
    },
}


def e(s: object) -> str:
    return html.escape(str(s), quote=True)


def slug(text: str) -> str:
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")


def num(value: float, code: str, digits: int = 2) -> str:
    text = f"{value:,.{digits}f}"
    if digits:
        text = text.rstrip("0").rstrip(".")
    if code == "pt":
        text = text.replace(",", "\u0000").replace(".", ",").replace("\u0000", ".")
    return text


def pct(chance: float, code: str) -> str:
    p = chance * 100
    digits = 0 if p >= 10 else 1 if p >= 1 else 2 if p >= 0.1 else 3
    text = num(p, code, digits) + "%"
    if chance and p < 1:
        text += " (" + L[code]["one_in"].format(n=num(round(1 / chance), code, 0)) + ")"
    return text


# ---------------------------------------------------------------- dados


def load() -> tuple[list[dict], dict[str, dict]]:
    """Reservas e espécies (uma por nome em inglês, juntando os apelidos do jogo)."""
    reserves = json.loads((ROOT / "data" / "game.json").read_text(encoding="utf-8"))
    reserves.sort(key=lambda r: r["name"])
    species: dict[str, dict] = {}
    for r in reserves:
        r["slug"] = slug(r["name"])
        for s in r["species"]:
            key = slug(s["en"])
            s["key"] = key
            entry = species.setdefault(key, {**s, "reserves": []})
            if not entry.get("bands") and s.get("bands"):
                entry.update({k: v for k, v in s.items() if k not in ("reserves",)})
            if r["slug"] not in [x["slug"] for x in entry["reserves"]]:
                entry["reserves"].append({"slug": r["slug"], "name": r["name"]})
    for s in species.values():
        merged: dict[str, dict] = {}
        for f in s.get("furs") or []:
            m = merged.setdefault(f["key"], {"key": f["key"], "chance": 0.0, "rarity": f["rarity"]})
            m["chance"] += f["chance"]
            m["rarity"] = max(m["rarity"], f["rarity"])
        s["furs"] = sorted(merged.values(), key=lambda f: (-f["chance"], f["key"]))
        s["slug_pt"] = slug(s["pt"])
        s["slug_en"] = s["key"]
    return reserves, species


def rarest(s: dict) -> dict | None:
    furs = [f for f in s["furs"] if f["chance"] > 0]
    return min(furs, key=lambda f: f["chance"]) if furs else None


def has_great_one(s: dict) -> bool:
    return bool(s.get("great_one_furs")) or "Male_GreatOne_Scoring" in (s.get("scoring") or {})


def species_url(s: dict, code: str) -> str:
    return L[code]["animals"] + (s["slug_pt"] if code == "pt" else s["slug_en"]) + "/"


def reserve_url(r: dict, code: str) -> str:
    return L[code]["reserves"] + r["slug"] + "/"


# ---------------------------------------------------------------- moldura


def frame(code: str, path: str, other_path: str, title: str, desc: str, body: str, site: str, download: str, legal: str, jsonld: list | None = None) -> str:
    t = L[code]
    base = "../" * path.count("/")
    other_code, other_name = t["other"]
    other_lang = "en" if code == "pt" else "pt-BR"
    home = base + ("" if code == "pt" else "en/")
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#0b0f0c">
<link rel="canonical" href="{site}/{path}">
<link rel="alternate" hreflang="{t['lang']}" href="{site}/{path}">
<link rel="alternate" hreflang="{other_lang}" href="{site}/{other_path}">
<link rel="icon" type="image/png" sizes="32x32" href="{base}assets/favicon-32.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Great COTW One">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{site}/{path}">
<meta property="og:image" content="{site}/assets/og.png">
<link rel="stylesheet" href="{base}assets/style.css">
{ld}
</head>
<body>
<header class="top">
  <a class="brand" href="{home}"><img src="{base}assets/icon-128.png" alt="" width="32" height="32"><span>Great COTW One</span></a>
  <nav aria-label="menu"><a href="{base}{t['animals']}">{t['animals_t']}</a><a href="{base}{t['reserves']}">{t['reserves_t']}</a></nav>
  <a class="lang" href="{base}{other_path}" hreflang="{other_lang}">{other_name}</a>
</header>
<main class="guide">
{body}
<aside class="cta-box">
  <h2>{e(t['cta_h'])}</h2>
  <p>{e(t['cta_p'])}</p>
  <a class="btn primary" href="{download}" rel="noopener">{e(t['cta'])}</a>
</aside>
<p class="note">{e(t['source'].format(date=DATA_DATE[code]))}</p>
</main>
<footer><p class="links"><a href="{home}">{t['home']}</a> · <a href="{base}{t['animals']}">{t['animals_t']}</a> · <a href="{base}{t['reserves']}">{t['reserves_t']}</a> · {legal}</p></footer>
</body>
</html>
"""


def crumbs(code: str, base: str, items: list[tuple[str, str]], site: str) -> tuple[str, dict]:
    t = L[code]
    home = ("", t["home"]) if code == "pt" else ("en/", t["home"])
    full = [home, *items]
    links = " › ".join(f'<a href="{base}{p}">{e(n)}</a>' for p, n in full[:-1]) + f" › <span>{e(full[-1][1])}</span>"
    ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": f"{site}/{p}"} for i, (p, n) in enumerate(full)],
    }
    return f'<nav class="crumbs" aria-label="breadcrumb">{links}</nav>', ld


def class_chip(cls: int | None, code: str) -> str:
    if not cls:
        return '<span class="chip">—</span>'
    return f'<span class="chip c{cls}" title="{L[code]["class"]} {cls}">{cls}</span>'


# ---------------------------------------------------------------- páginas


def species_page(s: dict, code: str, site: str, download: str, legal) -> tuple[str, str]:
    t = L[code]
    name = s[code if code == "en" else "pt"]
    path = species_url(s, code)
    other = species_url(s, "en" if code == "pt" else "pt")
    base = "../" * path.count("/")
    res_links = ", ".join(f'<a href="{base}{t["reserves"]}{r["slug"]}/">{e(r["name"])}</a>' for r in s["reserves"])
    res_plain = ", ".join(r["name"] for r in s["reserves"])
    n = len(s["reserves"])
    cls = s.get("class") or "—"
    bands = s.get("bands")
    nav, crumb_ld = crumbs(code, base, [(t["animals"], t["animals_t"]), (path, name)], site)
    lowered = name if code == "pt" else name
    intro = t["sp_intro"].format(name=e(name), cls=cls, n=n, res_word=t["res_word"][0 if n == 1 else 1], res=res_links)
    facts = [f'<div><span>{t["class"]}</span><strong>{cls}</strong></div>']
    if bands:
        facts.append(f'<div><span>{t["diamond"]}</span><strong>{num(bands["diamond"], code)}</strong></div>')
    male = (s.get("scoring") or {}).get("Male_Scoring")
    if male:
        facts.append(f'<div><span>{t["weight"]} ({t["male"].lower()})</span><strong>{num(male["weight"][0], code)}–{num(male["weight"][1], code)} kg</strong></div>')
    if has_great_one(s):
        facts.append(f'<div class="go"><span>{t["great_one"]}</span><strong>✓</strong></div>')
    body = [nav, f"<h1>{e(name)}</h1>", f'<p class="lead">{intro}</p>', f'<div class="facts">{"".join(facts)}</div>']

    if bands:
        heads = "".join(f"<th scope='col'>{m}</th>" for m in t["medal_names"])
        vals = "".join(f"<td>{num(bands[k], code)}</td>" for k in ("bronze", "silver", "gold", "diamond", "max"))
        body.append(f'<h2>{t["medals"]}</h2><div class="table-wrap"><table class="medals"><thead><tr>{heads}</tr></thead><tbody><tr>{vals}</tr></tbody></table></div><p class="note">{e(t["medal_note"])}</p>')
    else:
        body.append(f'<h2>{t["medals"]}</h2><p>{e(t["no_medal"])}</p>')

    scoring = s.get("scoring") or {}
    rows = []
    for key, label in (("Male_Scoring", t["male"]), ("Female_Scoring", t["female"]), ("Male_GreatOne_Scoring", f'{t["great_one"]} ({t["male"].lower()})')):
        if key in scoring:
            w = scoring[key]["weight"]
            rows.append(f"<tr><th scope='row'>{e(label)}</th><td>{num(w[0], code)} – {num(w[1], code)} kg</td></tr>")
    if rows:
        body.append(f'<h2>{t["weight"]}</h2><div class="table-wrap"><table class="narrow"><tbody>{"".join(rows)}</tbody></table></div>')

    if s["furs"]:
        fr = "".join(
            f'<tr><th scope="row">{e(fur_name(f["key"], code))}</th><td><span class="rar r{f["rarity"]}">{t["rarities"][min(f["rarity"], 3)]}</span></td><td>{pct(f["chance"], code)}</td></tr>'
            for f in s["furs"]
        )
        body.append(
            f'<h2>{t["furs"]}</h2><div class="table-wrap"><table><thead><tr><th scope="col">{t["fur"]}</th><th scope="col">{t["rarity"]}</th><th scope="col">{t["chance"]}</th></tr></thead><tbody>{fr}</tbody></table></div><p class="note">{e(t["fur_note"])}</p>'
        )
    if has_great_one(s):
        extra = f' {len(s["great_one_furs"])} {t["go_furs"]}.' if s.get("great_one_furs") else ""
        body.append(f'<h2>{t["great_one"]}</h2><p>{e(t["go_yes"])}{e(extra)}</p>')

    faq = []
    if bands:
        faq.append((t["q_diamond"].format(name=lowered), t["a_diamond"].format(name=lowered, d=num(bands["diamond"], code), m=num(bands["max"], code))))
    faq.append((t["q_where"].format(name=lowered), t["a_where"].format(name=name, res=res_plain)))
    rare = rarest(s)
    if rare:
        faq.append((t["q_rare"].format(name=lowered), t["a_rare"].format(fur=fur_name(rare["key"], code), chance=pct(rare["chance"], code))))
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

    diamond_desc = t["sp_diamond_desc"].format(d=num(bands["diamond"], code)) if bands else ""
    title = t["sp_title"].format(name=name)
    desc = t["sp_desc"].format(name=name, cls=cls, diamond=diamond_desc)
    return path, frame(code, path, other, title, desc, "\n".join(body), site, download, legal(code, base), [crumb_ld, faq_ld])


def reserve_page(r: dict, species: dict[str, dict], code: str, site: str, download: str, legal) -> tuple[str, str]:
    t = L[code]
    path = reserve_url(r, code)
    other = reserve_url(r, "en" if code == "pt" else "pt")
    base = "../" * path.count("/")
    nav, crumb_ld = crumbs(code, base, [(t["reserves"], t["reserves_t"]), (path, r["name"])], site)
    seen, rows = set(), []
    for item in sorted(r["species"], key=lambda x: (-(x.get("class") or 0), x[code if code == "en" else "pt"])):
        s = species[item["key"]]
        if s["key"] in seen:
            continue
        seen.add(s["key"])
        name = s[code if code == "en" else "pt"]
        bands = s.get("bands")
        rare = rarest(s)
        go = ' <span class="go-tag">GO</span>' if has_great_one(s) else ""
        rows.append(
            f'<tr><th scope="row"><a href="{base}{species_url(s, code)}">{e(name)}</a>{go}</th><td>{class_chip(s.get("class"), code)}</td>'
            f'<td>{num(bands["diamond"], code) if bands else "—"}</td>'
            f'<td>{e(fur_name(rare["key"], code)) + " · " + pct(rare["chance"], code) if rare else "—"}</td></tr>'
        )
    n = len(rows)
    table = (
        f'<div class="table-wrap"><table><thead><tr><th scope="col">{t["species"]}</th><th scope="col">{t["class"]}</th>'
        f'<th scope="col">{t["diamond"]}</th><th scope="col">{t["rarest"]}</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
    )
    body = "\n".join([nav, f"<h1>{e(r['name'])}</h1>", f'<p class="lead">{e(t["rs_intro"].format(name=r["name"], n=n))}</p>', table, f'<h2>{t["classes_h"]}</h2><p>{e(t["classes_p"])}</p>'])
    title = t["rs_title"].format(name=r["name"])
    desc = t["rs_desc"].format(name=r["name"], n=n)
    return path, frame(code, path, other, title, desc, body, site, download, legal(code, base), [crumb_ld])


SEARCH_JS = """<script>
(function(){var i=document.getElementById('q');if(!i)return;var rows=[].slice.call(document.querySelectorAll('#list tbody tr'));
i.addEventListener('input',function(){var q=i.value.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');
rows.forEach(function(r){r.hidden=q&&r.dataset.k.indexOf(q)<0;});});})();
</script>"""


def animals_index(species: dict[str, dict], code: str, site: str, download: str, legal) -> tuple[str, str]:
    t = L[code]
    path = t["animals"]
    other = L["en" if code == "pt" else "pt"]["animals"]
    base = "../" * path.count("/")
    nav, crumb_ld = crumbs(code, base, [(path, t["animals_t"])], site)
    items = sorted(species.values(), key=lambda s: s[code if code == "en" else "pt"])
    rows = []
    for s in items:
        name = s[code if code == "en" else "pt"]
        bands = s.get("bands")
        res = ", ".join(r["name"] for r in s["reserves"])
        key = slug(name + " " + s["en"] + " " + res).replace("-", " ")
        go = ' <span class="go-tag">GO</span>' if has_great_one(s) else ""
        rows.append(
            f'<tr data-k="{e(key)}"><th scope="row"><a href="{base}{species_url(s, code)}">{e(name)}</a>{go}</th><td>{class_chip(s.get("class"), code)}</td>'
            f'<td>{num(bands["diamond"], code) if bands else "—"}</td><td class="res">{e(res)}</td></tr>'
        )
    body = "\n".join(
        [
            nav,
            f"<h1>{e(t['idx_animals_h'])}</h1>",
            f'<p class="lead">{e(t["idx_animals_p"])}</p>',
            f'<input id="q" class="search" type="search" placeholder="{e(t["search"])}" aria-label="{e(t["search"])}">',
            f'<div class="table-wrap"><table id="list"><thead><tr><th scope="col">{t["species"]}</th><th scope="col">{t["class"]}</th><th scope="col">{t["diamond"]}</th><th scope="col">{t["in_reserves"]}</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>',
            SEARCH_JS,
        ]
    )
    return path, frame(code, path, other, t["idx_animals_title"], t["idx_animals_p"], body, site, download, legal(code, base), [crumb_ld])


def reserves_index(reserves: list[dict], species: dict[str, dict], code: str, site: str, download: str, legal) -> tuple[str, str]:
    t = L[code]
    path = t["reserves"]
    other = L["en" if code == "pt" else "pt"]["reserves"]
    base = "../" * path.count("/")
    nav, crumb_ld = crumbs(code, base, [(path, t["reserves_t"])], site)
    cards = []
    for r in reserves:
        names = sorted({species[s["key"]][code if code == "en" else "pt"] for s in r["species"]})
        cards.append(
            f'<a class="res-card" href="{base}{reserve_url(r, code)}"><h2>{e(r["name"])}</h2><p class="count">{len(names)} {t["n_species"]}</p><p>{e(", ".join(names))}</p></a>'
        )
    body = "\n".join([nav, f"<h1>{e(t['idx_reserves_h'])}</h1>", f'<p class="lead">{e(t["idx_reserves_p"])}</p>', f'<div class="res-grid">{"".join(cards)}</div>'])
    return path, frame(code, path, other, t["idx_reserves_title"], t["idx_reserves_p"], body, site, download, legal(code, base), [crumb_ld])


def build(site: str, download: str, legal) -> list[str]:
    """Escreve todas as páginas de conteúdo e devolve os caminhos (para o sitemap)."""
    reserves, species = load()
    pages: list[tuple[str, str]] = []
    for code in ("pt", "en"):
        pages.append(animals_index(species, code, site, download, legal))
        pages.append(reserves_index(reserves, species, code, site, download, legal))
        for s in species.values():
            pages.append(species_page(s, code, site, download, legal))
        for r in reserves:
            pages.append(reserve_page(r, species, code, site, download, legal))
    for path, text in pages:
        folder = ROOT / path
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(text, encoding="utf-8", newline="\n")
    return [p for p, _ in pages]
