"""Inject the FY26 Q3 partnership reporting inventory section into partnership-ideas.html.

Grouped: Region -> Line of Business -> Program initiative.
Columns shown: Partner/Activity, Initiative description, Markets (country).
Source: DDS RDS Opex Marketing Spend (Q3).
"""
import html as _html
import pathlib

PAGE = pathlib.Path(__file__).resolve().parent.parent / "partnership-ideas.html"

# (region, lob, partner, description, markets) — partner = source "Activity" column
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

    total = len(RECORDS)

    # Filter controls
    regions = [r for r in REGION_ORDER if any(rec[0] == r for rec in RECORDS)]
    lobs = sorted({rec[1] for rec in RECORDS}, key=lob_rank)
    partners = sorted({rec[2] for rec in RECORDS}, key=str.lower)

    out.append('    <div class="inv-filters">')
    out.append('      <label class="inv-filter">Region'
               '<select id="filt-region"><option value="">All regions</option>'
               + ''.join(f'<option value="{esc(r)}">{esc(r)}</option>' for r in regions)
               + '</select></label>')
    out.append('      <label class="inv-filter">Line of business'
               '<select id="filt-lob"><option value="">All LOBs</option>'
               + ''.join(f'<option value="{esc(l)}">{esc(l)}</option>' for l in lobs)
               + '</select></label>')
    out.append('      <label class="inv-filter">Partnership'
               '<select id="filt-partner"><option value="">All partnerships</option>'
               + ''.join(f'<option value="{esc(p)}">{esc(p)}</option>' for p in partners)
               + '</select></label>')
    out.append('      <button type="button" id="filt-reset" class="inv-reset">Reset</button>')
    out.append('      <span class="inv-result-count"></span>')
    out.append('    </div>')

    # Single flat table
    out.append('    <div class="grid-wrap">')
    out.append('    <table class="inv-table" id="q3-table">')
    out.append('      <thead><tr>'
               '<th>Region</th><th>Line of business</th><th>Partnership</th>'
               '<th>Initiative</th><th>Markets</th>'
               '</tr></thead>')
    out.append('      <tbody>')
    ordered = sorted(
        RECORDS,
        key=lambda rec: (REGION_ORDER.index(rec[0]) if rec[0] in REGION_ORDER else 99,
                         lob_rank(rec[1])),
    )
    for region, lob, partner, desc, markets in ordered:
        out.append('        <tr '
                   f'data-region="{esc(region)}" data-lob="{esc(lob)}" data-partner="{esc(partner)}">'
                   f'<td class="inv-region-cell">{esc(region)}</td>'
                   f'<td class="inv-lob-cell">{esc(lob)}</td>'
                   f'<td><span class="inv-tag">{esc(partner)}</span></td>'
                   f'<td>{esc(desc)}</td>'
                   f'<td>{esc(markets)}</td></tr>')
    out.append('      </tbody>')
    out.append('    </table>')
    out.append('    </div>')

    out.append(f'    <p class="footer-note" style="margin-top:1.25rem;">{total} initiatives total across '
               'EMEA, Americas and Asia. Reporting source/cadence to be confirmed per initiative with regional teams.</p>')

    # Filter behaviour
    out.append('    <script>')
    out.append('    (function () {')
    out.append('      var sec = document.getElementById("q3-inventory");')
    out.append('      if (!sec) return;')
    out.append('      var rows = Array.prototype.slice.call(sec.querySelectorAll("#q3-table tbody tr"));')
    out.append('      var fR = sec.querySelector("#filt-region");')
    out.append('      var fL = sec.querySelector("#filt-lob");')
    out.append('      var fP = sec.querySelector("#filt-partner");')
    out.append('      var count = sec.querySelector(".inv-result-count");')
    out.append('      function apply() {')
    out.append('        var r = fR.value, l = fL.value, p = fP.value, n = 0;')
    out.append('        rows.forEach(function (tr) {')
    out.append('          var ok = (!r || tr.dataset.region === r)')
    out.append('                && (!l || tr.dataset.lob === l)')
    out.append('                && (!p || tr.dataset.partner === p);')
    out.append('          tr.style.display = ok ? "" : "none";')
    out.append('          if (ok) n++;')
    out.append('        });')
    out.append('        count.textContent = n + " of " + rows.length + " initiatives";')
    out.append('      }')
    out.append('      [fR, fL, fP].forEach(function (s) { s.addEventListener("change", apply); });')
    out.append('      sec.querySelector("#filt-reset").addEventListener("click", function () {')
    out.append('        fR.value = ""; fL.value = ""; fP.value = ""; apply();')
    out.append('      });')
    out.append('      apply();')
    out.append('    })();')
    out.append('    </script>')

    out.append('  </section>')
    out.append('')
    return "\n".join(out)


CSS = """
  /* Q3 partnership reporting inventory */
  .inv-filters {
    display: flex; flex-wrap: wrap; align-items: flex-end; gap: 0.9rem;
    margin: 0 0 1.1rem;
  }
  .inv-filter {
    display: flex; flex-direction: column; gap: 0.25rem;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.5px;
    color: var(--ink-soft); font-weight: 600;
  }
  .inv-filter select {
    font-family: inherit; font-size: 0.85rem; font-weight: 400;
    text-transform: none; letter-spacing: 0;
    color: var(--ink); background: var(--c-white);
    border: 1px solid var(--line); border-radius: 6px;
    padding: 0.4rem 0.6rem; min-width: 180px; cursor: pointer;
  }
  .inv-filter select:focus { outline: 2px solid var(--ms-blue); outline-offset: 1px; }
  .inv-reset {
    font-family: inherit; font-size: 0.8rem; font-weight: 600;
    color: var(--ms-blue-dark); background: var(--ms-blue-light);
    border: 1px solid var(--line); border-radius: 6px;
    padding: 0.45rem 0.9rem; cursor: pointer;
  }
  .inv-reset:hover { background: var(--c-aqua); }
  .inv-result-count {
    font-size: 0.78rem; color: var(--ink-soft); font-weight: 600;
    margin-left: auto; align-self: center;
  }
  table.inv-table {
    width: 100%; border-collapse: collapse;
    font-size: 0.86rem; min-width: 820px;
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
    position: sticky; top: 0;
  }
  table.inv-table td.inv-region-cell { font-weight: 600; color: var(--ms-blue-dark); white-space: nowrap; }
  table.inv-table td.inv-lob-cell { color: var(--ink); white-space: nowrap; }
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

    # 1) inject or replace CSS (block runs from its start comment to </style>)
    css_start = "\n  /* Q3 partnership reporting inventory */"
    if css_start in text:
        s = text.index(css_start)
        e = text.index("</style>", s)
        text = text[:s] + CSS + text[e:]
    else:
        text = text.replace("</style>", CSS + "</style>", 1)

    # 2) add page-nav link after the amex-grid nav link
    nav_anchor = '  <a href="#amex-grid">AMEX FY26 Q2 grid</a>'
    if "#q3-inventory" not in text:
        text = text.replace(
            nav_anchor,
            nav_anchor + '\n  <a href="#q3-inventory">Q3 inventory</a>',
            1,
        )

    # 3) inject (or replace) the section before the closing footer-note paragraph
    marker = '  <p class="footer-note">This is a working scratch-pad.'
    section = build_section()
    start = '  <!-- ============================================ -->\n  <!-- FY26 Q3 partnership reporting inventory'
    if 'id="q3-inventory"' in text:
        # remove the existing generated section and re-inject
        s_idx = text.index(start)
        e_idx = text.index(marker, s_idx)
        text = text[:s_idx] + section + "\n" + text[e_idx:]
    else:
        text = text.replace(marker, section + "\n" + marker, 1)

    PAGE.write_text(text, encoding="utf-8")
    print(f"Injected Q3 inventory: {len(RECORDS)} records.")


if __name__ == "__main__":
    main()
