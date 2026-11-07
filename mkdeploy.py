#!/usr/bin/env python3
"""Build deploy.js, the Cloudflare Worker bundle for bizwinnow.com.

Sample pages are every HTML file under samples/html/. The build refuses to
finish if any path in samples/sent-paths.txt is missing, so a later edit
cannot drop an emailed sample by replacing a short dict of "current" slugs.
"""
import base64, json, sys
from io import BytesIO
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
# Upload path rejects a request over 4 MB. Stay under 3.5 MB decimal.
MAX_DEPLOY_BYTES = 3_500_000

def b64(path):
    return base64.b64encode(Path(path).read_bytes()).decode()

def b64_image(path, max_width, quality):
    """WebP for the bundle. Same URL as the source file; the worker sets image/webp."""
    im = Image.open(path).convert('RGB')
    if im.width > max_width:
        height = max(1, round(im.height * max_width / im.width))
        im = im.resize((max_width, height), Image.Resampling.LANCZOS)
    buf = BytesIO()
    im.save(buf, 'WEBP', quality=quality, method=6)
    return base64.b64encode(buf.getvalue()).decode()

pages = {
    '/': 'home',
    '/real_estate': 'real_estate',
    '/govcon': 'govcon',
    '/staffing': 'staffing',
    '/podcast_and_newsletter': 'podcast_and_newsletter',
    '/shopify': 'shopify',
}
PG = {route: (ROOT / 'pages' / f'{name}.html').read_text() for route, name in pages.items()}
NF = (ROOT / 'pages' / '404.html').read_text()

for folder, prefix in (('govcon', '/govcon/samples/'), ('real_estate', '/real_estate/samples/')):
    for path in sorted((ROOT / 'samples' / 'html' / folder).glob('*.html')):
        PG[prefix + path.stem] = path.read_text()

# Matrix screenshots are 2325px wide and shown in a ~1152px column.
# Photos are shown at most ~1200px wide. WebP at these sizes matches that layout.
MI = {p.stem: b64_image(p, 1400, 78) for p in sorted((ROOT / 'samples' / 'img' / 'govcon').glob('*.png'))}
RI = {p.stem: b64_image(p, 1200, 67) for p in sorted((ROOT / 'samples' / 'img' / 'real_estate').glob('*.jpg'))}

required = [ln.strip() for ln in (ROOT / 'samples' / 'sent-paths.txt').read_text().splitlines() if ln.strip()]
missing = [p for p in required if p not in PG]
if missing:
    sys.exit('refusing to build; emailed sample pages missing from samples/html:\n' + '\n'.join(missing))
for path in required:
    slug = path.rsplit('/', 1)[1]
    html = PG[path]
    if path.startswith('/real_estate/samples/') and slug not in RI:
        sys.exit('refusing to build; listing image missing for ' + path)
    if f'/govcon/samples/{slug}.png' in html and slug not in MI:
        sys.exit('refusing to build; matrix PNG missing for ' + path)
    if f'/real_estate/samples/{slug}.jpg' in html and slug not in RI:
        sys.exit('refusing to build; listing image missing for ' + path)

pdf_names = [
    'govcon-draft-technical-approach',
    'real-estate-virtual-staging-sample',
    'staffing-shortlist-sample',
    'newsletter-sponsor-matchmaking-sample',
    'shopify-teardown-sample',
]
imgs = ['re-before-bed', 're-after-bed', 're-room-still']

w = 'const PG=' + json.dumps(PG) + ';\n'
w += 'const NF=' + json.dumps(NF) + ';\n'
w += 'const P=' + json.dumps(b64(ROOT / 'sample-compliance-matrix.pdf')) + ';\n'
w += 'const X=' + json.dumps(b64(ROOT / 'sample-compliance-matrix.xlsx')) + ';\n'
w += 'const S={' + ','.join(json.dumps(n) + ':' + json.dumps(b64(ROOT / 'samples' / 'pdfs' / f'{n}.pdf')) for n in pdf_names) + '};\n'
w += 'const MI={' + ','.join(json.dumps(k) + ':' + json.dumps(v) for k, v in MI.items()) + '};\n'
w += 'const RI={' + ','.join(json.dumps(k) + ':' + json.dumps(v) for k, v in RI.items()) + '};\n'
w += 'const I={' + ','.join(json.dumps(n) + ':' + json.dumps(b64_image(ROOT / 'assets' / f'{n}.jpg', 1200, 67)) for n in imgs) + '};\n'
w += 'const MP0=' + json.dumps(b64_image(ROOT / 'assets' / 're-room-3d-zoom-poster.jpg', 1200, 67)) + ';\n'
w += 'const MV=' + json.dumps(b64(ROOT / 'assets' / 're-room-3d-zoom.mp4')) + ';\n'
w += r"""function b(s){const r=atob(s),u=new Uint8Array(r.length);for(let i=0;i<r.length;i++)u[i]=r.charCodeAt(i);return u}
const HT={'content-type':'text/html; charset=utf-8'};
export default{fetch(req){const u=new URL(req.url);let p=u.pathname;
if(p.length>1)p=p.replace(/\/+$/,'');
if(p===''||p==='/index.html')p='/';
if(p==='/sample-compliance-matrix.pdf')return new Response(b(P),{headers:{'content-type':'application/pdf'}});
if(p==='/sample-compliance-matrix.xlsx')return new Response(b(X),{headers:{'content-type':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','content-disposition':'attachment; filename="sample-compliance-matrix.xlsx"'}});
let m=p.match(/^\/samples\/([a-z0-9-]+)\.pdf$/);
if(m&&S[m[1]])return new Response(b(S[m[1]]),{headers:{'content-type':'application/pdf','content-disposition':'inline; filename="'+m[1]+'.pdf"'}});
m=p.match(/^\/assets\/([a-z0-9-]+)\.jpg$/);
if(m&&I[m[1]])return new Response(b(I[m[1]]),{headers:{'content-type':'image/webp','cache-control':'public, max-age=86400'}});
if(p==='/assets/re-room-3d-zoom-poster.jpg')return new Response(b(MP0),{headers:{'content-type':'image/webp','cache-control':'public, max-age=86400'}});
if(p==='/assets/re-room-3d-zoom.mp4')return new Response(b(MV),{headers:{'content-type':'video/mp4','cache-control':'public, max-age=86400','accept-ranges':'bytes'}});
m=p.match(/^\/govcon\/samples\/([A-Za-z0-9-]+)\.png$/);
if(m&&MI[m[1]])return new Response(b(MI[m[1]]),{headers:{'content-type':'image/webp','x-robots-tag':'noindex','cache-control':'public, max-age=3600'}});
m=p.match(/^\/real_estate\/samples\/([a-z0-9]+)\.jpg$/);
if(m&&RI[m[1]])return new Response(b(RI[m[1]]),{headers:{'content-type':'image/webp','x-robots-tag':'noindex','cache-control':'public, max-age=3600'}});
if((p.startsWith('/govcon/samples/')||p.startsWith('/real_estate/samples/'))&&PG[p])return new Response(PG[p],{headers:{...HT,'x-robots-tag':'noindex, nofollow'}});
if(Object.prototype.hasOwnProperty.call(PG,p))return new Response(PG[p],{headers:HT});
return new Response(NF,{status:404,headers:HT})}};
"""

# Same deploy wrapper the current bundle uses. The account id is the existing
# Worker account identifier already shipped in this repo; it is not an API token.
code = """async () => { const W=%s; const acc='5d78fcfb5800a50ee9943bd31b926c46'; const b='F'+Date.now();
const meta={main_module:'worker.js',compatibility_date:'2026-10-01'};
const body=['--'+b,'Content-Disposition: form-data; name="metadata"','Content-Type: application/json','',JSON.stringify(meta),'--'+b,'Content-Disposition: form-data; name="worker.js"; filename="worker.js"','Content-Type: application/javascript+module','',W,'--'+b+'--'].join('\\r\\n');
const r=await cloudflare.request({method:'PUT',path:`/accounts/${acc}/workers/scripts/businesswinnow`,body,contentType:'multipart/form-data; boundary='+b,rawBody:true});
const s=await cloudflare.request({method:'POST',path:`/accounts/${acc}/workers/scripts/businesswinnow/subdomain`,body:{enabled:true}});
return {ok:r.success,sub:s.success}; }""" % json.dumps(w)
out = ROOT / 'deploy.js'
out.write_text(code)
size = out.stat().st_size
print('worker', len(w), 'deploy.js', size, 'pages', len(PG), 'png', len(MI), 'jpg', len(RI))
if size >= MAX_DEPLOY_BYTES:
    sys.exit('deploy.js is %d bytes; the upload cap needs it under %d' % (size, MAX_DEPLOY_BYTES))
