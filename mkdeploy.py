import base64,json
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
H=lambda n:open('pages/%s.html'%n).read()
# routes -> html
pages={'/':'home','/real_estate':'real_estate','/govcon':'govcon','/staffing':'staffing','/podcast_and_newsletter':'podcast_and_newsletter','/shopify':'shopify'}
PG={k:H(v) for k,v in pages.items()}
NF=H('404')

MX={'doi-udall-garage-drywall-140D0427Q0949':('DOI RFQ 140D0427Q0949: Garage Drywall Demolition, Stewart Lee Udall Building (SB)','Quotes due Nov 19, 2026, 2:00 PM ET'),
'uscg-cape-charles-sewage-70ZL1927QELIZ0002':('USCG RFQ 70ZL1927QELIZ0002: Sewage Lift Station Repairs, Station Cape Charles VA (SB)','Quotes due Dec 2, 2026'),
'ushmm-bollards-95476727Q1104':('USHMM RFQ 95476727Q1104: Retractable Security Bollards Maintenance (USHMM DC + SCCRC Bowie)','Quotes due Dec 1, 2026, 5:00 PM ET'),
'treasury-g7-events-2099AB27Q00003':('Treasury RFQ 2099AB27Q00003: G7 Host Year Integrated Event Management (SB)','Quotes due Nov 25, 2026, 10:00 AM ET'),
'eousa-mdga-court-reporting-15JA0527Q00000009':('EOUSA RFQ 15JA0527Q00000009: Grand Jury/Deposition Court Reporting, USAO MDGA Macon (SB)','Quotes due Dec 2, 2026, 1:00 PM ET'),
'navfac-earle-pest-N4008527R0009':('NAVFAC RFQ N4008527R0009: Pest Control Support Services, NWS Earle NJ (SB)','Quotes due Nov 24, 2026, 11:00 AM ET'),
'nca-salisbury-turf-36C78627Q0021':('VA NCA RFQ 36C78627Q0021: Turf Application Services, Salisbury National Cemetery (SDVOSB)','Quotes due Nov 18, 2026, 4:00 PM ET'),
'uscg-academy-ballfield-70ZH1526QCGA00003':('USCG RFQ 70ZH1526QCGA00003: Ballfield Maintenance, USCGA Nitchman Field Complex (SB)','Quotes due Nov 18, 2026, 8:00 AM ET'),
'eousa-wyoming-court-reporting-15JA0527Q00000004':('EOUSA RFQ 15JA0527Q00000004: Grand Jury Court Reporting, USAO District of Wyoming (SB)','Quotes due Nov 27, 2026, 12:00 PM ET'),
'va-bedford-window-wash-36C24127Q0017':('VA RFQ 36C24127Q0017: Window Washing Services, Bedford Healthcare System (SDVOSB)','Quotes due per Amd 0001 (Nov 2026)'),
'gsa-stelizabeths-gate7-garage-47PB5126R0038':('GSA Solicitation 47PB5126R0038: Gate 7 Parking Garage, St. Elizabeths West Campus DC','Offers due Nov 23, 2026'),
'fort-bragg-pressure-wash-W91247-27-Q-A001':('Army RFQ W91247-27-Q-A001: Pressure Washing, Fort Bragg NC (HUBZone)','Quotes due Nov 23, 2026, 10:00 AM ET'),
}
import glob as _g
MP={k:(_g.glob('/workspace/bwn-kit/img/govcon/2026-1*/'+k+'_matrix_q.png') or _g.glob('/workspace/bwn-kit/img/govcon/2026-1*/'+k+'_matrix.png'))[0] for k in MX}
RX={'brandywine':'11309 Brandywine Rd, Clinton, MD','crain':'123 Robert Crain Highway SE, Upper Marlboro, MD','nicholson14':'14 Nicholson St NW, Washington, DC','villagegreen1732':'1732 Village Green Dr #A-17, Landover, MD','nova1630':'1630 Nova Ave, Capitol Heights, MD','minnesota':'3356 Minnesota Ave SE, Washington, DC','16th':'6805 16th St NW, Washington, DC'}
CL={'nicholson14','villagegreen1732','nova1630','minnesota','16th','brandywine','crain'}
RD='/workspace/bwn-kit/img/listings/2026-10-30/web/'
def rpage(k,a): return f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content="noindex,nofollow"><title>Free photo edit preview | Business Win Now</title>
<style>body{{font-family:Helvetica,Arial,sans-serif;margin:0;color:#1a1a1a;background:#f4f6fa}}main{{max-width:1200px;margin:0 auto;padding:24px}}h1{{color:#0b2545;font-size:22px}}img{{width:100%;border:1px solid #ccd;background:#fff}}a{{color:#0b2545}}.n{{font-size:13px;color:#555}}</style></head><body><main>
<p><b style="color:#0b2545">Business Win Now</b> &middot; Listing photos and visuals</p>
<h1>Free edit preview: {a}</h1><p>Before: the current listing photo. After: an AI-edited preview of the same room or view. Watermarked preview only; the clean full-resolution file is free if you want it.</p>
<img src="/real_estate/samples/{k}.jpg" alt="Before and after photo edit for {a}">
<p class=n>AI-edited preview. If used in a listing, label it as digitally enhanced or virtually staged per MLS rules. Business Win Now is not affiliated with the listing brokerage.</p>
<p>Want the full photo set and a 3D-zoom video? <a href="/real_estate">See listing visuals</a> or email businesswinnow@gmail.com.</p></main></body></html>"""

MD='/workspace/bwn-kit/img/govcon/2026-10-29/'
import html as _h
def mpage(k,t,d): return f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content="noindex,nofollow"><title>Sample compliance matrix | Business Win Now</title>
<style>body{{font-family:Helvetica,Arial,sans-serif;margin:0;color:#1a1a1a;background:#f4f6fa}}main{{max-width:1200px;margin:0 auto;padding:24px}}h1{{color:#0b2545;font-size:22px}}img{{width:100%;border:1px solid #ccd;background:#fff}}a{{color:#0b2545}}.n{{font-size:13px;color:#555}}</style></head><body><main>
<p><b style="color:#0b2545">Business Win Now</b> &middot; Proposal support for small federal contractors</p>
<h1>Sample compliance matrix: {_h.escape(t)}</h1><p>{_h.escape(d)}. A one-page starter matrix built from the public SAM.gov solicitation documents, showing the requirements, where each one is answered, and who owns it.</p>
<img src="/govcon/samples/{k}.png" alt="Compliance matrix for {_h.escape(t)}">
<p class=n>Starter sample, not a complete matrix. Verify every line against the full solicitation and all amendments. Business Win Now is not affiliated with any government agency.</p>
<p>Want the full matrix and a first draft of your proposal? <a href="/govcon">See GovCon proposal support</a> or email businesswinnow@gmail.com.</p></main></body></html>"""
import re as _re
HX={k:_g.glob('/workspace/bwn-kit/img/govcon/2026-11-*/'+k+'_matrix.html') or _g.glob('/workspace/bwn-kit/img/govcon/2026-11-05/'+k+'_matrix.html') for k in MX}
HX={k:v[0] for k,v in HX.items() if v}
MXCSS='.mx{background:#fff;border:1px solid #ccd;padding:12px;overflow-x:auto;font-size:13px}.mx .h{border-bottom:3px solid #c9a227;padding-bottom:6px;margin-bottom:8px}.mx .b{color:#0b2545;font-size:20px;font-weight:bold}.mx table{border-collapse:collapse;width:100%;min-width:900px}.mx th{background:#0b2545;color:#fff;text-align:left;padding:5px}.mx td{border:1px solid #ccd;padding:4px;vertical-align:top}.mx tr:nth-child(even) td{background:#f4f6fa}.mx .n{font-size:11px;color:#555;margin-top:8px}.mx .tag{display:inline-block;background:#c9a227;color:#0b2545;font-weight:bold;padding:1px 6px;border-radius:3px;margin-right:4px}.mx .uv{color:#b00020;font-weight:bold}.mx .wm{text-align:right;margin-top:6px;color:#0b2545;opacity:.35;font-weight:bold}'
def hpage(k,t,d):
    body=_re.search(r'<body>(.*)</body>',open(HX[k]).read(),_re.S).group(1)
    pg=mpage(k,t,d).replace('</style>',MXCSS+'</style>')
    return _re.sub(r'<img src="/govcon/samples/[^"]+\.png"[^>]*>','<div class=mx>'+body.replace('\\','\\\\')+'</div>',pg)
for k,(t,d) in MX.items(): PG['/govcon/samples/'+k]=(hpage if k in HX else mpage)(k,t,d)
def cpage(k,a): return rpage(k,a).replace('an AI-edited preview of the same room or view','a digitally enhanced preview of the same photo (light, color and sharpness adjusted)').replace('AI-edited preview. If used','Digitally enhanced preview. If used').replace('Want the full photo set and a 3D-zoom video?','Want more photos from this listing enhanced?')
for k,a in RX.items(): PG['/real_estate/samples/'+k]=(cpage if k in CL else rpage)(k,a)
S='/workspace/bwn-kit/samples/'
samples=['govcon-draft-technical-approach','real-estate-virtual-staging-sample','staffing-shortlist-sample','newsletter-sponsor-matchmaking-sample','shopify-teardown-sample']
imgs=['re-before-living','re-after-living','re-before-bed','re-after-bed','re-room-still','re-room-3d-zoom-poster']
w="const PG="+json.dumps(PG)+";\nconst NF="+json.dumps(NF)+";\n"
w+="const P="+json.dumps(b('sample-compliance-matrix.pdf'))+";\nconst X="+json.dumps(b('sample-compliance-matrix.xlsx'))+";\n"
w+="const S={"+",".join(json.dumps(n)+":"+json.dumps(b(S+n+'.pdf')) for n in samples)+"};\n"
w+="const MI={"+",".join(json.dumps(k)+":"+json.dumps(b(MP[k])) for k in MX if k not in HX)+"};\n"
w+="const RI={"+",".join(json.dumps(k)+":"+json.dumps(b(_g.glob('/workspace/bwn-kit/img/listings/2026-1*/web/'+k+'.jpg')[0])) for k in RX)+"};\n"
w+="const I={"+",".join(json.dumps(n)+":"+json.dumps(b('assets/%s.jpg'%n)) for n in imgs)+"};\n"
w+="const V="+json.dumps(b('assets/re-room-3d-zoom.mp4'))+";\n"
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
m=p.match(/^\\/real_estate\\/samples\\/([a-z0-9]+)\\.jpg$/);
if(m&&RI[m[1]])return new Response(b(RI[m[1]]),{headers:{'content-type':'image/jpeg','x-robots-tag':'noindex','cache-control':'public, max-age=3600'}});
if((p.startsWith('/govcon/samples/')||p.startsWith('/real_estate/samples/'))&&PG[p])return new Response(PG[p],{headers:{...HT,'x-robots-tag':'noindex, nofollow'}});
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
