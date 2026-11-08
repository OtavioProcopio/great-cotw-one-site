# Great COTW One – site

Página de divulgação do [Great COTW One](https://github.com/OtavioProcopio/great-cotw-one) (pt-BR em `/`, English em `/en/`).

- Site estático, sem framework. As páginas são geradas por `python build.py` (só biblioteca padrão) e o resultado é versionado, pronto para o GitHub Pages.
- Textos em `build.py` (dicionário `T`), estilo em `assets/style.css`.
- Os prints em `assets/img/` vêm do modo de demonstração do app (`?mock`), com dados de exemplo. Nada do jogo é usado.
- SEO: título, descrição, canonical, hreflang, Open Graph, Twitter Card, JSON-LD (`SoftwareApplication` e `FAQPage`), `sitemap.xml` e `robots.txt`. Ao ter domínio próprio, troque `SITE` em `build.py` e rode o gerador.

```bash
python build.py
python -m http.server 8099   # http://localhost:8099
```
