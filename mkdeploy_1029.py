import base64,json
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
H=lambda n:open('pages/%s.html'%n).read()
# routes -> html
pages={'/':'home','/real_estate':'real_estate','/govcon':'govcon','/staffing':'staffing','/podcast_and_newsletter':'podcast_and_newsletter','/shopify':'shopify'}
PG={k:H(v) for k,v in pages.items()}
NF=H('404')

MX={'dha-wrnmmc-hospital-comms-HT001426QE048':('DHA RFQ HT001426QE048: WRNMMC Hospital Communications Support','Quotes due Nov 9, 2026, 3:00 PM ET'),
'dot-graphic-design-693JK427R500001':('DOT RFP 693JK427R500001: Graphic Design Support Services (WOSB set-aside)','Proposals due Dec 3, 2026, 11:30 PM ET'),
'usmc-edcom-it-support-M0026427R0001':('USMC RFP M0026427R0001: EDCOM IT Support Services (WOSB)','Proposals due Nov 9, 2026, 10:00 AM ET')}
MD='/workspace/bwn-kit/img/govcon/2026-10-29/'
import html as _h
def mpage(k,t,d): return f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content="noindex,nofollow"><title>Sample compliance matrix | Business Win Now</title>
<style>body{{font-family:Helvetica,Arial,sans-serif;margin:0;color:#1a1a1a;background:#f4f6fa}}main{{max-width:1200px;margin:0 auto;padding:24px}}h1{{color:#0b2545;font-size:22px}}img{{width:100%;border:1px solid #ccd;background:#fff}}a{{color:#0b2545}}.n{{font-size:13px;color:#555}}</style></head><body><main>
<p><b style="color:#0b2545">Business Win Now</b> &middot; Proposal support for small federal contractors</p>
<h1>Sample compliance matrix: {_h.escape(t)}</h1><p>{_h.escape(d)}. A one-page starter matrix built from the public SAM.gov solicitation documents, showing the requirements, where each one is answered, and who owns it.</p>
<img src="/govcon/samples/{k}.png" alt="Compliance matrix for {_h.escape(t)}">
<p class=n>Starter sample, not a complete matrix. Verify every line against the full solicitation and all amendments. Business Win Now is not affiliated with any government agency.</p>
<p>Want the full matrix and a first draft of your proposal? <a href="/govcon">See GovCon proposal support</a> or email businesswinnow@gmail.com.</p></main></body></html>"""
for k,(t,d) in MX.items(): PG['/govcon/samples/'+k]=mpage(k,t,d)
S='/workspace/bwn-kit/samples/'
samples=['govcon-draft-technical-approach','real-estate-virtual-staging-sample','staffing-shortlist-sample','newsletter-sponsor-matchmaking-sample','shopify-teardown-sample']
imgs=['re-before-living','re-after-living','re-before-bed','re-after-bed']
w="const PG="+json.dumps(PG)+";\nconst NF="+json.dumps(NF)+";\n"
w+="const P="+json.dumps(b('sample-compliance-matrix.pdf'))+";\nconst X="+json.dumps(b('sample-compliance-matrix.xlsx'))+";\n"
w+="const S={"+",".join(json.dumps(n)+":"+json.dumps(b(S+n+'.pdf')) for n in samples)+"};\n"
w+="const MI={"+",".join(json.dumps(k)+":"+json.dumps(b(MD+k+'_matrix.png')) for k in MX)+"};\n"
w+="const I={"+",".join(json.dumps(n)+":"+json.dumps(b('assets/%s.jpg'%n)) for n in imgs)+"};\n"
w+="""function b(s){const r=atob(s),u=new Uint8Array(r.length);for(let i=0;i<r.length;i++)u[i]=r.charCodeAt(i);return u}
const HT={'content-type':'text/html; charset=utf-8'};
export default{fetch(req){const u=new URL(req.url);let p=u.pathname;
if(p.length>1)p=p.replace(/\\/+$/,'');
if(p===''||p==='/index.html')p='/';
if(p==='/sample-compliance-matrix.pdf')return new Response(b(P),{headers:{'content-type':'application/pdf'}});
if(p==='/sample-compliance-matrix.xlsx')return new Response(b(X),{headers:{'content-type':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','content-disposition':'attachment; filename="sample-compliance-matrix.xlsx"'}});
let m=p.match(/^\\/samples\\/([a-z0-9-]+)\\.pdf$/);
if(m&&S[m[1]])return new Response(b(S[m[1]]),{headers:{'content-type':'application/pdf','content-disposition':'inline; filename="'+m[1]+'.pdf"'}});
m=p.match(/^\\/assets\\/([a-z0-9-]+)\\.jpg$/);
if(m&&I[m[1]])return new Response(b(I[m[1]]),{headers:{'content-type':'image/jpeg','cache-control':'public, max-age=86400'}});
m=p.match(/^\\/govcon\\/samples\\/([A-Za-z0-9-]+)\\.png$/);
if(m&&MI[m[1]])return new Response(b(MI[m[1]]),{headers:{'content-type':'image/png','x-robots-tag':'noindex','cache-control':'public, max-age=3600'}});
if(p.startsWith('/govcon/samples/')&&PG[p])return new Response(PG[p],{headers:{...HT,'x-robots-tag':'noindex, nofollow'}});
if(Object.prototype.hasOwnProperty.call(PG,p))return new Response(PG[p],{headers:HT});
return new Response(NF,{status:404,headers:HT})}};"""
code="""async () => { const W=%s; const acc='5d78fcfb5800a50ee9943bd31b926c46'; const b='F'+Date.now();
const meta={main_module:'worker.js',compatibility_date:'2026-10-01'};
const body=['--'+b,'Content-Disposition: form-data; name="metadata"','Content-Type: application/json','',JSON.stringify(meta),'--'+b,'Content-Disposition: form-data; name="worker.js"; filename="worker.js"','Content-Type: application/javascript+module','',W,'--'+b+'--'].join('\\r\\n');
const r=await cloudflare.request({method:'PUT',path:`/accounts/${acc}/workers/scripts/businesswinnow`,body,contentType:'multipart/form-data; boundary='+b,rawBody:true});
const s=await cloudflare.request({method:'POST',path:`/accounts/${acc}/workers/scripts/businesswinnow/subdomain`,body:{enabled:true}});
return {ok:r.success,sub:s.success}; }""" % json.dumps(w)
open('deploy.js','w').write(code)
open('/tmp/worker.js','w').write(w)
print(len(w),len(code))
