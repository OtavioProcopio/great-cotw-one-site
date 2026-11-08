# Great COTW One – site

Página de divulgação do Great COTW One (pt-BR em `/`, English em `/en/`).

- Site estático, sem framework. As páginas são geradas por `python build.py` (só biblioteca padrão) e o resultado é versionado, pronto para o GitHub Pages.
- Textos em `build.py` (dicionário `T`), estilo em `assets/style.css`.
- Os prints em `assets/img/` vêm do modo de demonstração do app (`?mock`), com dados de exemplo. Nada do jogo é usado.
- SEO: título, descrição, canonical, hreflang, Open Graph, Twitter Card, JSON-LD (`SoftwareApplication` e `FAQPage`), `sitemap.xml` e `robots.txt`. Ao ter domínio próprio, troque `SITE` em `build.py` e rode o gerador.

```bash
python build.py
python -m http.server 8099   # http://localhost:8099
```

## Instalador

O código do app é privado. O instalador (`.exe`) é publicado em **Releases deste repositório** pelo CI do repositório do app (segredo `SITE_RELEASES_TOKEN`), e o botão "Baixar" do site aponta para `releases/latest`. Este repositório nunca deve receber código do app, chaves ou arquivos do jogo.

## Atualização automática
Cada release deste repositório leva também `latest.json` e o `.sig` do instalador. O app instalado lê
`releases/latest/download/latest.json` e só instala o que tiver a assinatura da chave de atualização.
Não apague esses arquivos das releases.

## Privacidade e Termos
Textos em `legal.py` (pt-BR e English), escritos a partir do que o app e o servidor fazem.
Antes de abrir a loja: revisão de um advogado e preencher `CONTACT_EMAIL` e `LICENSE_HOST` em `build.py`.
