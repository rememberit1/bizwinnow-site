import html, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
C="confirm in solicitation"
R=[
("ADM-01","E.2.1.a","Submit signed, dated quote by email to CO Tyrone Whalen (tyrone.whalen@va.gov); copy Danielle Carrico per Amendment 0001 Q&A","Cover email","Capture lead","Open","~10 MB/email limit; may split across emails"),
("ADM-02","SAM.gov notice / Amd 0001","Quote due Nov 3, 2026, 5:00 PM Pacific (8:00 PM ET)","Cover email","Capture lead","Open","Amendment 0001 extended deadline from 10/13/2026"),
("ADM-03","E.2.1.b","Submit Parts I-III (required) as separate attachments; Part IV if past performance available","Submission package","Proposal mgr","Open","Formats/naming at contractor discretion (Amd 0001)"),
("ADM-04","SF1449 Blk 10 / Notice","100% SDVOSB set-aside; NAICS 541519","Part I","Contracts","Open","Verify SBA VetCert status; "+C),
("P1-01","E.2.b.i","Complete SF1449 incl. Block 17a (SAM UEI) and Blocks 30a-c","Part I","Contracts","Open",""),
("P1-02","E.2.b.i / B.1","Acknowledge all amendments (incl. Amendment 0001)","Part I","Contracts","Open",""),
("P1-03","E.2.b.i / VAAR 852.219-75","Complete VA Notice of Limitations on Subcontracting certificate","Part I","Contracts","Open","Offers without it not considered"),
("P2-01","E.2.b.ii / B.3","Unit and extended prices for CLINs 0001-4001, two decimals, calculations correct","Part II","Pricing","Open","Options added to total for evaluation (E.4(b))"),
("P2-02","SOW travel / Amd 0001","Include all travel and training costs in FFP line items; do not price optional modules/added licenses","Part II","Pricing","Open","Travel not separately reimbursed"),
("P3-01","E.2.b.iii Q1","Fully operational COTS SaaS at award, no customization","Part III Q1","Tech lead","Open",""),
("P3-02","E.2.b.iii Q2 / Tech Reqs","FedRAMP-compliant, FedRAMP ID, hosted on FedRAMP-approved infrastructure","Part III Q2","Tech lead","Open","Ready/In-Process acceptability not stated; "+C),
("P3-03","E.2.b.iii Q3 / Tech Reqs","Meets NIST 800-145 (SaaS) and NIST 800-53 Rev.3","Part III Q3","Security","Open",""),
("P3-04","Tech Reqs","Registered in eMASS with current, approved VA ATO","Part III Q2-Q3","Security","Open","ATO timing not specified; "+C),
("P3-05","E.2.b.iii Q4","Multi-factor and replay-resistant authentication","Part III Q4","Security","Open",""),
("P3-06","E.2.b.iii Q5","Data encrypted in transit and at rest","Part III Q5","Security","Open",""),
("P3-07","E.2.b.iii Q6","Track loads, tonnage, deficiencies, labor types/costs, usage, assets (asset/part nos., manufacturer, model, location)","Part III Q6","Tech lead","Open",""),
("P3-08","E.2.b.iii Q7","Configurable standard audit reports and ad-hoc user reports","Part III Q7","Tech lead","Open",""),
("P3-09","E.2.b.iii Q8","Dashboards for performance metrics; historical data, analytics, trending","Part III Q8","Tech lead","Open",""),
("P3-10","E.2.b.iii Q9 / SOW 17","Multi-level access (national/regional/local) with accurate role/permission mapping","Part III Q9","Tech lead","Open","Be ready to demonstrate"),
("P3-11","E.2.b.iii Q10 / SOW 13","On-site and web-based training before go-live; classroom instruction with proficiency evaluation","Part III Q10","Training lead","Open",""),
("SOW-01","SOW 17.4","Single-tenant deployment; ability to run on virtual server on Government network","Part III Q2","Tech lead","Open","See Amd 0001 Q&A"),
("SOW-02","SOW 10.1","Licenses for 10 initial users; unlimited site licenses for Government-defined facilities","Part III / Part II","Pricing","Open","User count (10 vs ~20) - "+C),
("SOW-03","SOW Tier II","Tier II help desk via phone/email/chat, M-F 8 AM-6 PM Pacific","Part III","Support lead","Open","Delays >2 business days noted in past performance"),
("SOW-04","SOW 6.1","System testing and acceptance plan within 5 days of award (3 phases)","Part III","PM","Open",""),
("SOW-05","SOW Kickoff","Technical kickoff meeting within 10 days of award","Part III","PM","Open",""),
("SOW-06","SOW data migration","Load up to 2 years of existing EMS records","Part III","Tech lead","Open",""),
("SOW-07","SOW Emergency Ops","Disaster recovery, failover and backups; RTO/RPO set with VA POC","Part III","Security","Open",""),
("SOW-08","SOW reporting","Progress/deliverable reports in Microsoft Word format","Part III","PM","Open",""),
("P4-01","E.2.b.iv","Past performance (last 5 yrs): entity/address, services and scale, reference POC, dates, contract type and value","Part IV","Capture lead","Open","Users/sites may replace sq. ft.; CPARS accepted (Amd 0001)"),
("EVAL-01","E.4 (52.212-2)","Best value: Technical, Past Performance, Price; no alternate quotes","All parts","Proposal mgr","Info","Relative weights not stated - "+C),
("INS-01","Insurance clause","Evidence of general liability insurance before award","Pre-award","Contracts","Open",C+" for limits"),
]
H=["Req ID","Section ref","Requirement","Response location","Owner","Status","Notes"]
wb=openpyxl.Workbook();ws=wb.active;ws.title="Compliance Matrix"
ws.append(["Business Win Now - SAMPLE Compliance Matrix - VA RFQ 36C26026Q1017 (Portland VA EMS SaaS)"]);ws["A1"].font=Font(bold=True,size=13,color="0B2545")
ws.append(["Source: RFQ revised 10-13-2026 + Amendment 0001 (SAM.gov). Sample only; verify against the current solicitation."])
ws.append(H)
for c in ws[3]: c.font=Font(bold=True,color="FFFFFF");c.fill=PatternFill("solid",fgColor="0B2545")
for r in R: ws.append(list(r))
for i,w in enumerate([10,22,60,18,14,9,45]): ws.column_dimensions["ABCDEFG"[i]].width=w
for row in ws.iter_rows(min_row=4):
  for c in row: c.alignment=Alignment(wrap_text=True,vertical="top")
ws.freeze_panes="A4"
wb.save("sample-compliance-matrix.xlsx")
rows="".join("<tr>"+"".join(f"<td>{html.escape(x)}</td>" for x in r)+"</tr>" for r in R)
open("matrix.html","w").write(f"""<html><head><meta charset=utf-8><style>
@page{{size:letter landscape;margin:.5in}}body{{font-family:Helvetica,Arial;font-size:9pt;color:#1a1a1a}}
.h{{border-bottom:3px solid #c9a227;padding-bottom:6px;margin-bottom:8px}}.b{{color:#0b2545;font-size:18pt;font-weight:bold}}
table{{border-collapse:collapse;width:100%}}th{{background:#0b2545;color:#fff;text-align:left;padding:5px}}td{{border:1px solid #ccd;padding:4px;vertical-align:top}}tr:nth-child(even) td{{background:#f4f6fa}}
.n{{font-size:8pt;color:#555;margin-top:8px}}</style></head><body>
<div class=h><span class=b>Business Win Now</span> &nbsp; Proposal support for small federal contractors<br>
<b>SAMPLE Compliance Matrix — VA RFQ 36C26026Q1017</b> · Portland VA, EMS Quality Assurance Inspection SaaS · SDVOSB set-aside · NAICS 541519 · Quotes due Nov 3, 2026, 5:00 PM PT (8:00 PM ET)</div>
<table><tr>{''.join(f'<th>{h}</th>' for h in H)}</tr>{rows}</table>
<p class=n>Built from the public RFQ (revised 10-13-2026) and Amendment 0001 posted on SAM.gov. This is a sample for illustration, not legal or contracting advice; items marked "confirm in solicitation" need verification. Owner/Status columns are placeholders for the bidding team. Contact: businesswinnow@gmail.com</p></body></html>""")
