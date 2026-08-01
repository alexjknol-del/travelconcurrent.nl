# TravelConcurrent.nl

Broncode voor [travelconcurrent.nl](https://travelconcurrent.nl), een onafhankelijk inspiratieplatform voor reizen: de beste aanbieders op reisgebied, besparen op reizen en actuele deals.

Gebouwd met [Astro](https://astro.build) (statische site, geen server nodig) en gehost via Cloudflare Pages.

## Structuur

- `src/pages/` — alle pagina's (home, over, contact, juridische pagina's, dynamische routes voor nieuws en aanbieders)
- `src/content/blog/` — blogartikelen (markdown), verschijnen onder `/nieuws/...`
- `src/content/aanbieders/` — bedrijfsprofielen (markdown), verschijnen onder `/aanbieders/...`
- `src/layouts/` — gedeelde paginalayout
- `src/components/` — header en footer
- `src/styles/global.css` — alle styling (geen losse CSS-framework, bewust lichtgewicht)
- `public/afbeeldingen/` — favicon, OG-afbeelding en de illustratie van de redactie
- `scripts/make_og_image.py` — genereert de gedeelde social-share-afbeelding (`public/afbeeldingen/og-default.png`); alleen nodig als die afbeelding ooit opnieuw gemaakt moet worden

## Nieuw artikel of aanbieder toevoegen

Voeg een nieuw `.md`-bestand toe in `src/content/blog/` (artikel) of `src/content/aanbieders/` (bedrijfsprofiel) met de juiste frontmatter (zie bestaande bestanden als voorbeeld). Bij een nieuwe push naar de hoofdbranch bouwt Cloudflare Pages de site automatisch opnieuw.

## Lokaal ontwikkelen

```bash
npm install
npm run dev       # lokale ontwikkelserver
npm run build     # productie-build naar dist/
npm run preview   # preview van de build
```

## Hosting

De site draait op Cloudflare Pages, gekoppeld aan deze GitHub-repository. Build-instellingen:

- **Build command:** `npm run build`
- **Build output directory:** `dist`
- **Root directory:** `/`

Elke push naar de hoofdbranch triggert automatisch een nieuwe deploy.
