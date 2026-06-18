"""Inject the FY26 Q3 partnership reporting inventory section into partnership-ideas.html.

Grouped: Region -> Line of Business -> Program initiative.
Columns shown: Partner/Activity, Initiative description, Markets (country).
Source: DDS RDS Opex Marketing Spend (Q3).
"""
import html as _html
import pathlib

PAGE = pathlib.Path(__file__).resolve().parent.parent / "partnership-ideas.html"

# (region, lob, partner, description, markets, budget) — partner = source "Activity" column, budget = Funding Ask (USD)
RECORDS = [
    # ---- EMEA ----
    ("EMEA", "Surface Consumer", "Amex", "Amex cashback (spend 500, get 100 back), AOV $1,500.", "UK, DE, FR, IT", 125000),
    ("EMEA", "Surface Consumer", "Trade-In", "Trade-In top-up.", "UK, DE, FR, IT, ES", 55000),
    ("EMEA", "Surface Consumer", "Paylead", "Extension of Paylead. 10% CPA on min $399 purchase, get up to 8.5% cashback from banking partners.", "FR, BE, ES", 9800),
    ("EMEA", "Surface Consumer", "UNiDAYS", "UNiDAYS relaunch and marketing package. BSKU & Laptop 13\" closed-loop offers.", "UK, FR, DE, IT", 30000),
    ("EMEA", "Surface Consumer", "Student Beans", "Extension of Student Beans partnership. 3% CPA on BSKU & Pro 12\" closed-loop offers.", "UK, DE, FR", 15000),
    ("EMEA", "Surface Consumer", "XDL", "XDL Promo Code Test (15% discount) \u2014 repurposed from 'I am Student' Spring BTS partnership.", "DE", 10000),
    ("EMEA", "Surface Consumer", "ShowRoom Priv\u00e9", "ShowRoom Priv\u00e9: 45% saving on Refurbished Pro 11 BSKU (all SKUs) via vanity promocode.", "FR", 11500),
    ("EMEA", "Surface Consumer", "Other", "Behind the Cart feature onboarding to scraping tool.", "UK, FR, DE", 2700),
    ("EMEA", "Surface Commercial", "Trade-In", "Trade-In top-up.", "UK, DE, FR, IT, ES", 15000),
    ("EMEA", "Gaming HW", "Trade-In", "Trade-In top-up.", "UK, DE, FR, IT, ES", 5000),
    ("EMEA", "M365", "PayPal", "PayPal Cashback (get 15% cashback up to max \u20ac100).", "UK", 40000),

    # ---- Americas ----
    ("Americas", "Surface Consumer, Surface Commercial", "Amex", "Marketing Partnership \u2013 AMEX: Spend $1,000, get $X back.", "US", 50000),
    ("Americas", "Surface Consumer", "Mastercard", "Marketing Partnership \u2013 Mastercard: Get 15% back on purchases $1,000+.", "US", 30000),
    ("Americas", "Surface Consumer", "Trade-In", "Trade-In Plus Up.", "US, CA", 50000),
    ("Americas", "Surface Commercial", "Trade-In", "Trade-In Plus Up campaign.", "US, CA", 15000),
    ("Americas", "Surface Commercial", "Trade-In", "Trade-In Plus Up: multiple assisted opportunities in play with customers that will exhaust current funding.", "US", 30000),
    ("Americas", "Surface Consumer, Surface Commercial, Gaming HW", "PayPal", "Marketing Partnership \u2013 PayPal: Get 15% back on purchases, up to $175.", "US", 25000),
    ("Americas", "Gaming HW", "Amex", "Marketing Partnership \u2013 AMEX: Spend $70 get $15 back; Spend $450 get $80 back.", "US", 20000),
    ("Americas", "Gaming HW", "Trade-In", "Trade-In Plus Up campaign.", "US", 10000),
    ("Americas", "M365", "Mastercard", "Marketing Partnership \u2013 Mastercard: Get 20% back on purchases of $99.99+.", "US", 20000),

    # ---- Asia ----
    ("Asia", "Surface Consumer", "Amex", "Amex Cashback Campaign.", "ANZ, JPN, SKI", 130000),
    ("Asia", "Surface Consumer", "Amex", "Q1 Amex campaign overspend cost.", "JPN", 36000),
    ("Asia", "Surface Consumer", "Rakuten", "Rakuten Advertising Bronze.", "JPN", 100000),
    ("Asia", "Surface Consumer", "Trade-In", "Trade-In Plus Up [ANZ \u2013 50K, SKI \u2013 15K].", "ANZ, SKI", 55000),
    ("Asia", "Surface Consumer", "Visa/Mastercard", "Visa/Mastercard Co-marketing.", "ANZ", 50000),
    ("Asia", "Surface Consumer", "UNiDAYS", "UNiDAYS Co-marketing.", "ANZ", 20000),
    ("Asia", "Surface Consumer", "Amazon / Rakuten", "Amazon Prime Day (Prime Day $30K / Rakuten $30K / Paid Media top-up $40K).", "JPN", 100000),
    ("Asia", "Surface Consumer", "Alipay", "Alipay Co-marketing.", "GCR", 100000),
    ("Asia", "Surface Commercial", "Amex", "Amex Cashback Campaign.", "ANZ, JPN, SKI", 50000),
    ("Asia", "Surface Commercial", "Intel", "*NEW* Partnership marketing with Intel.", "ANZ, JPN", 50000),
    ("Asia", "Surface Commercial", "WeChat", "New pipeline acquisition through WeChat Ads.", "GCR", 20000),
    ("Asia", "Surface Commercial", "Other", "Customize Brand Love gift to increase the un-assisted CVR.", "GCR", 10000),
    ("Asia", "Surface Commercial", "Other", "12 stages free instalment.", "GCR", 5000),
    ("Asia", "Surface Commercial", "Other", "Amex Co-marketing top-up due to outperformance while keeping strong ROI.", "AU", 20000),
    ("Asia", "Gaming HW", "Alipay", "Alipay Co-marketing Pilot.", "GCR", 15000),
    ("Asia", "Gaming HW", "Trade-In", "Trade-In Plus Up for 2TB.", "ANZ", 10000),
    ("Asia", "Gaming HW", "Other", "3PP Gifts.", "GCR", 10000),
    ("Asia", "Gaming HW", "Other", "PC Attach Co-marketing.", "GCR", 25000),
    ("Asia", "Gaming HW", "Other", "Loyalty program: customize store membership.", "GCR", 10000),
    ("Asia", "Gaming HW", "Other", "Top-up of Xbox Attach programme to drive additional $30K (1:4 ROI) in Gaming Accessories.", "CN", 7000),
    ("Asia", "Surface Consumer", "Other", "3PP Gifts.", "GCR", 30000),
    ("Asia", "Surface Consumer", "Alipay", "Alipay Co-marketing.", "GCR", 30000),
    ("Asia", "Surface Consumer", "Trade-In", "Q2 Trade-In Plus Up campaign overspend.", "AU", 13000),
    ("Asia", "Cross LOB", "Amex", "Additional funding to support Amex campaign overperformance in Q3.", "JPN", 53000),
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
    grand_total = sum(rec[5] for rec in RECORDS)

    # Filter controls
    regions = [r for r in REGION_ORDER if any(rec[0] == r for rec in RECORDS)]
    lobs = sorted({rec[1] for rec in RECORDS}, key=lob_rank)
    partners = sorted({rec[2] for rec in RECORDS}, key=str.lower)

    def multiselect(fid, label, all_label, values):
        opts = ''.join(
            f'<label class="inv-ms-opt"><input type="checkbox" value="{esc(v)}">'
            f'<span>{esc(v)}</span></label>'
            for v in values
        )
        return (
            f'      <div class="inv-filter inv-ms" data-filter="{fid}">'
            f'<span class="inv-ms-label">{esc(label)}</span>'
            f'<button type="button" class="inv-ms-toggle" aria-expanded="false">'
            f'<span class="inv-ms-text">{esc(all_label)}</span><span class="inv-ms-chev">\u25be</span></button>'
            f'<div class="inv-ms-panel" hidden>{opts}</div>'
            f'</div>'
        )

    out.append('    <div class="inv-filters">')
    out.append(multiselect('region', 'Region', 'All regions', regions))
    out.append(multiselect('lob', 'Line of business', 'All LOBs', lobs))
    out.append(multiselect('partner', 'Partnership', 'All partnerships', partners))
    out.append('      <button type="button" id="filt-reset" class="inv-reset">Reset</button>')
    out.append('      <span class="inv-result-count"></span>')
    out.append('    </div>')

    # Single flat table
    out.append('    <div class="grid-wrap">')
    out.append('    <table class="inv-table" id="q3-table">')
    out.append('      <thead><tr>'
               '<th>Region</th><th>Line of business</th><th>Partnership</th>'
               '<th>Initiative</th><th>Markets</th><th class="inv-budget-col">Budget</th>'
               '</tr></thead>')
    out.append('      <tbody>')
    ordered = sorted(
        RECORDS,
        key=lambda rec: (REGION_ORDER.index(rec[0]) if rec[0] in REGION_ORDER else 99,
                         lob_rank(rec[1])),
    )
    for region, lob, partner, desc, markets, budget in ordered:
        out.append('        <tr '
                   f'data-region="{esc(region)}" data-lob="{esc(lob)}" data-partner="{esc(partner)}" '
                   f'data-budget="{budget}">'
                   f'<td class="inv-region-cell">{esc(region)}</td>'
                   f'<td class="inv-lob-cell">{esc(lob)}</td>'
                   f'<td><span class="inv-tag">{esc(partner)}</span></td>'
                   f'<td>{esc(desc)}</td>'
                   f'<td>{esc(markets)}</td>'
                   f'<td class="inv-budget-col">${budget:,}</td></tr>')
    out.append('      </tbody>')
    out.append('    </table>')
    out.append('    </div>')

    out.append(f'    <p class="footer-note" style="margin-top:1.25rem;">{total} initiatives total across '
               f'EMEA, Americas and Asia \u00b7 ${grand_total:,} combined budget. '
               'Reporting source/cadence to be confirmed per initiative with regional teams.</p>')

    # Filter behaviour
    out.append('    <script>')
    out.append('    (function () {')
    out.append('      var sec = document.getElementById("q3-inventory");')
    out.append('      if (!sec) return;')
    out.append('      var rows = Array.prototype.slice.call(sec.querySelectorAll("#q3-table tbody tr"));')
    out.append('      var widgets = Array.prototype.slice.call(sec.querySelectorAll(".inv-ms"));')
    out.append('      var count = sec.querySelector(".inv-result-count");')
    out.append('      function selected(w) {')
    out.append('        return Array.prototype.slice.call(w.querySelectorAll("input:checked")).map(function (c) { return c.value; });')
    out.append('      }')
    out.append('      function syncLabel(w) {')
    out.append('        var sel = selected(w);')
    out.append('        var txt = w.querySelector(".inv-ms-text");')
    out.append('        var all = w.querySelector(".inv-ms-toggle").getAttribute("data-all") || txt.textContent;')
    out.append('        w.querySelector(".inv-ms-toggle").setAttribute("data-all", all);')
    out.append('        if (sel.length === 0) { txt.textContent = all; w.classList.remove("has-sel"); }')
    out.append('        else if (sel.length === 1) { txt.textContent = sel[0]; w.classList.add("has-sel"); }')
    out.append('        else { txt.textContent = sel.length + " selected"; w.classList.add("has-sel"); }')
    out.append('      }')
    out.append('      function apply() {')
    out.append('        var sel = {};')
    out.append('        widgets.forEach(function (w) { sel[w.dataset.filter] = selected(w); });')
    out.append('        var n = 0, sum = 0;')
    out.append('        rows.forEach(function (tr) {')
    out.append('          var ok = (!sel.region.length  || sel.region.indexOf(tr.dataset.region) > -1)')
    out.append('                && (!sel.lob.length     || sel.lob.indexOf(tr.dataset.lob) > -1)')
    out.append('                && (!sel.partner.length || sel.partner.indexOf(tr.dataset.partner) > -1);')
    out.append('          tr.style.display = ok ? "" : "none";')
    out.append('          if (ok) { n++; sum += parseInt(tr.dataset.budget, 10) || 0; }')
    out.append('        });')
    out.append('        count.textContent = n + " of " + rows.length + " initiatives \u00b7 $" + sum.toLocaleString() + " budget";')
    out.append('      }')
    out.append('      widgets.forEach(function (w) {')
    out.append('        var toggle = w.querySelector(".inv-ms-toggle");')
    out.append('        var panel = w.querySelector(".inv-ms-panel");')
    out.append('        toggle.addEventListener("click", function (e) {')
    out.append('          e.stopPropagation();')
    out.append('          var open = !panel.hidden;')
    out.append('          widgets.forEach(function (o) { o.querySelector(".inv-ms-panel").hidden = true; o.querySelector(".inv-ms-toggle").setAttribute("aria-expanded", "false"); });')
    out.append('          panel.hidden = open;')
    out.append('          toggle.setAttribute("aria-expanded", open ? "false" : "true");')
    out.append('        });')
    out.append('        panel.addEventListener("click", function (e) { e.stopPropagation(); });')
    out.append('        w.querySelectorAll("input").forEach(function (c) {')
    out.append('          c.addEventListener("change", function () { syncLabel(w); apply(); });')
    out.append('        });')
    out.append('      });')
    out.append('      document.addEventListener("click", function () {')
    out.append('        widgets.forEach(function (o) { o.querySelector(".inv-ms-panel").hidden = true; o.querySelector(".inv-ms-toggle").setAttribute("aria-expanded", "false"); });')
    out.append('      });')
    out.append('      sec.querySelector("#filt-reset").addEventListener("click", function () {')
    out.append('        widgets.forEach(function (w) {')
    out.append('          w.querySelectorAll("input:checked").forEach(function (c) { c.checked = false; });')
    out.append('          syncLabel(w);')
    out.append('        });')
    out.append('        apply();')
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
  .inv-ms { position: relative; }
  .inv-ms-label {
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.5px;
    color: var(--ink-soft); font-weight: 600;
  }
  .inv-ms-toggle {
    font-family: inherit; font-size: 0.85rem; font-weight: 400;
    text-transform: none; letter-spacing: 0;
    color: var(--ink); background: var(--c-white);
    border: 1px solid var(--line); border-radius: 6px;
    padding: 0.4rem 0.6rem; min-width: 200px; cursor: pointer;
    display: flex; align-items: center; justify-content: space-between; gap: 0.5rem;
  }
  .inv-ms-toggle:focus { outline: 2px solid var(--ms-blue); outline-offset: 1px; }
  .inv-ms.has-sel .inv-ms-toggle {
    border-color: var(--ms-blue); color: var(--ms-blue-dark); font-weight: 600;
  }
  .inv-ms-text { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .inv-ms-chev { color: var(--ink-soft); flex-shrink: 0; font-size: 0.7rem; }
  .inv-ms-panel {
    position: absolute; top: calc(100% + 4px); left: 0; z-index: 50;
    min-width: 100%; max-width: 320px; max-height: 280px; overflow-y: auto;
    background: var(--c-white); border: 1px solid var(--line); border-radius: 6px;
    box-shadow: var(--shadow); padding: 0.35rem;
  }
  .inv-ms-opt {
    display: flex; align-items: center; gap: 0.5rem;
    padding: 0.35rem 0.5rem; border-radius: 4px; cursor: pointer;
    font-size: 0.85rem; font-weight: 400; text-transform: none; letter-spacing: 0;
    color: var(--ink); white-space: nowrap;
  }
  .inv-ms-opt:hover { background: var(--ms-blue-light); }
  .inv-ms-opt input { cursor: pointer; accent-color: var(--ms-blue); margin: 0; }
  .inv-reset {
    font-family: inherit; font-size: 0.8rem; font-weight: 600;
    color: var(--ms-blue-dark); background: var(--ms-blue-light);
    border: 1px solid var(--line); border-radius: 6px;
    padding: 0.45rem 0.9rem; cursor: pointer; align-self: flex-end;
  }
  .inv-reset:hover { background: var(--c-aqua); }
  .inv-result-count {
    font-size: 0.78rem; color: var(--ink-soft); font-weight: 600;
    margin-left: auto; align-self: center;
  }
  table.inv-table {
    width: 100%; border-collapse: collapse;
    font-size: 0.86rem; min-width: 900px;
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
  table.inv-table th.inv-budget-col { text-align: left; }
  table.inv-table td.inv-budget-col {
    white-space: nowrap;
    font-variant-numeric: tabular-nums;
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
