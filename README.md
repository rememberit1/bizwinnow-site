# Business Win Now (bizwinnow.com)

## Overview

Marketing site for **Business Win Now**, a Washington, DC services business that sells done-for-you tech and content work to other businesses. The live site is **https://bizwinnow.com**.

## Purpose

Explain each service, show sample work, list pricing ranges, and drive free-sample requests by email. It is the public face of the company, not an app or dashboard.

## Features / pages

Static pages (built from `pages/*.html`):

| Path | Service |
|------|---------|
| `/` | Home — overview of all services |
| `/govcon` | GovCon RFP compliance matrices and proposal drafting |
| `/real_estate` | MLS virtual staging and short listing reels |
| `/staffing` | Candidate shortlists, skill matrices, tailored resumes |
| `/shopify` | Shopify / DTC checkout and email retention teardowns |
| `/podcast_and_newsletter` | Podcast / newsletter sponsor and guest matchmaking |
| `/matrix` (`matrix.html`) | Standalone sample compliance-matrix page |

Each service page covers who it is for, what you get, process, pricing, FAQ, and a mailto CTA for a free sample. Home and service pages share Inter / Plus Jakarta Sans styling via shared CSS.

## Tech stack

- Static HTML + CSS (+ small `main.js`)
- Python builders: `mkdeploy.py` / `gen.py` / `build.py` assemble pages into a single Cloudflare Worker script (`deploy.js`)
- Deployed as a Cloudflare Worker / Pages-style deploy artifact (not a Node app)

## Run / deploy

```bash
# Preview pages locally
python3 -m http.server 8080
# open http://localhost:8080/index.html or pages/*.html

# Regenerate the Worker deploy bundle
python3 mkdeploy.py   # writes deploy.js

# Confirm all 36 emailed sample paths are in that bundle
node scripts/check-samples.mjs
```

`mkdeploy.py` includes every HTML file under `samples/html/` and refuses to write `deploy.js` if any path in `samples/sent-paths.txt` is missing. Upload / execute `deploy.js` through your Cloudflare account tooling to publish to **bizwinnow.com**.

## License / notes

Independent marketing site. Not affiliated with any government agency.
