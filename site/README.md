# The Fleet Operator Directory — site

Static site framing the dataset one level up (`../data/operators.csv`):
home page, the alphabetical directory table with client-side search, and
a rendered inclusion-criteria page. Same content-fragment + YAML front
matter -> Jinja2 -> static-output pattern as `sitara-website/site/` and
The Exhibit Cost Record, tinted toward Sitara Skies' purple family.

## Build

```
pip install -r requirements.txt
python build.py            # -> _site/
```

`build.py` calls `scripts/export_data.py`'s `build_substitutions()`,
which regenerates `assets/data/operators.json` from
`../data/operators.csv` every build (sorted alphabetically by name), so
the site can never drift from the source CSV.

## Local preview

```
python -m http.server 8098 -d _site
```

## Deployment target

Designed to be folded into `sitara-skies-website`'s deploy pipeline as
`/records/drone-show-operators/`, the same way `experiential-design-index`
and `exhibit-cost-record` fold into `sitara-website`. `SITE_URL` defaults
to `https://skies.sitara.systems/records/drone-show-operators` (override
via the `SITE_URL` env var for a preview/interim deploy).

Until that fold-in lands, `.github/workflows/deploy-pages.yml` builds and
deploys this repo standalone to GitHub Pages at
`https://sitara-systems.github.io/drone-show-operators/` for preview.

## Status

Built, not yet folded into the parent site's deploy pipeline. Data
research completed 2026-07-22; content pages authored same day. Gate
note: per `Records_Authorities_Instructions.md`, this record ships only
once Nathan confirms at least one live outdoor-operator relationship
exists (design engagement, subcontract, or formalized partnership).
