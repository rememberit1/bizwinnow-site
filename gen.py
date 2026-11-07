import os, html
E=html.escape
CSS=open('base.css').read()+open('extra.css').read()
MAIL='businesswinnow@gmail.com'
LOGO='<svg viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6366f1"/><stop offset="1" stop-color="#f5b83d"/></linearGradient></defs><rect width="32" height="32" rx="9" fill="url(#lg)"/><path d="M8 21l5-6 4 4 7-9" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FAV="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='9' fill='%234f46e5'/%3E%3Cpath d='M8 21l5-6 4 4 7-9' fill='none' stroke='%23fff' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"
ICO={
'real_estate':'<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
'govcon':'<path d="M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8z"/><path d="M14 3v5h5"/><path d="M9 14l2 2 4-4"/>',
'staffing':'<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M17 11l1.8 1.8L22 9.5"/>',
'podcast_and_newsletter':'<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0"/><path d="M12 18v3"/>',
'shopify':'<path d="M3 4h2l2.2 11h10.6L20 8H6.2"/><circle cx="9" cy="19.5" r="1.4"/><circle cx="17" cy="19.5" r="1.4"/>'}
def ico(k,cls='ico'): return '<div class="%s"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></div>'%(cls,ICO[k])
def mail(subj): return 'mailto:%s?subject=%s'%(MAIL,subj.replace(' ','%20').replace(':','%3A'))

SV=[ # key,title,who,price html,short blurb,mail subject
('govcon','GovCon RFP Compliance Matrix &amp; Proposal Drafting','Small federal and state contractors','From $300&ndash;$1,500 per proposal','A compliance matrix, bid/no-bid summary and first draft built from the solicitation.','Free sample: GovCon compliance matrix'),
('real_estate','MLS Virtual Staging &amp; Listing Reels','Real estate agents and brokerages','From $99&ndash;$249 per listing pack<br><span style="font-weight:400;font-size:.9rem">Monthly brokerage retainer available.</span>','Furnished-looking listing photos and a short vertical reel, delivered as one pack.','Free sample: MLS virtual staging'),
('staffing','Candidate Shortlists &amp; Resume Tailoring','Boutique tech staffing agencies','From $300&ndash;$500 per shortlist<br><span style="font-weight:400;font-size:.9rem">Or a monthly sourcing seat.</span>','Three matched candidates per open req, with resumes tailored to the job.','Free sample: candidate shortlist'),
('podcast_and_newsletter','Podcast &amp; Newsletter Sponsor / Guest Matchmaking','B2B creators, podcast hosts, newsletter writers and founders','20&ndash;30% commission on sponsorship deals<br><span style="font-weight:400;font-size:.9rem">Or $1,000&ndash;$2,500/mo for guest booking.</span>','Sponsors and guest spots found, pitched and packaged with a media kit.','Free sample: sponsor or guest matchmaking'),
('shopify','Checkout &amp; Email Retention Teardowns','Shopify and DTC brands','From $300 setup<br><span style="font-weight:400;font-size:.9rem">Plus monthly management.</span>','A teardown of your emails and product pages, with copy ready to paste in.','Free sample: email retention teardown'),
]
SVD={s[0]:s for s in SV}
NAVL=[('govcon','GovCon'),('real_estate','Real estate'),('staffing','Staffing'),('podcast_and_newsletter','Podcast &amp; newsletter'),('shopify','Shopify')]

def nav(cur):
    l=''.join('<a%s href="/%s">%s</a>'%(' class="cur"' if k==cur else '',k,t) for k,t in NAVL)
    return '<nav><div class="w"><a class="brand" href="/"><b>%sBusiness Win Now</b></a><div>%s<a class="k" href="/#contact">Contact</a></div></div></nav>'%(LOGO,l)
def foot():
    l=''.join('<a href="/%s">%s</a>'%(k,t) for k,t in NAVL)
    return '<footer><div class="w"><div class="fl"><a href="/">Home</a>%s<a href="mailto:%s">%s</a></div><div class="fine">&copy; 2026 Business Win Now &middot; Washington, DC &middot; Independent services; not affiliated with any government agency.</div></div></footer>'%(l,MAIL,MAIL)
def page(title,desc,cur,body,status=''):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    '<title>%s</title><meta name="description" content="%s"><link rel="icon" href="%s">'
    '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">'
    '<style>%s</style></head><body>%s%s%s</body></html>')%(title,E(desc,quote=True) if '&' not in desc else desc.replace('"','&quot;'),FAV,CSS,nav(cur),body,foot())

def cards(items,cls='card'):
    return ''.join('<div class="%s"><h3>%s</h3>%s</div>'%(cls,t,d) for t,d in items)
def steps(items):
    return '<div class="grid">'+''.join('<div class="card step"><b>%d</b><h3>%s</h3>%s</div>'%(i+1,t,d) for i,(t,d) in enumerate(items))+'</div>'
def faq(items):
    return '<div class="faq">'+''.join('<details><summary>%s</summary><p>%s</p></details>'%(q,a) for q,a in items)+'</div>'
def cta(h,p,subj,label='Request a free sample'):
    return '<section class="cta" id="contact"><div class="w"><h2>%s</h2><p>%s</p><a class="btn" href="%s">%s</a> <a class="btn o" href="mailto:%s">%s</a></div></section>'%(h,p,mail(subj),label,MAIL,MAIL)

def svc_page(k,eyebrow,lead,who,problem,gets,process,pricing,samples,faqs,ctah,ctap,desc,extra_mid='',extra_after=''):
    s=SVD[k]
    hero='<header class="hero sm"><div class="w"><p class="crumb"><a href="/">Home</a> / %s</p><span class="eyebrow">%s</span><h1>%s</h1><p>%s</p><a class="btn" href="%s">Request a free sample</a><a class="btn o" href="#sample">See the sample</a></div></header>'%(s[1],eyebrow,s[1],lead,mail(s[5]))
    body=hero
    body+='<section><div class="w"><h2>Who it&rsquo;s for, and the problem</h2><div class="two"><div class="card tint"><span class="k">Who it&rsquo;s for</span>%s</div><div class="card tint"><span class="k">The problem</span>%s</div></div></div></section>'%(who,problem)
    body+='<section id="what"><div class="w"><h2>What you get</h2><div class="grid s">%s</div>%s</div></section>'%(cards(gets),extra_mid)
    sample_block='<section id="sample"><div class="w"><h2>Sample work</h2>%s</div></section>'%samples
    if k=='real_estate': body+=sample_block
    body+='<section id="process"><div class="w"><h2>How it works</h2>%s</div></section>'%steps(process)
    body+='<section id="pricing"><div class="w"><h2>Pricing</h2>%s</div></section>'%pricing
    if k!='real_estate': body+=sample_block
    if extra_after: body+=extra_after
    body+='<section id="faq"><div class="w"><h2>Questions</h2>%s</div></section>'%faq(faqs)
    body+=cta(ctah,ctap,s[5])
    return page('%s | Business Win Now'%s[1].replace('&amp;','&'),desc,k,body)
def price1(big,sub,note):
    return '<div class="two"><div class="card tint"><span class="k">Pricing</span><div class="big">%s</div>%s</div><div class="card"><span class="k">Good to know</span>%s</div></div>'%(big,sub,note)
def ul(items): return '<ul class="plain">'+''.join('<li>%s</li>'%i for i in items)+'</ul>'
def pdfs(*pairs): return '<div class="links">'+''.join('<a class="btn ghost" href="%s">%s</a>'%p for p in pairs)+'</div>'

P={}
# ---------- HOME
def home():
    cardsh=''
    for k,t,who,price,blurb,subj in SV:
        cardsh+='<div class="card svc">%s<h3>%s</h3><p class="for"><b>Who it&rsquo;s for:</b> %s</p><p class="blurb">%s</p><div class="from">%s</div><a class="btn" href="/%s">Learn more</a></div>'%(ico(k),t,who,blurb,price,k)
    body=('<header class="hero"><div class="w"><h1>Done-for-you tech expertise that wins you more business.</h1>'
    '<p>Five focused services for small businesses that need strong work without hiring a team: federal proposal support, staged listing photos, candidate shortlists, sponsor and guest matchmaking, and store teardowns for Shopify brands.</p>'
    '<a class="btn" href="#services">See all 5 services</a><a class="btn o" href="%s">Request a free sample</a><p class="em">Calls only if you want them &mdash; otherwise everything is handled efficiently by email.</p></div></header>'%mail('Free sample request'))
    body+='<section id="services"><div class="w"><h2>Services</h2><p class="lead">Pick the one that fits your business. Each has its own page with details, pricing and a sample.</p><div class="grid s">%s</div></div></section>'%cardsh
    body+=('<section id="how"><div class="w"><h2>How it works</h2>'+steps([
     ('Email us','Tell us what you need and send any links or files. No forms, and calls only if you want one.'),
     ('Get a free sample','We do a small piece of the real work so you can judge the quality first.'),
     ('Approve a quote','Final quotes are given up front. Listed prices are starting points.'),
     ('Receive the work','Delivered by email. You review it, ask for changes and stay in control of the final call.')])+'</div></section>')
    body+=('<section id="why"><div class="w"><h2>Why Business Win Now</h2><div class="grid">'+cards([
     ('Built by an engineer','Founder Ben is a mobile software engineer, so the technical work is done by someone who builds software for a living.'),
     ('Based in Washington, DC','A local business, reachable by email and straightforward about scope and price.'),
     ('Email-only, on your schedule','Work arrives in your inbox and everything moves efficiently by email. Prefer to talk? A call is available whenever you want one.'),
     ('Quoted before we start','You see the price before any paid work begins, and your first sample is free.')])+'</div></div></section>')
    body+=cta('Contact','Not sure which service fits? Email what you are working on and we will point you to the right one, or start your free sample.','Free sample request')
    return page('Business Win Now | Done-for-you tech expertise that wins you more business',
     'Business Win Now is a Washington, DC business offering five done-for-you services by email: GovCon proposal support, virtual staging and listing reels, candidate shortlists, podcast and newsletter sponsor matchmaking, and Shopify email and checkout teardowns.','home',body)
P['/']=home()

# ---------- REAL ESTATE
re_samples=('<p>These samples are watermarked, and the furnishings are AI-generated.</p>'
 '<h3 class="zoom-heading" style="margin-top:0">One still photo, with depth-based motion</h3><p>The same room as an empty still, then virtually staged with AI-generated furnishings and a short 3D parallax zoom.</p>'
 '<div class="ba zoom"><figure><img src="/assets/re-room-still.jpg" alt="Before: the empty living room as a still listing photo" width="960" height="600"><figcaption>Before: still photo, as listed</figcaption></figure>'
 '<figure><video muted autoplay loop playsinline preload="metadata" width="960" height="600" poster="/assets/re-room-3d-zoom-poster.jpg" aria-label="Eight-second depth-based parallax zoom through the same living room, virtually staged with AI-generated furnishings"><source src="/assets/re-room-3d-zoom.mp4" type="video/mp4">Your browser cannot play this sample; the still photo is shown alongside.</video><figcaption>After: virtually staged + 3D zoom video</figcaption></figure></div>'
 '<p class="cap">The furnishings are AI-generated. The video applies a depth-map camera push-in and parallax motion to the virtually staged photo. The motion is a rendered perspective effect, not a full 3D room scan.</p>'
 '<div class="ba"><figure><img src="/assets/re-before-bed.jpg" alt="Bedroom listing photo before staging" width="1000" height="750"><figcaption>Before: bedroom, as listed</figcaption></figure>'
 '<figure><img src="/assets/re-after-bed.jpg" alt="Same bedroom after virtual staging" width="1000" height="750"><figcaption>After: virtually staged</figcaption></figure></div>'
 '<p class="cap">Sample images start from a public listing photo and are not a client project.</p>'
 +pdfs(('/samples/real-estate-virtual-staging-sample.pdf','Virtual staging PDF')))
P['/real_estate']=svc_page('real_estate','For listing agents &amp; brokerages',
 'Empty, dated or awkward rooms photograph poorly and get scrolled past. We restyle the photos you already have and cut them into a short vertical clip, so the listing looks furnished and ready to post.',
 ul(['Listing agents with vacant or dated homes','Teams and brokerages that want a consistent look across their listings','Agents who post listings to Instagram, TikTok or Reels']),
 '<p style="margin:0">Bare rooms look small and cold in photos, and buyers struggle to picture living there. Physical staging takes time and money before the listing even goes live.</p>',
 [('Staged room photos','We restyle your existing listing photos with furniture, rugs, art and lighting. The room itself stays the same.'),
  ('Style matched to the home','The look is chosen to suit the property and its likely buyer, from clean and neutral to warm and modern.'),
  ('A 15-second vertical clip','A slow pan and zoom across the staged photos, sized for Reels, TikTok and Stories.'),
  ('Before and after pairs','Side-by-side images that make the transformation obvious in a post.'),
  ('Ready-to-post delivery','Files arrive by email as one listing pack, ready to upload to the MLS and your social accounts.'),
  ('Honestly labeled','Staged rooms are AI-generated, and we review each render against the original photo. Label them as virtually staged and check your MLS rules.')],
 [('Send the listing','Email the listing link or the photos you want restyled.'),('Free sample','We stage one room so you can see the result on your own listing.'),('Choose the pack','Pick the rooms and whether you want the clip. Most listings benefit from the living room, main bedroom and kitchen or dining area.'),('Receive the pack','Staged photos and the clip land in your inbox, ready to use.')],
 price1('$99&ndash;$249 <span style="font-size:1rem;font-weight:600;color:var(--mu);-webkit-text-fill-color:var(--mu)">per listing pack</span>','<p style="margin:0">Monthly brokerage retainer available.</p>',
  ul(['Where you land in the range depends on how many rooms are staged and whether the reel is included.','Your first sample is free, and the full quote is given up front.','Rooms that are already furnished gain little, so we recommend staging the empty or dated ones.'])),
 re_samples,
 [('Is virtual staging allowed on the MLS?','Rules differ by MLS and brokerage. Label staged images as virtually staged and keep the original photos available. Check with your MLS if you are unsure.'),
  ('Do you offer 3D tours?','Not full walkthrough tours. We can add a depth-based 3D parallax zoom, like the sample above, to a listing reel. It is a perspective video made from a still photo, not a 3D scan.'),
  ('What do you need from me?','The listing link or the original photos. Wide, well-lit shots of empty rooms give the best results.'),
  ('Can a brokerage get a recurring arrangement?','Yes. A monthly retainer is available. Email us how many listings you handle and we will quote it.')],
 'Stage a room from your own listing','Send a listing link and we will restyle one room for free, so you can see it on a real home.',
 'Virtual staging and short vertical listing reels for real estate agents and brokerages, delivered by email as a listing pack. From $99 to $249 per listing pack.')

# ---------- GOVCON
gov_cards=cards([
 ('Bid/no-bid summaries','A one-page brief on scope, set-aside, deadlines, evaluation factors and red flags, so you can decide fast.'),
 ('Compliance matrices','Every "shall," instruction and evaluation item pulled from the solicitation and mapped to where your response answers it.'),
 ('Outlines &amp; first drafts','A proposal outline that follows the instructions, plus first-draft technical narrative ready for your edits.'),
 ('Deadline tracking','Question deadlines, amendments and due dates (with time zones) tracked so nothing slips.')])
gov_why='<section id="why"><div class="w"><h2>Why Business Win Now for federal bids</h2><div class="grid">'+cards([
 ('Federal project background','Founder Ben is a mobile software engineer who has worked on federal projects, including the Library of Congress LOC Collections app (2019&ndash;2021) and the MyMilitary Health Care app (2024&ndash;present).'),
 ('Fast turnaround','Compliance matrices and bid summaries delivered quickly, so you have more time before the deadline.'),
 ('You keep control','Your pricing, past performance and final decisions stay with you. We do the heavy lifting on the documents.')])+'</div></div></section>'
gov_price='<div class="grid">'+cards([
 ('First matrix','<div class="price">Free</div>Your first compliance matrix on a live bid costs nothing. See the quality before you pay.'),
 ('Per proposal','<div class="price">$300&ndash;$1,500</div>Flat fee, based on solicitation size and scope. Quoted up front.'),
 ('Optional win bonus','<div class="price">If you win</div>Lower flat fee plus an agreed bonus only when you win the award.')])+'</div>'
gov_sample=('<p>A sample compliance matrix for a real, open VA solicitation: RFQ 36C26026Q1017 (Portland VA EMS Quality Assurance Inspection SaaS, SDVOSB set-aside, NAICS 541519).</p>'
 +pdfs(('/sample-compliance-matrix.pdf','Download sample matrix (PDF)'),('/sample-compliance-matrix.xlsx','Excel version'),('/samples/govcon-draft-technical-approach.pdf','Draft technical approach (PDF)')))
P['/govcon']=svc_page('govcon','For federal &amp; state contractors',
 'Federal solicitations bury what matters across dozens of pages and amendments. Send us the bid and we return a compliance matrix, a bid/no-bid summary and a first-draft technical response, so your time goes to pricing and past performance.',
 ul(['Small federal and state contractors bidding on RFPs and RFQs','Small-business and set-aside bidders, such as SDVOSB firms','Owner-run teams without a dedicated proposal manager']),
 '<p style="margin:0">Every &ldquo;shall&rdquo; has to be answered, amendments quietly change the requirements, and deadlines for questions and quotes are easy to miss. One overlooked instruction can sink an otherwise strong quote.</p>',
 [('Solicitation breakdown','We read the RFP or RFQ and every amendment, then pull out scope, set-aside, evaluation factors and instructions.'),
  ('Compliance matrix','Each requirement mapped to the section of your response that answers it, delivered as PDF and Excel.'),
  ('Bid/no-bid summary','A short brief with the red flags called out, so you can decide quickly whether the bid is worth your time.'),
  ('Proposal outline','An outline that follows the submission instructions and the order of the evaluation criteria.'),
  ('First-draft technical response','Draft narrative written to the evaluation criteria, ready for you to edit and add detail.'),
  ('Dates and deadlines','Question deadlines, amendment dates and due dates, with time zones, in one place.')],
 [('Send the bid','Email the SAM.gov link or solicitation number.'),('We break it down','We read the RFP/RFQ and amendments and build your compliance matrix and bid summary.'),('We draft','Outline and first draft of the technical volume, written to the evaluation criteria.'),('You finalize','You add pricing and past performance, review and submit. You stay in control.')],
 gov_price,gov_sample,
 [('Do you submit the proposal for me?','No. You add your pricing and past performance, review everything and submit it yourself.'),
  ('What do you need to start?','The SAM.gov link or the solicitation number. We pull the solicitation and amendments from there.'),
  ('Is the first matrix really free?','Yes. Your first compliance matrix on a live bid costs nothing, so you can judge the quality before you pay.'),
  ('How is the price set?','As a flat fee based on the size and scope of the solicitation, quoted up front. There is also an option for a lower fee plus a bonus if you win.')],
 'Send us a bid','Have a bid on your list? Send the solicitation number and we will start your free matrix.',
 'Compliance matrices, bid/no-bid summaries and first-draft technical responses for small federal and state contractors. From $300 to $1,500 per proposal; first matrix free.',
 extra_after=gov_why)
# govcon: unique blocks reuse existing text; "Dates and deadlines" card duplicates minor wording on purpose from existing section moved

# ---------- STAFFING
P['/staffing']=svc_page('staffing','For staffing agencies',
 'When a req lands, speed and fit decide whose candidates get seen. We build the shortlist and tailor each resume to the job, so your recruiters send sharper submittals sooner.',
 ul(['Boutique tech staffing agencies and small recruiting firms','Recruiters carrying several open reqs at once']),
 '<p style="margin:0">Sorting resumes against a long list of required skills eats a recruiter&rsquo;s day, and a generic resume does not show a client how closely a candidate matches the req.</p>',
 [('A three-candidate shortlist','For each open req you get three candidates who match the posting, rather than a pile of resumes to sort.'),
  ('Skill matrix','Each candidate is compared against the posting&rsquo;s mandatory and preferred skills, so gaps are visible at a glance.'),
  ('Tailored resumes','Resumes are rewritten to the job requirements using what is already in the candidate&rsquo;s background, with nothing invented.'),
  ('Matched to your job ID','Work is organized by your req or job ID, so it drops straight into your tracking.'),
  ('Short fit notes','A line or two per candidate on why they fit and what to confirm before you submit.')],
 [('Send the req','Email the job ID and the posting or description.'),('Free sample','We build a shortlist for one req so you can judge the format and the matches.'),('Receive the shortlist','The shortlist, skill matrix and tailored resumes arrive by email.'),('You review and submit','You decide who goes to the client.')],
 price1('$300&ndash;$500 <span style="font-size:1rem;font-weight:600;color:var(--mu);-webkit-text-fill-color:var(--mu)">per shortlist</span>','<p style="margin:0">Or a monthly sourcing seat.</p>',
  ul(['Quoted up front for your reqs.','A monthly sourcing seat suits agencies with a steady flow of open roles.','The first sample is free.'])),
 '<p>An example shortlist for a full-stack developer posting, with the skill matrix. The candidates in the sample are fictional and invented to show the format.</p>'+pdfs(('/samples/staffing-shortlist-sample.pdf','Shortlist PDF (example candidates)')),
 [('Are the candidates in the sample real?','No. They are fictional profiles that show the format. For a real req, candidates are sourced and screened before they reach you.'),
  ('What do you need from me?','The job ID and the posting or description. Must-have skills and location rules help us match more closely.'),
  ('Do you change what is on a candidate&rsquo;s resume?','We reword and reorder to match the job, using only the candidate&rsquo;s real background. Nothing is invented.'),
  ('What is a monthly sourcing seat?','A recurring arrangement for agencies with a steady stream of reqs. Email us your volume and we will quote it.')],
 'Send us one open req','Send a job ID and posting and we will build a free sample shortlist.',
 'Three-candidate shortlists, skill matrices and tailored resumes for boutique tech staffing agencies. From $300 to $500 per shortlist, or a monthly sourcing seat.')

# ---------- PODCAST / NEWSLETTER
P['/podcast_and_newsletter']=svc_page('podcast_and_newsletter','For creators &amp; founders',
 'Shows and newsletters grow on the right sponsors and the right guest spots, but finding and pitching them is slow work. We find the matches, write the pitches and package your audience into a media kit.',
 ul(['B2B podcast hosts and newsletter writers who want paid sponsors','Founders and experts who want to be booked as guests on relevant shows']),
 '<p style="margin:0">Sponsor outreach keeps slipping behind the content itself, generic pitches get ignored, and without a media kit it is hard to show a sponsor what they would be buying.</p>',
 [('Sponsor matching','A target list of brands that fit your audience, with the reasoning for each match.'),
  ('Sponsor pitches','Pitch emails written for each target, drafted for your approval before anything goes out.'),
  ('Guest pitching','Pitches to relevant shows with a custom angle for each, built around what you can talk about.'),
  ('Media kits','A clean one-pager covering your audience, format and sponsorship options.'),
  ('Two ways to work together','Pay a commission on sponsorship deals, or a monthly fee for guest booking.')],
 [('Share your show','Send a link to your podcast or newsletter and tell us who your audience is.'),('Free sample','We send a short list of matched sponsors or shows with the pitch angle for each.'),('We pitch','We write and manage outreach, and you approve the pitches.'),('You close or book','Deals and guest spots are confirmed with you before they are final.')],
 price1('20&ndash;30% <span style="font-size:1rem;font-weight:600;color:var(--mu);-webkit-text-fill-color:var(--mu)">commission on sponsorship deals</span>','<p style="margin:0">Or $1,000&ndash;$2,500/mo for guest booking.</p>',
  ul(['The commission rate within the range is agreed up front.','Guest booking is a monthly fee, quoted for your goals.','The first sample is free.'])),
 '<p>A sample sponsor matchmaking write-up, showing how matches and pitch angles are laid out.</p>'+pdfs(('/samples/newsletter-sponsor-matchmaking-sample.pdf','Sponsor matchmaking PDF')),
 [('Do I pay if no sponsor signs?','The commission applies to sponsorship deals, so you pay it only when a deal closes. The guest-booking option is a separate monthly fee.'),
  ('Who sends the pitches?','We draft them for you to approve. Nothing goes out in your name until you sign off.'),
  ('Does this work for guests as well as hosts?','Yes. Guest booking is for founders and experts who want to appear on other people&rsquo;s shows.'),
  ('What do you need from me?','A link to your show or newsletter, who it is for, and the topics you can speak on or sell against.')],
 'Tell us about your show','Send a link to your podcast or newsletter and we will send a free sample of matches.',
 'Sponsor matching, guest pitching and media kits for podcasts and newsletters. 20 to 30% commission on sponsorship deals, or $1,000 to $2,500 per month for guest booking.')

# ---------- SHOPIFY
P['/shopify']=svc_page('shopify','For Shopify &amp; DTC brands',
 'Most stores lose sales in two places: the emails sent after a signup or an abandoned cart, and the product pages that carry the sale. We audit both and hand back copy you can paste straight in.',
 ul(['Shopify and direct-to-consumer brands that already collect emails','Founders who know their emails and product pages could work harder but lack the time']),
 '<p style="margin:0">Welcome emails read like templates, abandoned-cart reminders are easy to ignore, and product pages leave questions unanswered at the moment a shopper decides.</p>',
 [('Welcome email audit','A review of your welcome emails: timing, offer, tone and what the first message asks the reader to do.'),
  ('Abandoned-cart audit','A review of your cart reminders and how they bring the shopper back to checkout.'),
  ('Product page review','Notes on headlines, descriptions, proof and calls to action on your key pages.'),
  ('Paste-ready rewritten copy','New subject lines and email copy formatted so you can drop it into your email platform.'),
  ('Prioritized fix list','The changes most likely to matter first, so you know where to start.'),
  ('Monthly management','After setup, ongoing management of your flows if you want it.')],
 [('Send your store','Email your store link and forward your welcome and cart emails.'),('Free sample','We send a short teardown of one email so you can judge the depth.'),('Full teardown','The full audit and rewritten copy arrive by email.'),('You implement or we manage','Paste the copy in yourself, or add monthly management.')],
 price1('$300 <span style="font-size:1rem;font-weight:600;color:var(--mu);-webkit-text-fill-color:var(--mu)">setup</span>','<p style="margin:0">Plus monthly management.</p>',
  ul(['Setup covers the teardown and the rewritten copy.','Monthly management is optional and quoted separately.','The first sample is free.'])),
 '<p>An example store teardown showing how findings and rewritten copy are presented.</p>'+pdfs(('/samples/shopify-teardown-sample.pdf','Store teardown PDF')),
 [('Which email platform do you work with?','The copy is written to be pasted into whichever platform you use. Tell us which one when you write.'),
  ('Do you need access to my store?','To start, a store link and the emails you forward are enough. We will say what else we need as the work grows.'),
  ('Is monthly management required?','No. Setup stands alone, and monthly management is an optional add-on.'),
  ('What does the sample cover?','A short teardown of one of your emails, so you can judge the depth before you commit.')],
 'Send us your store','Send your store link and one email and we will return a free sample teardown.',
 'Email and product page teardowns for Shopify and DTC brands, with paste-ready rewritten copy. From $300 setup plus optional monthly management.')

# ---------- 404
P['404']=page('Page not found | Business Win Now','Page not found.','',
 '<section class="nf"><div class="w"><h1>Page not found</h1><p>That page does not exist. Try the <a href="/">home page</a> or pick a service above.</p><a class="btn" href="/">Back to home</a></div></section>')

os.makedirs('pages',exist_ok=True)
for k,v in P.items():
    open('pages/'+('home' if k=='/' else '404' if k=='404' else k[1:])+'.html','w').write(v)
open('index.html','w').write(P['/'])
print({k:len(v) for k,v in P.items()})
