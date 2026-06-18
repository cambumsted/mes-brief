"""Inject the FY26 Q3 partnership reporting inventory section into partnership-ideas.html.

Grouped: Region -> Line of Business -> Program initiative.
Columns shown: Partner/Activity, Initiative description, Markets (country).
Source: DDS RDS Opex Marketing Spend (Q3).
"""
import html as _html
import pathlib

PAGE = pathlib.Path(__file__).resolve().parent.parent / "partnership-ideas.html"

# (region, lob, activity, description, markets)
RECORDS = [
    # ---- EMEA ----
    ("EMEA", "Surface Consumer", "Amex", "Amex cashback (spend 500, get 100 back), AOV $1,500.", "UK, DE, FR, IT"),
    ("EMEA", "Surface Consumer", "Trade-In", "Trade-In top-up.", "UK, DE, FR, IT, ES"),
    ("EMEA", "Surface Consumer", "Partnership", "Extension of Paylead. 10% CPA on min $399 purchase, get up to 8.5% cashback from banking partners.", "FR, BE, ES"),
    ("EMEA", "Surface Consumer", "Partnership", "UNiDAYS relaunch and marketing package. BSKU & Laptop 13\" closed-loop offers.", "UK, FR, DE, IT"),
    ("EMEA", "Surface Consumer", "Partnership", "Extension of Student Beans partnership. 3% CPA on BSKU & Pro 12\" closed-loop offers.", "UK, DE, FR"),
    ("EMEA", "Surface Consumer", "Partnership", "XDL Promo Code Test (15% discount) \u2014 repurposed from 'I am Student' Spring BTS partnership.", "DE"),
    ("EMEA", "Surface Consumer", "Partnership", "ShowRoom Priv\u00e9: 45% saving on Refurbished Pro 11 BSKU (all SKUs) via vanity promocode.", "FR"),
    ("EMEA", "Surface Consumer", "Other", "Behind the Cart feature onboarding to scraping tool.", "UK, FR, DE"),
    ("EMEA", "Surface Commercial", "Trade-In", "Trade-In top-up.", "UK, DE, FR, IT, ES"),
    ("EMEA", "Gaming HW", "Trade-In", "Trade-In top-up.", "UK, DE, FR, IT, ES"),
    ("EMEA", "M365", "Partnership", "PayPal Cashback (get 15% cashback up to max \u20ac100).", "UK"),

    # ---- Americas ----
    ("Americas", "Surface Consumer, Surface Commercial", "Amex", "Marketing Partnership \u2013 AMEX: Spend $1,000, get $X back.", "US"),
    ("Americas", "Surface Consumer", "Mastercard", "Marketing Partnership \u2013 Mastercard: Get 15% back on purchases $1,000+.", "US"),
    ("Americas", "Surface Consumer", "Trade-In", "Trade-In Plus Up.", "US, CA"),
    ("Americas", "Surface Commercial", "Trade-In", "Trade-In Plus Up campaign.", "US, CA"),
    ("Americas", "Surface Commercial", "Trade-In", "Trade-In Plus Up: multiple assisted opportunities in play with customers that will exhaust current funding.", "US"),
    ("Americas", "Surface Consumer, Surface Commercial, Gaming HW", "Partnership", "Marketing Partnership \u2013 PayPal: Get 15% back on purchases, up to $175.", "US"),
    ("Americas", "Gaming HW", "Amex", "Marketing Partnership \u2013 AMEX: Spend $70 get $15 back; Spend $450 get $80 back.", "US"),
    ("Americas", "Gaming HW", "Trade-In", "Trade-In Plus Up campaign.", "US"),
    ("Americas", "M365", "Mastercard", "Marketing Partnership \u2013 Mastercard: Get 20% back on purchases of $99.99+.", "US"),

    # ---- Asia ----
    ("Asia", "Surface Consumer", "Amex", "Amex Cashback Campaign.", "ANZ, JPN, SKI"),
    ("Asia", "Surface Consumer", "Amex", "Q1 Amex campaign overspend cost.", "JPN"),
    ("Asia", "Surface Consumer", "Rakuten", "Rakuten Advertising Bronze.", "JPN"),
    ("Asia", "Surface Consumer", "Trade-In", "Trade-In Plus Up [ANZ \u2013 50K, SKI \u2013 15K].", "ANZ, SKI"),
    ("Asia", "Surface Consumer", "Visa/Mastercard", "Visa/Mastercard Co-marketing.", "ANZ"),
    ("Asia", "Surface Consumer", "Partnership", "UNiDAYS Co-marketing.", "ANZ"),
    ("Asia", "Surface Consumer", "Partnership", "Amazon Prime Day (Prime Day $30K / Rakuten $30K / Paid Media top-up $40K).", "JPN"),
    ("Asia", "Surface Consumer", "Alipay", "Alipay Co-marketing.", "GCR"),
    ("Asia", "Surface Commercial", "Amex", "Amex Cashback Campaign.", "ANZ, JPN, SKI"),
    ("Asia", "Surface Commercial", "Partnership", "*NEW* Partnership marketing with Intel.", "ANZ, JPN"),
    ("Asia", "Surface Commercial", "WeChat", "New pipeline acquisition through WeChat Ads.", "GCR"),
    ("Asia", "Surface Commercial", "Other", "Customize Brand Love gift to increase the un-assisted CVR.", "GCR"),
    ("Asia", "Surface Commercial", "Other", "12 stages free instalment.", "GCR"),
    ("Asia", "Surface Commercial", "Other", "Amex Co-marketing top-up due to outperformance while keeping strong ROI.", "AU"),
    ("Asia", "Gaming HW", "Alipay", "Alipay Co-marketing Pilot.", "GCR"),
    ("Asia", "Gaming HW", "Trade-In", "Trade-In Plus Up for 2TB.", "ANZ"),
    ("Asia", "Gaming HW", "Other", "3PP Gifts.", "GCR"),
    ("Asia", "Gaming HW", "Other", "PC Attach Co-marketing.", "GCR"),
    ("Asia", "Gaming HW", "Other", "Loyalty program: customize store membership.", "GCR"),
    ("Asia", "Gaming HW", "Other", "Top-up of Xbox Attach programme to drive additional $30K (1:4 ROI) in Gaming Accessories.", "CN"),
    ("Asia", "Surface Consumer", "Other", "3PP Gifts.", "GCR"),
    ("Asia", "Surface Consumer", "Alipay", "Alipay Co-marketing.", "GCR"),
    ("Asia", "Surface Consumer & Commercial", "Trade-In", "Q2 Trade-In Plus Up campaign overspend.", "AU"),
    ("Asia", "Cross LOB", "Amex", "Additional funding to support Amex campaign overperformance in Q3.", "JPN"),
]

REGION_ORDER = ["EMEA", "Americas", "Asia"]
LOB_ORDER = [
    "Surface Consumer",
    "Surface Commercial",
    "Gaming HW",
    "M365",
    "Surface Consumer, Surface Commercial",
    "Surface Consumer, Surface Commercial, Gaming HW",
    "Surface Consumer & Commercial",
    "Cross LOB",
]


def esc(s):
    return _html.escape(s, quote=True)


def lob_rank(lob):
    return LOB_ORDER.index(lob) if lob in LOB_ORDER else len(LOB_ORDER)


def build_section():
    out = []
    out.append('  <!-- ============================================ -->')
    out.append('  <!-- FY26 Q3 partnership reporting inventory       -->')
    out.append('  <!-- Source: DDS RDS Opex Marketing Spend (Q3)     -->')
    out.append('  <!-- ============================================ -->')
    out.append('  <section class="block" id="q3-inventory">')
    out.append('    <h2>Q3 partnership reporting inventory '
               '<span style="font-size:0.7rem;font-weight:500;color:var(--ink-soft);'
               'text-transform:uppercase;letter-spacing:1px;margin-left:0.4rem;">FY26 Q3 \u00b7 DDS/RDS Opex</span>'
               '<button type="button" class="section-toggle" aria-label="Collapse section" aria-expanded="true">'
               '<span class="chev">\u25be</span></button></h2>')
    out.append('    <p class="lede">Every FY26 Q3 partner-marketing initiative we are running, grouped by '
               'region \u2192 line of business \u2192 program. This is the working inventory we use to confirm '
               '<em>how each one is reported on</em> with the regional teams. Source: DDS\u00a0RDS\u00a0Opex Marketing Spend (Q3).</p>')

    total = len(RECORDS)
    for region in REGION_ORDER:
        region_recs = [r for r in RECORDS if r[0] == region]
        if not region_recs:
            continue
        out.append(f'    <h3 class="inv-region-title">{esc(region)} '
                   f'<span class="inv-count">{len(region_recs)} initiatives</span></h3>')

        lobs = sorted({r[1] for r in region_recs}, key=lob_rank)
        for lob in lobs:
            lob_recs = [r for r in region_recs if r[1] == lob]
            out.append('    <div class="inv-lob">')
            out.append(f'      <h4 class="inv-lob-title">{esc(lob)}</h4>')
            out.append('      <div class="grid-wrap">')
            out.append('      <table class="inv-table">')
            out.append('        <thead><tr><th>Partner / activity</th><th>Initiative</th><th>Markets</th></tr></thead>')
            out.append('        <tbody>')
            for _, _, activity, desc, markets in lob_recs:
                out.append('          <tr>'
                           f'<td><span class="inv-tag">{esc(activity)}</span></td>'
                           f'<td>{esc(desc)}</td>'
                           f'<td>{esc(markets)}</td></tr>')
            out.append('        </tbody>')
            out.append('      </table>')
            out.append('      </div>')
            out.append('    </div>')

    out.append(f'    <p class="footer-note" style="margin-top:1.25rem;">{total} initiatives total across '
               'EMEA, Americas and Asia. Reporting source/cadence to be confirmed per initiative with regional teams.</p>')
    out.append('  </section>')
    out.append('')
    return "\n".join(out)


CSS = """
  /* Q3 partnership reporting inventory */
  .inv-region-title {
    font-size: 1.15rem;
    margin: 1.6rem 0 0.8rem;
    padding-bottom: 0.35rem;
    border-bottom: 2px solid var(--ms-blue);
    color: var(--ms-blue-dark);
  }
  .inv-region-title .inv-count {
    font-size: 0.72rem; font-weight: 500; color: var(--ink-soft);
    text-transform: uppercase; letter-spacing: 1px; margin-left: 0.4rem;
  }
  .inv-lob { margin: 0 0 1.4rem; }
  .inv-lob-title {
    display: inline-block;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px;
    color: var(--ms-blue-dark); background: var(--ms-blue-light);
    padding: 0.3rem 0.6rem; border-radius: 4px; margin: 0 0 0.5rem;
  }
  table.inv-table {
    width: 100%; border-collapse: collapse;
    font-size: 0.86rem; min-width: 640px;
  }
  table.inv-table th, table.inv-table td {
    padding: 0.5rem 0.7rem;
    border-bottom: 1px solid var(--line);
    text-align: left; vertical-align: top;
  }
  table.inv-table thead th {
    background: var(--bg); color: var(--ink-soft);
    font-size: 0.72rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.5px;
  }
  table.inv-table td:last-child {
    white-space: nowrap; color: var(--ink-soft);
    font-weight: 600; font-size: 0.8rem;
  }
  table.inv-table tbody tr:hover { background: var(--bg); }
  .inv-tag {
    display: inline-block;
    background: var(--c-aqua); color: var(--c-dark-blue);
    font-size: 0.68rem; font-weight: 600;
    padding: 0.12rem 0.5rem; border-radius: 10px; white-space: nowrap;
  }
"""


def main():
    text = PAGE.read_text(encoding="utf-8")

    # 1) inject CSS before </style>
    if ".inv-region-title" not in text:
        text = text.replace("</style>", CSS + "</style>", 1)

    # 2) add page-nav link after the amex-grid nav link
    nav_anchor = '  <a href="#amex-grid">AMEX FY26 Q2 grid</a>'
    if "#q3-inventory" not in text:
        text = text.replace(
            nav_anchor,
            nav_anchor + '\n  <a href="#q3-inventory">Q3 inventory</a>',
            1,
        )

    # 3) inject the section before the closing footer-note paragraph
    marker = '  <p class="footer-note">This is a working scratch-pad.'
    if 'id="q3-inventory"' not in text:
        section = build_section()
        text = text.replace(marker, section + "\n" + marker, 1)

    PAGE.write_text(text, encoding="utf-8")
    print(f"Injected Q3 inventory: {len(RECORDS)} records.")


if __name__ == "__main__":
    main()
