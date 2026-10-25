#!/usr/bin/env python3
"""Vishavabhartiya Foundation website — static page builder (v2, English + Hindi).

HOW TO UPDATE
  • Final domain:        change CONFIG["site_url"] below, then run:  python3 build.py
  • Official emails:     fill CONFIG["emails"] (info / csr / donations) once the mailboxes WORK, then run build.py
  • Online form saving:  put your Google Apps Script / form-service URL in CONFIG["forms"]["endpoint"] (see backend/README.md)
  • Activities, news, photos, awards: edit assets/js/data.js only (no rebuild needed)
Build writes: *.html (English), hi/*.html (Hindi), assets/js/config.js, assets/js/img-sizes.js, sitemap.xml, robots.txt
"""
import json, os, glob
from PIL import Image

# ======================================================================= CENTRAL CONFIGURATION
CONFIG = {
    "site_url": "https://helpinghandshub16-alt.github.io/vishavabhartiya-foundation-website",   # TODO(owner): replace with final domain, e.g. https://www.<your-domain>
    "emails": {
        "fallback": "vishavabhartiya.foundation@gmail.com",   # current working mailbox (keep until domain email is live)
        "info": "",        # e.g. info@<domain>      — leave "" until the mailbox is created and tested
        "csr": "",         # e.g. csr@<domain>
        "donations": "",   # e.g. donations@<domain>
    },
    "whatsapp": "919423632405",
    "social": {"youtube": "https://www.youtube.com/@vishavabhartiyafoundation", "facebook": "https://www.facebook.com/share/1DJMhnjx2n/"},
    "forms": {"endpoint": ""},   # TODO(owner): Google Apps Script web-app URL (backend/google-apps-script.gs). Empty = honest WhatsApp/email fallback
}
LANGS = ["en", "hi"]            # future: add "mr" + its strings; structure is ready
OUT = os.path.dirname(os.path.abspath(__file__))

def email(role):
    return CONFIG["emails"].get(role) or CONFIG["emails"]["fallback"]

# ======================================================================= helpers
LANG = "en"
def t(en, hi): return hi if LANG == "hi" else en
def R(): return "../" if LANG == "hi" else ""     # asset prefix

SIZES = {}
for f in glob.glob(os.path.join(OUT, "assets/img/**/*.*"), recursive=True):
    if f.lower().endswith((".webp", ".jpg", ".png")):
        with Image.open(f) as im: SIZES[os.path.relpath(f, OUT).replace(os.sep, "/")] = list(im.size)

def IMG(src, alt, cls="", lazy=True, cap=None, extra=""):
    w, h = SIZES.get(src, [None, None])
    wh = f' width="{w}" height="{h}"' if w else ""
    c = f' class="{cls}"' if cls else ""
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    dc = f' data-cap="{cap}"' if cap else ""
    return f'<img{c} src="{R()}{src}"{wh} alt="{alt}"{lz}{dc}{extra}>'

def ico(name):
    P = {
     "eye": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
     "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
     "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10Z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>',
     "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
     "mega": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
     "heart": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>',
     "woman": '<circle cx="12" cy="9" r="6"/><path d="M12 15v7M9 19h6"/>',
     "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
     "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
     "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
     "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
     "check": '<path d="M20 6 9 17l-5-5"/>',
     "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
     "down": '<path d="m6 9 6 6 6-6"/>',
     "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
     "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
     "youtube": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3z"/>',
     "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
     "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
     "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a2 2 0 0 0-2.8 0l-.9.9a2 2 0 0 1-2.8 0 1 1 0 0 1 0-1.4l2.8-2.8a3.5 3.5 0 0 1 4.9 0L21 9"/><path d="m21 3-9 9M3 12l4 4 3-3"/>',
    }
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{P[name]}</svg>'

ORG = {
 "cin": "U88900ME2026NPL473814", "lic": "181714", "pan": "AALCV9970E", "tan": "NGPV08949D",
 "darpan": "MH/2026/1028763", "eanudaan": "MH/00054145", "csr": "CSR00109367",
 "iso": "E20260347010", "udyam": "UDYAM-MH-20-0332301",
 "ph1": "+91 94236 32405", "ph2": "+91 86690 55934",
 "upi": "9423632405m1@pnb", "acc": "4608002100009435", "ifsc": "PUNB0460800",
}
def ADDR():  return t("Plot No. 3159/A/3, Diamond Nagar, Kharbi Main Road, Nandanvan Colony, Nagpur, Maharashtra 440024",
                      "प्लॉट नं. 3159/A/3, डायमंड नगर, खरबी मेन रोड, नंदनवन कॉलोनी, नागपुर, महाराष्ट्र 440024")
def SVC():   return t("Maharashtra Hospital &amp; Optical, A/3, New Diamond Nagar, Kharbi Main Road, Nagpur 440024",
                      "महाराष्ट्र हॉस्पिटल एवं ऑप्टिकल, A/3, न्यू डायमंड नगर, खरबी मेन रोड, नागपुर 440024")
def SOCIAL(cls="social"):
    s = CONFIG["social"]
    yt = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8Z"/><path fill="#fff" d="m9.75 15.02 5.75-3.02-5.75-3.02z"/></svg>'
    fb = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M13.5 22v-8.2h2.8l.4-3.2h-3.2V8.5c0-.9.3-1.6 1.6-1.6h1.7V4.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.3v3.2h2.8V22z"/></svg>'
    return f'<div class="{cls}" style="display:flex;gap:10px;align-items:center"><a class="si yt" style="background:#ff0000;color:#fff;width:36px;height:36px;border-radius:50%;display:inline-grid;place-items:center" href="{s["youtube"]}" target="_blank" rel="noopener" aria-label="YouTube" title="YouTube">{yt}</a><a class="si fb" style="background:#1877f2;color:#fff;width:36px;height:36px;border-radius:50%;display:inline-grid;place-items:center" href="{s["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook">{fb}</a></div>'
def NAME():  return t("Vishavabhartiya Foundation", "विश्वभारतीय फाउंडेशन")
def EM(role, link=True):
    e = email(role)
    return f'<a href="mailto:{e}" data-email="{role}">{e}</a>' if link else f'<span data-email="{role}">{e}</span>'

LEGACY_EN = "Vishavabhartiya Foundation was incorporated on 12 March 2026 and carries forward the community health, eye-care and social service initiatives begun in 1998 by its founder and the earlier organisation, Vishvabhartiya Manav Kalyan Sewa Sanstha."
LEGACY_HI = "विश्वभारतीय फाउंडेशन की स्थापना 12 मार्च 2026 को Section 8 कंपनी के रूप में हुई। फाउंडेशन संस्थापक एवं पूर्ववर्ती संस्था विश्वभारतीय मानव कल्याण सेवा संस्था द्वारा वर्ष 1998 से किए जा रहे स्वास्थ्य, नेत्र-जांच एवं सामुदायिक सेवा कार्यों को आगे बढ़ा रहा है।"
def LEGACY(): return t(LEGACY_EN, LEGACY_HI)

# ======================================================================= navigation / header / footer
def NAV():
    return [
     ("index.html", t("Home","होम"), None),
     (None, t("About","हमारे बारे में"), [("about.html",t("About Us","परिचय")),("about.html#vision",t("Vision &amp; Mission","दृष्टि एवं मिशन")),("about.html#objectives",t("Our Objectives","हमारे उद्देश्य")),("about.html#journey",t("Our Journey","हमारी यात्रा")),("about.html#team",t("Our Team","हमारी टीम")),("about.html#partners",t("Our Partners","हमारे साझेदार"))]),
     (None, t("Programmes","कार्यक्रम"), [("programs.html",t("Focus Areas &amp; Programmes","कार्यक्षेत्र एवं कार्यक्रम")),("programs.html#health",t("Health &amp; Eye Care","स्वास्थ्य एवं नेत्र सेवा")),("programs.html#education",t("Education &amp; Skill Development","शिक्षा एवं कौशल विकास")),("programs.html#women",t("Women Empowerment","महिला सशक्तिकरण")),("programs.html#environment",t("Environment &amp; Plantation","पर्यावरण एवं वृक्षारोपण")),("programs.html#awareness",t("Social Awareness","सामाजिक जागरूकता"))]),
     ("impact.html", t("Impact &amp; Awards","प्रभाव एवं सम्मान"), None),
     ("media.html", t("Media","मीडिया"), None),
     ("gallery.html", t("Gallery","गैलरी"), None),
     (None, t("Transparency","पारदर्शिता"), [("registrations.html",t("Registrations &amp; Certifications","पंजीकरण एवं प्रमाणन")),("transparency.html",t("Transparency &amp; Governance","पारदर्शिता एवं शासन")),("donation-policy.html",t("Donation &amp; Refund Policy","दान एवं धनवापसी नीति")),("safeguarding.html",t("Safeguarding Statement","सुरक्षा (सेफ़गार्डिंग) वक्तव्य")),("grievance.html",t("Grievance Mechanism","शिकायत निवारण"))]),
     ("csr.html", t("CSR","CSR"), None),
     ("contact.html", t("Contact","संपर्क"), None),
    ]

def lang_switch(fname):
    if LANG == "en":
        return f'<div class="lang" role="navigation" aria-label="Language"><span aria-current="true" lang="en">EN</span><a href="hi/{fname}" lang="hi" hreflang="hi">हिंदी</a></div>'
    return f'<div class="lang" role="navigation" aria-label="भाषा"><a href="../{fname}" lang="en" hreflang="en">EN</a><span aria-current="true" lang="hi">हिंदी</span></div>'

def header(active):
    items = []
    for href, label, sub in NAV():
        if sub is None:
            cur = ' aria-current="page"' if href == active else ""
            items.append(f'<a href="{href}"{cur}>{label}</a>')
        else:
            act = " active" if any(s[0].split("#")[0] == active for s in sub) else ""
            links = "".join(f'<a href="{h}">{l}</a>' for h, l in sub)
            items.append(f'<div class="dd{act}"><button type="button" aria-expanded="false">{label}{ico("down")}</button><div class="dd-menu">{links}</div></div>')
    items.append(f'<a class="btn btn-gold" href="donate.html">{t("Donate","दान करें")}</a>')
    return f'''<a class="skip" href="#main">{t("Skip to content","मुख्य सामग्री पर जाएँ")}</a>
<div class="topstrip"><div class="wrap">
  <span>{ico("shield")} {t("Section 8 Not-for-Profit · 12A &amp; 80G · CSR-1 · NGO Darpan","Section 8 गैर-लाभकारी · 12A एवं 80G · CSR-1 · NGO दर्पण")}</span>
  <span><a href="tel:+919423632405">{ico("phone")} {ORG["ph1"]}</a> {ico("mail")} {EM("info")} {SOCIAL("social top")}</span>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="{NAME()} — {t("home","होम")}">
    <img src="{R()}assets/img/logo-160.webp" alt="" width="72" height="72">
    <span><b>VISHAVABHARTIYA</b><small>{t("Foundation · Nagpur","फाउंडेशन · नागपुर")}</small></span>
  </a>
  {lang_switch(active)}
  {SOCIAL("social hdr")}
  <button class="menu-btn" type="button" aria-label="{t("Open menu","मेनू खोलें")}" aria-expanded="false">{ico("menu")}</button>
  <nav class="nav" aria-label="{t("Main","मुख्य")}">{"".join(items)}</nav>
</div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div>
      <div class="foot-brand"><img src="{R()}assets/img/logo-160.webp" alt="" width="60" height="60" loading="lazy"><b>{t("Vishavabhartiya<br>Foundation","विश्वभारतीय<br>फाउंडेशन")}</b></div>
      <p>{t("A Section 8 not-for-profit company (est. 12 March 2026) carrying forward community health and eye-care work begun in 1998.","12 मार्च 2026 को स्थापित Section 8 गैर-लाभकारी कंपनी, जो 1998 से चल रहे सामुदायिक स्वास्थ्य एवं नेत्र-सेवा कार्य को आगे बढ़ा रही है।")}</p>
      <p class="deva" style="color:var(--gold-lt)">रोगोत्मूलम् · दीर्घजीवनम्</p>
      {SOCIAL()}
    </div>
    <div><h4>{t("Explore","जानें")}</h4><ul>
      <li><a href="about.html">{t("About Us","परिचय")}</a></li><li><a href="programs.html">{t("Programmes","कार्यक्रम")}</a></li><li><a href="impact.html">{t("Impact &amp; Awards","प्रभाव एवं सम्मान")}</a></li>
      <li><a href="media.html">{t("Media Coverage","मीडिया कवरेज")}</a></li><li><a href="gallery.html">{t("Photo Gallery","फ़ोटो गैलरी")}</a></li><li><a href="about.html#team">{t("Our Team","हमारी टीम")}</a></li></ul></div>
    <div><h4>{t("Support","सहयोग")}</h4><ul>
      <li><a href="donate.html">{t("Donate","दान करें")}</a></li><li><a href="donate.html#receipt">{t("Request 80G Receipt","80G रसीद का अनुरोध")}</a></li><li><a href="csr.html">{t("CSR Partnerships","CSR साझेदारी")}</a></li><li><a href="contact.html#volunteer">{t("Volunteer","स्वयंसेवक बनें")}</a></li></ul></div>
    <div><h4>{t("Trust &amp; Legal","विश्वास एवं नीतियाँ")}</h4><ul>
      <li><a href="registrations.html">{t("Registrations","पंजीकरण")}</a></li><li><a href="transparency.html">{t("Transparency &amp; Governance","पारदर्शिता एवं शासन")}</a></li>
      <li><a href="privacy.html">{t("Privacy Policy","गोपनीयता नीति")}</a></li><li><a href="terms.html">{t("Terms of Use","उपयोग की शर्तें")}</a></li>
      <li><a href="donation-policy.html">{t("Donation &amp; Refund Policy","दान एवं धनवापसी नीति")}</a></li><li><a href="photo-consent.html">{t("Photo &amp; Media Consent","फ़ोटो एवं मीडिया सहमति")}</a></li>
      <li><a href="safeguarding.html">{t("Safeguarding Statement","सेफ़गार्डिंग वक्तव्य")}</a></li><li><a href="grievance.html">{t("Grievance Mechanism","शिकायत निवारण")}</a></li></ul></div>
    <div><h4>{t("Registered Office","पंजीकृत कार्यालय")}</h4><ul>
      <li>{ADDR()}</li>
      <li><a href="tel:+919423632405">{ORG["ph1"]}</a> · <a href="tel:+918669055934">{ORG["ph2"]}</a></li>
      <li>{EM("info")}</li></ul>
      <p class="foot-reg" style="margin-top:14px">CIN {ORG["cin"]}<br>{t("Sec. 8 Licence","Sec. 8 लाइसेंस")} {ORG["lic"]}<br>PAN {ORG["pan"]} · CSR {ORG["csr"]}<br>NGO Darpan {ORG["darpan"]}</p></div>
  </div>
  <div class="foot-bottom"><span>© <span id="year">2026</span> {NAME()}, {t("Nagpur. All rights reserved.","नागपुर। सर्वाधिकार सुरक्षित।")}</span><span>{t("“A service to man is a service to God.”","“मानव सेवा ही ईश्वर सेवा है।”")}</span></div>
</div></footer>
<a class="btn btn-gold float-donate" href="donate.html">{t("Support our work — Donate","हमारे कार्य में सहयोग करें — दान करें")}</a>'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hind:wght@400;600&family=IBM+Plex+Mono&family=Marcellus&family=Tiro+Devanagari+Hindi&display=swap">'
PAGES_BUILT = []

def page(fname, title, desc, body, extra_head=""):
    site = CONFIG["site_url"].rstrip("/")
    def url(lang): return site + "/" + ("hi/" if lang == "hi" else "") + ("" if fname == "index.html" else fname)
    brand = NAME()
    full_title = title if fname == "index.html" else f"{title} | {brand}"
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l)}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'
    head = f'''<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url(LANG)}">{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="{brand}"><meta property="og:locale" content="{t("en_IN","hi_IN")}">
<meta property="og:title" content="{full_title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(LANG)}"><meta property="og:image" content="{site}/assets/img/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#3a2214">
<link rel="icon" type="image/png" href="{R()}assets/img/favicon.png"><link rel="apple-touch-icon" href="{R()}assets/img/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="{R()}assets/css/style.css?v=20261025b">{extra_head}'''
    inner = f'''{header(fname)}
<main id="main">
{body}
</main>
{footer()}
<script src="{R()}assets/js/config.js?v=20261025b"></script>
<script src="{R()}assets/js/img-sizes.js?v=20261025b"></script>
<script src="{R()}assets/js/data.js?v=20261025b"></script>
<script src="{R()}assets/js/main.js?v=20261025b"></script>'''
    full = f'''<!doctype html>
<html lang="{LANG}" data-base="{R()}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{inner}
</body>
</html>
'''
    d = os.path.join(OUT, "hi") if LANG == "hi" else OUT
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, fname), "w", encoding="utf-8").write(full)
    if LANG == "en": PAGES_BUILT.append(fname)

def banner(crumb, h1, p):
    return f'''<section class="page-banner"><div class="wrap">
  <div class="crumbs"><a href="index.html">{t("Home","होम")}</a> / {crumb}</div>
  <h1>{h1}</h1><p>{p}</p></div></section>'''

def CTA():
    return f'''<section class="tight"><div class="wrap"><div class="cta-band">
  <div><h2>{t("Help us take care to one more family","एक और परिवार तक सेवा पहुँचाने में सहयोग करें")}</h2>
  <p>{t("Your donation supports free eye care, health camps and community programmes. Donations are eligible for tax benefit under Section 80G.","आपका दान निःशुल्क नेत्र सेवा, स्वास्थ्य शिविरों और सामुदायिक कार्यक्रमों में सहायक होता है। दान पर धारा 80G के अंतर्गत कर-लाभ उपलब्ध है।")}</p></div>
  <div class="ctas"><a class="btn btn-gold" href="donate.html">{t("Donate now","अभी दान करें")}</a><a class="btn btn-light" href="csr.html">{t("Partner through CSR","CSR के माध्यम से साझेदारी")}</a></div>
</div></div></section>'''

# ======================================================================= shared content
def FOCUS():
    return [
     ("health","eye",t("Health &amp; Eye Care","स्वास्थ्य एवं नेत्र सेवा"),t("Free eye check-ups, spectacles, health camps, blood donation and immunisation support.","निःशुल्क नेत्र जाँच, चश्मा वितरण, स्वास्थ्य शिविर, रक्तदान और टीकाकरण में सहयोग।")),
     ("education","book",t("Education &amp; Skills","शिक्षा एवं कौशल"),t("School awareness, competitions, personality development and skill training for youth.","विद्यालय जागरूकता, प्रतियोगिताएँ, व्यक्तित्व विकास और युवाओं के लिए कौशल प्रशिक्षण।")),
     ("women","woman",t("Women Empowerment","महिला सशक्तिकरण"),t("Mother-and-child health, women's health camps and programmes for women's self-reliance.","मातृ-शिशु स्वास्थ्य, महिला स्वास्थ्य शिविर और महिलाओं की आत्मनिर्भरता के कार्यक्रम।")),
     ("environment","leaf",t("Environment &amp; Plantation","पर्यावरण एवं वृक्षारोपण"),t("Tree plantation, cleanliness drives, Earth Day action and plastic-free campaigns.","वृक्षारोपण, स्वच्छता अभियान, पृथ्वी दिवस कार्यक्रम और प्लास्टिक-मुक्त अभियान।")),
     ("awareness","mega",t("Social Awareness","सामाजिक जागरूकता"),t("HIV/AIDS, leprosy, tobacco, voter enrolment and civic awareness in local languages.","HIV/एड्स, कुष्ठरोग, तंबाकू, मतदाता पंजीयन और नागरिक जागरूकता — स्थानीय भाषा में।")),
     ("awareness","users",t("Community Development","सामुदायिक विकास"),t("Service to slum dwellers, labourers, farmers, drivers and other underserved groups.","झुग्गी-बस्ती निवासियों, मज़दूरों, किसानों, चालकों और वंचित वर्गों की सेवा।")),
    ]
def focus_cards():
    return "".join(f'<a class="focus" href="programs.html#{a}"><span class="ic">{ico(i)}</span><h3>{ti}</h3><p>{d}</p><span class="more">{t("Learn more →","और जानें →")}</span></a>' for a,i,ti,d in FOCUS())

def STATS():
    return f'''<div class="stats">
    <div class="stat"><b>28+</b><span>{t("years of founder-led community health work (1998–2026)","वर्षों का संस्थापक-नेतृत्व सामुदायिक स्वास्थ्य कार्य (1998–2026)")}</span><em>{t("Founder &amp; earlier Sanstha","संस्थापक एवं पूर्ववर्ती संस्था")}</em></div>
    <div class="stat"><b>25</b><span>{t("years of Pulse Polio volunteering with NMC (1998–2023)","वर्षों तक मनपा पल्स पोलियो अभियान में सेवा (1998–2023)")}</span><em>{t("Founder &amp; earlier Sanstha","संस्थापक एवं पूर्ववर्ती संस्था")}</em></div>
    <div class="stat"><b>2</b><span>{t("core districts: Nagpur and Bhandara","मुख्य ज़िले: नागपुर और भंडारा")}</span><em>{t("Area of work","कार्यक्षेत्र")}</em></div>
    <div class="stat"><b>11</b><span>{t("key registrations &amp; certifications","प्रमुख पंजीकरण एवं प्रमाणन")}</span><em>{t("Foundation, 2026","फाउंडेशन, 2026")}</em></div>
    <div class="stat"><b>3</b><span>{t("awards &amp; honours conferred on the founder","संस्थापक को प्राप्त पुरस्कार एवं सम्मान")}</span><em>{t("Founder's honours","संस्थापक सम्मान")}</em></div>
  </div>'''

def REGS():
    L = [
     ("legal", t("Certificate of Incorporation (Section 8 company)","निगमन प्रमाणपत्र (Section 8 कंपनी)"), t("Ministry of Corporate Affairs","कॉर्पोरेट कार्य मंत्रालय"), "CIN "+ORG["cin"], "12 Mar 2026", "certificate-of-incorporation", "certificate-of-incorporation.pdf"),
     ("legal", t("Licence under Section 8(1), Companies Act 2013","कंपनी अधिनियम 2013 की धारा 8(1) के अंतर्गत लाइसेंस"), t("Registrar of Companies, CRC Manesar","रजिस्ट्रार ऑफ़ कंपनीज़, CRC मानेसर"), t("Licence No. ","लाइसेंस सं. ")+ORG["lic"], "12 Mar 2026", None, "section-8-licence.pdf"),
     ("legal", t("Permanent Account Number","स्थायी खाता संख्या (PAN)"), t("Income Tax Department","आयकर विभाग"), "PAN "+ORG["pan"], "12 Mar 2026", "pan-card", None),
     ("legal", t("Tax Deduction Account Number","कर कटौती खाता संख्या (TAN)"), t("Income Tax Department","आयकर विभाग"), "TAN "+ORG["tan"], "12 Mar 2026", "tan-allotment", None),
     ("legal", t("Udyam Registration","उद्यम पंजीकरण"), t("Ministry of MSME","MSME मंत्रालय"), ORG["udyam"], "14 Mar 2026", "udyam-registration", None),
     ("tax", t("Registration u/s 12A (provisional)","धारा 12A के अंतर्गत पंजीकरण (अस्थायी)"), t("Income Tax Department, Form 10AC","आयकर विभाग, फ़ॉर्म 10AC"), "URN AALCV9970EE20251 · AY 2026-27 – AY 2028-29", "30 Mar 2026", "12a-provisional", "12a-80g-provisional-approval.pdf"),
     ("tax", t("Approval u/s 80G (provisional)","धारा 80G के अंतर्गत अनुमोदन (अस्थायी)"), t("Income Tax Department, Form 10AC","आयकर विभाग, फ़ॉर्म 10AC"), "URN AALCV9970EF20261 · AY 2026-27 – AY 2028-29", "30 Mar 2026", "80g-provisional", "12a-80g-provisional-approval.pdf"),
     ("ngo", t("CSR-1 Registration","CSR-1 पंजीकरण"), t("Ministry of Corporate Affairs, ROC Nagpur","कॉर्पोरेट कार्य मंत्रालय, ROC नागपुर"), ORG["csr"], "7 Apr 2026", "csr-1-registration", None),
     ("ngo", t("NGO Darpan","NGO दर्पण"), t("NITI Aayog, Government of India","नीति आयोग, भारत सरकार"), t("Unique ID ","यूनिक आईडी ")+ORG["darpan"], "14 Mar 2026", "ngo-darpan", None),
     ("ngo", t("e-Anudaan enrolment","ई-अनुदान नामांकन"), t("Ministry of Social Justice &amp; Empowerment","सामाजिक न्याय एवं अधिकारिता मंत्रालय"), "NGO ID "+ORG["eanudaan"], "2026", "e-anudaan", None),
     ("cert", t("ISO 9001:2015 Quality Management System","ISO 9001:2015 गुणवत्ता प्रबंधन प्रणाली"), t("Royal Assessments Pvt. Ltd. — independent certification body (IAF / EGAC accredited)","रॉयल असेसमेंट्स प्रा. लि. — स्वतंत्र प्रमाणन संस्था (IAF / EGAC मान्यता)"), t("Cert. ","प्रमाणपत्र ")+ORG["iso"]+t(" · valid to 3 Mar 2029"," · 3 मार्च 2029 तक मान्य"), "4 Mar 2026", "iso-9001-2015", None),
    ]
    return L
def REG_GROUPS():
    return {"legal": t("Legal Registrations","वैधानिक पंजीकरण"), "tax": t("Tax Exemptions","कर छूट"), "ngo": t("NGO / CSR Registrations","NGO / CSR पंजीकरण"), "cert": t("Certifications (independent)","प्रमाणन (स्वतंत्र)")}

# ======================================================================= PAGES
def build_home():
    jsonld = {"@context":"https://schema.org","@type":"NGO","name":"Vishavabhartiya Foundation","alternateName":"विश्वभारतीय फाउंडेशन",
      "url":CONFIG["site_url"].rstrip("/")+"/","logo":CONFIG["site_url"].rstrip("/")+"/assets/img/logo.webp","image":CONFIG["site_url"].rstrip("/")+"/assets/img/og-image.jpg",
      "email":email("info"),"telephone":"+91-9423632405","foundingDate":"2026-03-12","nonprofitStatus":"Nonprofit",
      "founder":{"@type":"Person","name":"Dr. Dhananjay Kewalram Yerne","jobTitle":"Managing Director & CEO"},
      "address":{"@type":"PostalAddress","streetAddress":"Plot No. 3159/A/3, Diamond Nagar, Kharbi Main Road, Nandanvan Colony","addressLocality":"Nagpur","addressRegion":"Maharashtra","postalCode":"440024","addressCountry":"IN"},
      "identifier":[{"@type":"PropertyValue","name":"CIN","value":ORG["cin"]},{"@type":"PropertyValue","name":"NGO Darpan","value":ORG["darpan"]},{"@type":"PropertyValue","name":"CSR-1","value":ORG["csr"]}],
      "areaServed":["Nagpur","Bhandara","Maharashtra"],"sameAs":list(CONFIG["social"].values())}
    body = f'''
<section class="hero" style="padding:0">
  <div class="wrap">
    <div class="hero-copy">
      <a class="award-flag" href="impact.html#honours">
        {IMG("assets/img/awards/global-awards-logo.webp", "Global Awards logo", lazy=False)}
        <span class="af-text">
          <span class="af-kicker">{t("★ Founder's Honour · 2025-26 ★","★ संस्थापक सम्मान · 2025-26 ★")}</span>
          <b>{t("Global Sustainability Award","ग्लोबल सस्टेनेबिलिटी अवॉर्ड")}</b>
          <span class="af-cat">{t("Individual Changemaker (Top 35) — Dr. Dhananjay K. Yerne, MD &amp; CEO","इंडिविजुअल चेंजमेकर (टॉप 35) — डॉ. धनंजय के. येरने, एमडी एवं सीईओ")}</span>
          <span class="af-note">{t("Recognised for health-awareness work in Nagpur &amp; Bhandara districts since 1998. Presented on 10 Oct 2026 at Miranda House, University of Delhi.","नागपुर एवं भंडारा ज़िलों में 1998 से स्वास्थ्य-जागरूकता कार्य के लिए। 10 अक्टूबर 2026 को मिरांडा हाउस, दिल्ली विश्वविद्यालय में प्रदान किया गया।")}</span>
        </span>
      </a>
      <p class="motto">रोगोत्मूलम् · दीर्घजीवनम् — {t("Root out disease, live long","रोग का उन्मूलन, दीर्घ जीवन")}</p>
      <h1>{t("Health, sight and dignity for <em>every</em> family in Vidarbha","विदर्भ के <em>हर</em> परिवार के लिए स्वास्थ्य, दृष्टि और सम्मान")}</h1>
      <p class="lede">{LEGACY()}</p>
      <div class="ctas"><a class="btn btn-gold" href="donate.html">{t("Donate &amp; support","दान एवं सहयोग")}</a><a class="btn btn-light" href="programs.html">{t("See our programmes","हमारे कार्यक्रम देखें")}</a></div>
      <ul class="hero-facts">
        <li><b>2026</b><span>{t("Foundation incorporated","फाउंडेशन की स्थापना")}</span></li>
        <li><b>1998</b><span>{t("founder's legacy of service","संस्थापक की सेवा-विरासत")}</span></li>
        <li><b>12A · 80G</b><span>{t("tax-exempt giving","कर-मुक्त दान")}</span></li>
      </ul>
    </div>
    <div class="hero-visual">
      <figure class="hv-slot">{IMG("assets/img/gallery/yoga-day-2026.webp", t("International Yoga Day 2026","अंतर्राष्ट्रीय योग दिवस 2026"), "on", lazy=False)}<figcaption>{t("International Yoga Day 2026","अंतर्राष्ट्रीय योग दिवस 2026")}</figcaption></figure>
      <figure class="hv-slot">{IMG("assets/img/gallery/earth-day-2026.webp", t("Earth Day 2026","पृथ्वी दिवस 2026"), "on")}<figcaption>{t("Earth Day 2026","पृथ्वी दिवस 2026")}</figcaption></figure>
      <div class="hv-badge"><b>1998</b><span>{t("founder's legacy<br>of free eye care","संस्थापक की<br>निःशुल्क नेत्र-सेवा")}</span></div>
    </div>
  </div>
</section>
<div class="ribbon"><div class="wrap">
  <span>{ico("shield")} <b>Section 8</b> {t("Company · MCA","कंपनी · MCA")}</span>
  <span>{ico("check")} <b>12A &amp; 80G</b> {t("Income Tax","आयकर")}</span>
  <span>{ico("check")} <b>CSR-1</b> {ORG["csr"]}</span>
  <span>{ico("check")} <b>{t("NGO Darpan","NGO दर्पण")}</b> {t("NITI Aayog","नीति आयोग")}</span>
  <span>{ico("check")} <b>e-Anudaan</b> MoSJE</span>
  <span>{ico("check")} <b>ISO 9001:2015</b> {t("certified","प्रमाणित")}</span>
</div></div>

<section><div class="wrap split">
  <div class="photo-stack">
    {IMG("assets/img/gallery/eye-camp-screening.webp", t("Free eye screening at a mega eye check-up camp","भव्य नेत्र जाँच शिविर में निःशुल्क जाँच"))}
    <div class="badge"><b>1998 → 2026</b><small>{t("from the founder's clinic and Sanstha to a registered Foundation","संस्थापक के क्लिनिक एवं संस्था से पंजीकृत फाउंडेशन तक")}</small></div>
  </div>
  <div>
    <span class="eyebrow">{t("About us","हमारे बारे में")}</span><hr class="rule">
    <h2>{t("A legacy that began at a neighbourhood clinic","एक मोहल्ले के क्लिनिक से शुरू हुई सेवा-विरासत")}</h2>
    <p>{t("In 1998 our founder, optometrist Dr. Dhananjay K. Yerne, opened a public hospital and mother-and-child health centre on Kharbi Road, Nagpur, and began free eye check-up camps. Through his earlier organisation, Vishvabhartiya Manav Kalyan Sewa Sanstha, the work reached slums, labour colonies, villages, schools, anganwadis, places of worship of every faith, the Nagpur Central Jail and highway petrol pumps.","1998 में हमारे संस्थापक, ऑप्टोमेट्रिस्ट डॉ. धनंजय के. येरने ने खरबी रोड, नागपुर में सार्वजनिक अस्पताल एवं मातृ-शिशु स्वास्थ्य केंद्र शुरू किया और निःशुल्क नेत्र जाँच शिविर आरंभ किए। उनकी पूर्ववर्ती संस्था विश्वभारतीय मानव कल्याण सेवा संस्था के माध्यम से यह सेवा झुग्गी-बस्तियों, मज़दूर कॉलोनियों, गाँवों, विद्यालयों, आंगनवाड़ियों, सभी धर्मों के पूजा-स्थलों, नागपुर केंद्रीय कारागृह और राजमार्ग पेट्रोल पंपों तक पहुँची।")}</p>
    <p>{t("On <b>12 March 2026</b> this work gained an institutional home: <b>Vishavabhartiya Foundation</b>, a Section 8 not-for-profit company registered with the Ministry of Corporate Affairs.","<b>12 मार्च 2026</b> को इस कार्य को संस्थागत स्वरूप मिला: <b>विश्वभारतीय फाउंडेशन</b>, कॉर्पोरेट कार्य मंत्रालय में पंजीकृत Section 8 गैर-लाभकारी कंपनी।")}</p>
    <ul class="checks">
      <li>{ico("check")} {t("Free eye check-ups and spectacle distribution for people in need","ज़रूरतमंदों के लिए निःशुल्क नेत्र जाँच एवं चश्मा वितरण")}</li>
      <li>{ico("check")} {t("Awareness in the local language, where people live and work","लोगों के बीच, उनकी भाषा में जागरूकता")}</li>
      <li>{ico("check")} {t("Registered, CSR-eligible and committed to transparent reporting","पंजीकृत, CSR-पात्र एवं पारदर्शी रिपोर्टिंग के लिए प्रतिबद्ध")}</li>
    </ul>
    <a class="btn btn-line" href="about.html">{t("Read our story","हमारी कहानी पढ़ें")}</a>
  </div>
</div></section>

<section class="dark"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Our impact","हमारा प्रभाव")}</span><h2>{t("A legacy of steady work, now institutionalised","निरंतर सेवा की विरासत, अब संस्थागत रूप में")}</h2>
  <p>{t("Figures we can document. Legacy figures relate to the founder and the earlier Sanstha; beneficiary counts will be published in the Foundation's annual report.","वही आँकड़े जिनका प्रमाण उपलब्ध है। विरासत संबंधी आँकड़े संस्थापक एवं पूर्ववर्ती संस्था के हैं; लाभार्थियों की संख्या फाउंडेशन की वार्षिक रिपोर्ट में प्रकाशित की जाएगी।")}</p></div>
  {STATS()}
</div></section>

<section><div class="wrap">
  <div class="sec-head center"><span class="eyebrow">{t("Focus areas","कार्यक्षेत्र")}</span><hr class="rule"><h2>{t("Where we work","हम कहाँ काम करते हैं")}</h2>
  <p>{t("Six connected areas, with preventive health and eye care at the centre.","छह जुड़े हुए क्षेत्र, जिनके केंद्र में निवारक स्वास्थ्य एवं नेत्र सेवा है।")}</p></div>
  <div class="grid g3">{focus_cards()}</div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Latest activities","नवीनतम गतिविधियाँ")}</span><hr class="rule"><h2>{t("What's happening","क्या हो रहा है")}</h2></div>
  <div class="grid g3" data-render="activities" data-limit="3"></div>
  <p class="mt"><a class="btn btn-line" href="impact.html#activities">{t("All activities","सभी गतिविधियाँ")}</a></p>
</div></section>

<section><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">{t("Founder's Honours &amp; Recognition","संस्थापक के सम्मान एवं मान्यता")}</span><hr class="rule">
    <h2>{t("Honours received by our founder","संस्थापक को प्राप्त सम्मान")}</h2>
    <p class="muted">{t("Personal honours of Dr. Dhananjay K. Yerne for his social work since 1998.","1998 से सामाजिक कार्य हेतु डॉ. धनंजय के. येरने को व्यक्तिगत रूप से प्राप्त सम्मान।")}</p>
    <div class="grid" data-render="honours"></div>
  </div>
  <div>
    <span class="eyebrow">{t("Foundation Achievements &amp; Certifications","फाउंडेशन की उपलब्धियाँ एवं प्रमाणन")}</span><hr class="rule">
    <h2>{t("Institutional milestones, 2026","संस्थागत उपलब्धियाँ, 2026")}</h2>
    <ul class="tlist">
      <li><span>{t("Section 8 incorporation &amp; licence","Section 8 निगमन एवं लाइसेंस")}</span><span class="st ok">12 Mar 2026</span></li>
      <li><span>{t("NGO Darpan · e-Anudaan · Udyam","NGO दर्पण · ई-अनुदान · उद्यम")}</span><span class="st ok">Mar 2026</span></li>
      <li><span>{t("ISO 9001:2015 certification","ISO 9001:2015 प्रमाणन")}</span><span class="st ok">4 Mar 2026</span></li>
      <li><span>{t("12A &amp; 80G (provisional)","12A एवं 80G (अस्थायी)")}</span><span class="st ok">30 Mar 2026</span></li>
      <li><span>{t("CSR-1 registration","CSR-1 पंजीकरण")}</span><span class="st ok">7 Apr 2026</span></li>
    </ul>
    <p class="mt"><a class="btn btn-line" href="registrations.html">{t("View all registrations","सभी पंजीकरण देखें")}</a> <a class="btn btn-line" href="impact.html#honours">{t("All honours","सभी सम्मान")}</a></p>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("In the news","समाचारों में")}</span><hr class="rule"><h2>{t("Media coverage","मीडिया कवरेज")}</h2></div>
  <div class="grid g3" data-render="media" data-limit="3"></div>
  <p class="mt"><a class="btn btn-line" href="media.html">{t("All press coverage","सभी समाचार")}</a></p>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Photo gallery","फ़ोटो गैलरी")}</span><hr class="rule"><h2>{t("Moments from the field","कार्यक्षेत्र की झलकियाँ")}</h2></div>
  <div class="gallery" data-render="gallery" data-limit="6"></div>
  <p class="mt"><a class="btn btn-line" href="gallery.html">{t("Open the full gallery","पूरी गैलरी देखें")}</a></p>
</div></section>

<section><div class="wrap">
  <div class="sec-head center"><span class="eyebrow">{t("Our partners","हमारे साझेदार")}</span><hr class="rule"><h2>{t("Our Partners","हमारे साझेदार")}</h2></div>
  <div class="plogos" data-render="logo-strip"></div>
  <p class="center mt"><a class="btn btn-line" href="about.html#partners">{t("About our partners","हमारे साझेदारों के बारे में")}</a></p>
</div></section>

<section class="alt"><div class="wrap">
  <div class="sec-head center"><span class="eyebrow">{t("Leadership","नेतृत्व")}</span><hr class="rule"><h2>{t("Board of Directors","निदेशक मंडल")}</h2></div>
  <div class="grid g3">{BOARD_CARDS(short=True)}</div>
  <p class="center mt"><a class="btn btn-line" href="about.html#team">{t("Meet the team","टीम से मिलें")}</a></p>
</div></section>

{CTA()}

<section><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">{t("Contact","संपर्क")}</span><hr class="rule"><h2>{t("Visit or call us","हमसे मिलें या फ़ोन करें")}</h2>
    <ul class="contact-list">
      <li><span class="ic">{ico("pin")}</span><div><b>{t("Registered office","पंजीकृत कार्यालय")}</b><span>{ADDR()}</span></div></li>
      <li><span class="ic">{ico("eye")}</span><div><b>{t("Eye care / service centre","नेत्र सेवा / सेवा केंद्र")}</b><span>{SVC()}</span></div></li>
      <li><span class="ic">{ico("phone")}</span><div><b>{t("Phone / WhatsApp","फ़ोन / WhatsApp")}</b><span>{ORG["ph1"]} · {ORG["ph2"]}</span></div></li>
      <li><span class="ic">{ico("mail")}</span><div><b>{t("Email","ईमेल")}</b><span>{EM("info", link=False)}</span></div></li>
    </ul>
  </div>
  <div class="panel">
    <h3>{t("For CSR teams and institutions","CSR टीमों एवं संस्थानों के लिए")}</h3>
    <p class="muted">{t("We share registration documents and prepare a project proposal and budget for each partnership after a needs discussion.","हम पंजीकरण दस्तावेज़ साझा करते हैं और आवश्यकता पर चर्चा के बाद हर साझेदारी के लिए परियोजना प्रस्ताव एवं बजट तैयार करते हैं।")}</p>
    <p><a class="btn btn-gold" href="csr.html">{t("CSR Partnerships","CSR साझेदारी")}</a> <a class="btn btn-line" href="contact.html">{t("Send an enquiry","संदेश भेजें")}</a></p>
  </div>
</div></section>'''
    page("index.html",
         t("Vishavabhartiya Foundation — NGO in Nagpur for Health, Eye Care &amp; Community Welfare","विश्वभारतीय फाउंडेशन — नागपुर में स्वास्थ्य, नेत्र सेवा एवं समाज कल्याण हेतु NGO"),
         t("Vishavabhartiya Foundation, Nagpur: Section 8 NGO (est. 2026; 12A, 80G, CSR-1, NGO Darpan) carrying forward free eye care and community health work begun in 1998.",
           "विश्वभारतीय फाउंडेशन, नागपुर: Section 8 NGO (स्थापना 2026; 12A, 80G, CSR-1, NGO दर्पण), जो 1998 से चल रहे निःशुल्क नेत्र-सेवा एवं सामुदायिक स्वास्थ्य कार्य को आगे बढ़ा रहा है।"),
         body, '\n<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + '</script>')

def BOARD_CARDS(short=False):
    P = [("assets/img/team/dhananjay-yerne.webp", t("Dr. Dhananjay Kewalram Yerne","डॉ. धनंजय केवलराम येरने"), t("Managing Director &amp; CEO · DIN 11602652","प्रबंध निदेशक एवं सीईओ · DIN 11602652"),
          t("Optometrist and founder; free eye care and health awareness since 1998.","ऑप्टोमेट्रिस्ट एवं संस्थापक; 1998 से निःशुल्क नेत्र सेवा एवं स्वास्थ्य जागरूकता।")),
         ("assets/img/team/ajaya-yerne.webp", t("Dr. Ajaya Dhananjay Yerne","डॉ. अजया धनंजय येरने"), t("Director · DIN 11602653","निदेशक · DIN 11602653"),
          t("Co-founder and subscriber to the Memorandum; health camps and women's programmes.","सह-संस्थापक एवं मेमोरेंडम की हस्ताक्षरकर्ता; स्वास्थ्य शिविर एवं महिला कार्यक्रम।")),
         ("assets/img/team/tejendra-yerne.webp", t("Dr. Tejendra Dhananjay Yerne","डॉ. तेजेंद्र धनंजय येरने"), t("Director · DIN 11602654","निदेशक · DIN 11602654"),
          t("Co-founder and subscriber to the Memorandum; a doctor supporting health camps and awareness.","सह-संस्थापक एवं मेमोरेंडम के हस्ताक्षरकर्ता; स्वास्थ्य शिविरों एवं जागरूकता में सहयोगी चिकित्सक।"))]
    if not short: P = P[1:]
    return "".join(f'<div class="person">{IMG(s, n, "ph")}<div class="body"><h3>{n}</h3><span class="role">{r}</span><p>{d}</p></div></div>' for s,n,r,d in P)

def build_about():
    OBJ = [
     (t("Preventive health &amp; eye care","निवारक स्वास्थ्य एवं नेत्र सेवा"),t("Run free eye check-up and health camps, distribute spectacles, and refer patients for treatment.","निःशुल्क नेत्र जाँच एवं स्वास्थ्य शिविर, चश्मा वितरण और उपचार हेतु रेफ़रल।")),
     (t("Health awareness","स्वास्थ्य जागरूकता"),t("Educate communities on eye health, communicable diseases, tobacco, nutrition and hygiene.","नेत्र स्वास्थ्य, संक्रामक रोग, तंबाकू, पोषण एवं स्वच्छता पर जन-जागरूकता।")),
     (t("Education","शिक्षा"),t("Support schools and students; run competitions and awareness programmes that build confidence.","विद्यालयों एवं विद्यार्थियों को सहयोग; आत्मविश्वास बढ़ाने वाली प्रतियोगिताएँ एवं कार्यक्रम।")),
     (t("Skill development","कौशल विकास"),t("Offer vocational and life-skill training for youth and women.","युवाओं एवं महिलाओं के लिए व्यावसायिक एवं जीवन-कौशल प्रशिक्षण।")),
     (t("Women &amp; children","महिलाएँ एवं बच्चे"),t("Promote mother-and-child health and women's social and economic empowerment.","मातृ-शिशु स्वास्थ्य तथा महिलाओं का सामाजिक एवं आर्थिक सशक्तिकरण।")),
     (t("Environment","पर्यावरण"),t("Organise tree plantation, cleanliness and plastic-reduction drives.","वृक्षारोपण, स्वच्छता एवं प्लास्टिक-कमी अभियान।")),
     (t("Civic &amp; social awareness","नागरिक एवं सामाजिक जागरूकता"),t("Encourage voter enrolment, rights awareness and access to government schemes.","मतदाता पंजीयन, अधिकारों की जानकारी एवं सरकारी योजनाओं तक पहुँच।")),
     (t("Welfare of the disadvantaged","वंचितों का कल्याण"),t("Serve the elderly, differently-abled, labourers, slum dwellers and farmers without discrimination.","बुज़ुर्गों, दिव्यांगों, मज़दूरों, बस्तीवासियों एवं किसानों की बिना भेदभाव सेवा।")),
    ]
    obj = "".join(f'<div class="focus"><h3>{a}</h3><p>{b}</p></div>' for a,b in OBJ)
    LEG = [
     ("1 May 1998",t("Public hospital and mother-child health centre opened","सार्वजनिक अस्पताल एवं मातृ-शिशु स्वास्थ्य केंद्र आरंभ"),t("Started by the founder on Kharbi Main Road, Nagpur, with free eye check-ups.","संस्थापक द्वारा खरबी मेन रोड, नागपुर में निःशुल्क नेत्र जाँच के साथ आरंभ।")),
     ("1998",t("Vishvabhartiya Manav Kalyan Sewa Sanstha registered","विश्वभारतीय मानव कल्याण सेवा संस्था पंजीकृत"),t("Reg. No. 15456 (Nagpur) — the earlier organisation through which camps and awareness work were run.","पंजी. सं. 15456 (नागपुर) — पूर्ववर्ती संस्था, जिसके माध्यम से शिविर एवं जागरूकता कार्य हुए।")),
     ("1998–2023",t("Pulse Polio volunteering every year","हर वर्ष पल्स पोलियो सेवा"),t("Support to the Nagpur Municipal Corporation immunisation drive.","नागपुर महानगरपालिका टीकाकरण अभियान में सहयोग।")),
     ("2004",t("HIV/AIDS awareness and personality development","HIV/एड्स जागरूकता एवं व्यक्तित्व विकास"),t("School and college competitions; personality development camp with UNESCO Club, Nagpur.","विद्यालय-महाविद्यालय प्रतियोगिताएँ; यूनेस्को क्लब, नागपुर के साथ व्यक्तित्व विकास शिविर।")),
     ("2005",t("Science and environment fair","विज्ञान एवं पर्यावरण मेला"),t("With Marathi Vigyan Parishad.","मराठी विज्ञान परिषद के साथ।")),
     ("—",t("Leprosy Elimination Action Programme (LEAP)","कुष्ठरोग उन्मूलन कार्य कार्यक्रम (LEAP)"),t("Volunteer training across Bhandara district villages, promoted by ALERT India and supported by ANESVAD Foundation.","भंडारा ज़िले के गाँवों में स्वयंसेवक प्रशिक्षण; ALERT इंडिया द्वारा प्रवर्तित, ANESVAD फाउंडेशन द्वारा समर्थित।")),
    ]
    INST = [
     ("4 Mar 2026",t("ISO 9001:2015 certification","ISO 9001:2015 प्रमाणन"),t("Independent quality-management certification (Royal Assessments Pvt. Ltd.).","स्वतंत्र गुणवत्ता-प्रबंधन प्रमाणन (रॉयल असेसमेंट्स प्रा. लि.)।")),
     ("12 Mar 2026",t("Vishavabhartiya Foundation incorporated","विश्वभारतीय फाउंडेशन की स्थापना"),t("Section 8 not-for-profit company under the Companies Act, 2013 (Licence No. 181714).","कंपनी अधिनियम, 2013 के अंतर्गत Section 8 गैर-लाभकारी कंपनी (लाइसेंस सं. 181714)।")),
     ("14 Mar 2026",t("NGO Darpan, e-Anudaan and Udyam","NGO दर्पण, ई-अनुदान एवं उद्यम"),t("Listed on government NGO portals.","सरकारी NGO पोर्टलों पर पंजीकरण।")),
     ("30 Mar 2026",t("12A and 80G (provisional)","12A एवं 80G (अस्थायी)"),t("Income Tax registration and approval, AY 2026-27 to AY 2028-29.","आयकर पंजीकरण एवं अनुमोदन, निर्धारण वर्ष 2026-27 से 2028-29।")),
     ("7 Apr 2026",t("CSR-1 registration","CSR-1 पंजीकरण"),t("Eligible to implement CSR projects (CSR00109367).","CSR परियोजनाएँ लागू करने हेतु पात्र (CSR00109367)।")),
     ("2026",t("First Foundation programmes","फाउंडेशन के पहले कार्यक्रम"),t("Earth Day (22 April) and International Yoga Day (21 June), covered by the Nagpur press.","पृथ्वी दिवस (22 अप्रैल) एवं अंतर्राष्ट्रीय योग दिवस (21 जून), नागपुर के समाचार-पत्रों में प्रकाशित।")),
    ]
    tl = lambda L: "".join(f'<li><span class="when">{w}</span><b>{a}</b><p>{b}</p></li>' for w,a,b in L)
    body = banner(t("About Us","परिचय"), t("About Vishavabhartiya Foundation","विश्वभारतीय फाउंडेशन के बारे में"), LEGACY()) + f'''
<section><div class="wrap split">
  <div>
    <span class="eyebrow">{t("Who we are","हम कौन हैं")}</span><hr class="rule">
    <h2>{t("From one clinic to a registered foundation","एक क्लिनिक से पंजीकृत फाउंडेशन तक")}</h2>
    <p>{t("Vishavabhartiya Foundation was incorporated on <b>12 March 2026</b> as a not-for-profit company limited by guarantee under Section 8 of the Companies Act, 2013 (Licence No. 181714). Its registered office is at Diamond Nagar, Kharbi Main Road, Nagpur.","विश्वभारतीय फाउंडेशन की स्थापना <b>12 मार्च 2026</b> को कंपनी अधिनियम, 2013 की धारा 8 के अंतर्गत गारंटी द्वारा सीमित गैर-लाभकारी कंपनी के रूप में हुई (लाइसेंस सं. 181714)। इसका पंजीकृत कार्यालय डायमंड नगर, खरबी मेन रोड, नागपुर में है।")}</p>
    <p>{t("It carries forward the work that the founder, Dr. Dhananjay K. Yerne, began in 1998 — a public hospital and mother-and-child health centre, daily free eye check-ups, and, through the earlier organisation Vishvabhartiya Manav Kalyan Sewa Sanstha (Reg. No. 15456), eye camps, polio drives, HIV/AIDS and leprosy awareness and school programmes in Nagpur and Bhandara districts.","यह संस्थापक डॉ. धनंजय के. येरने द्वारा 1998 में शुरू किए गए कार्य को आगे बढ़ाता है — सार्वजनिक अस्पताल एवं मातृ-शिशु स्वास्थ्य केंद्र, प्रतिदिन निःशुल्क नेत्र जाँच, तथा पूर्ववर्ती संस्था विश्वभारतीय मानव कल्याण सेवा संस्था (पंजी. सं. 15456) के माध्यम से नागपुर एवं भंडारा ज़िलों में नेत्र शिविर, पोलियो अभियान, HIV/एड्स एवं कुष्ठरोग जागरूकता तथा विद्यालय कार्यक्रम।")}</p>
    <p>{t("The name joins <span class='deva'>विश्व</span> (the world) and <span class='deva'>भारतीय</span> (Indian). Our emblem carries the motto <span class='deva'>रोगोत्मूलम् दीर्घजीवनम्</span>, “root out disease, live long”, and an eye for the eye care at the heart of our work.","नाम में <span class='deva'>विश्व</span> और <span class='deva'>भारतीय</span> का संगम है। हमारे प्रतीक-चिह्न पर ध्येय-वाक्य <span class='deva'>रोगोत्मूलम् दीर्घजीवनम्</span> अंकित है, और नेत्र का चिह्न हमारे कार्य के केंद्र में नेत्र-सेवा का प्रतीक है।")}</p>
  </div>
  <div class="photo-stack">{IMG("assets/img/gallery/mother-child-centre.webp", t("Maharashtra Public Hospital and Mother-Child Health Care Centre, Nagpur","महाराष्ट्र सार्वजनिक अस्पताल एवं मातृ-शिशु स्वास्थ्य केंद्र, नागपुर"))}
  <div class="badge"><b>1998</b><small>{t("founder's public hospital &amp; mother-child care centre","संस्थापक का सार्वजनिक अस्पताल एवं मातृ-शिशु केंद्र")}</small></div></div>
</div></section>

<section class="alt" id="vision" style="scroll-margin-top:100px"><div class="wrap grid g2">
  <div class="panel" style="border-top:3px solid var(--gold)"><span class="eyebrow">{t("Vision","दृष्टि")}</span>
    <h2 style="font-size:1.7rem">{t("A healthy, educated and self-reliant society","स्वस्थ, शिक्षित एवं आत्मनिर्भर समाज")}</h2>
    <p>{t("where every person, whatever their income or where they live, can see clearly, stay healthy, learn and live with dignity.","जहाँ हर व्यक्ति, आय या निवास-स्थान की परवाह किए बिना, साफ़ देख सके, स्वस्थ रहे, सीख सके और सम्मान से जी सके।")}</p></div>
  <div class="panel" style="border-top:3px solid var(--leaf)"><span class="eyebrow">{t("Mission","मिशन")}</span>
    <h2 style="font-size:1.7rem">{t("Take care to people's doorsteps","सेवा को लोगों के द्वार तक पहुँचाना")}</h2>
    <p>{t("We bring free eye care, health camps and awareness to the communities that need them most, build skills among youth and women, protect the environment, and work with government, CSR partners and citizens transparently.","हम सबसे ज़रूरतमंद समुदायों तक निःशुल्क नेत्र सेवा, स्वास्थ्य शिविर एवं जागरूकता पहुँचाते हैं, युवाओं एवं महिलाओं में कौशल विकसित करते हैं, पर्यावरण की रक्षा करते हैं और सरकार, CSR साझेदारों एवं नागरिकों के साथ पारदर्शिता से काम करते हैं।")}</p></div>
</div></section>

<section id="objectives" style="scroll-margin-top:100px"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Our objectives","हमारे उद्देश्य")}</span><hr class="rule"><h2>{t("What the Foundation is set up to do","फाउंडेशन किन उद्देश्यों के लिए स्थापित है")}</h2>
  <p>{t("Summarised from the objects in our Memorandum of Association.","हमारे मेमोरेंडम ऑफ़ एसोसिएशन में दिए उद्देश्यों का सार।")} <a href="transparency.html">{t("Read the MOA","MOA पढ़ें")}</a></p></div>
  <div class="grid g4">{obj}</div>
</div></section>

<section class="alt" id="journey" style="scroll-margin-top:100px"><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">{t("Our journey","हमारी यात्रा")}</span><hr class="rule"><h2>{t("Two chapters, one purpose","दो अध्याय, एक उद्देश्य")}</h2>
    <p class="muted">{LEGACY()}</p>
    {IMG("assets/img/gallery/pulse-polio-drops.webp", t("Pulse Polio drive","पल्स पोलियो अभियान"), extra=' style="border-radius:var(--r);margin-top:18px"')}
  </div>
  <div>
    <p class="tl-group">{t("Founder &amp; earlier organisation legacy · 1998–2025","संस्थापक एवं पूर्ववर्ती संस्था की विरासत · 1998–2025")}</p>
    <ol class="timeline">{tl(LEG)}</ol>
    <p class="tl-group">{t("Vishavabhartiya Foundation institutional journey · 2026 →","विश्वभारतीय फाउंडेशन की संस्थागत यात्रा · 2026 →")}</p>
    <ol class="timeline inst">{tl(INST)}</ol>
  </div>
</div></section>

<section class="alt" id="partners" style="scroll-margin-top:100px"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Our partners","हमारे साझेदार")}</span><hr class="rule"><h2>{t("Our Partners","हमारे साझेदार")}</h2>
  <p>{t("Organisations we work with now, and those the founder and the earlier Sanstha collaborated with. Listing here shows collaboration on the programme named, not endorsement.","वे संस्थाएँ जिनके साथ हम अभी काम करते हैं, और जिनके साथ संस्थापक एवं पूर्ववर्ती संस्था ने सहयोग किया। यहाँ नाम होना उल्लिखित कार्यक्रम में सहयोग दर्शाता है, समर्थन नहीं।")}</p></div>
  <div class="plogos" data-render="logo-strip"></div>
  <div class="cat-head"><h3>{t("Partners &amp; collaborators of the Foundation","फाउंडेशन के साझेदार एवं सहयोगी")}</h3><span>2026 →</span></div>
  <div class="orgs" data-render="orgs-current"></div>
  <div class="cat-head"><h3>{t("Earlier collaborations (founder &amp; earlier Sanstha)","पूर्व सहयोग (संस्थापक एवं पूर्ववर्ती संस्था)")}</h3><span>1998–2025</span></div>
  <div class="orgs" data-render="orgs-legacy"></div>
  <p class="muted small mt">{t("Would you like to partner with us?","क्या आप हमारे साथ साझेदारी करना चाहते हैं?")} <a href="csr.html">{t("CSR Partnerships","CSR साझेदारी")}</a> · <a href="contact.html">{t("Contact us","संपर्क करें")}</a></p>
</div></section>

<section id="team" style="scroll-margin-top:100px"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Our team","हमारी टीम")}</span><hr class="rule"><h2>{t("Board of Directors","निदेशक मंडल")}</h2><p>{t("The Foundation is governed by a three-member Board of Directors.","फाउंडेशन का संचालन तीन सदस्यीय निदेशक मंडल द्वारा किया जाता है।")}</p></div>
  <div class="founder">
    {IMG("assets/img/team/dhananjay-yerne.webp", t("Dr. Dhananjay Kewalram Yerne","डॉ. धनंजय केवलराम येरने"))}
    <div>
      <h3 style="font-size:1.8rem;margin-bottom:2px">{t("Dr. Dhananjay Kewalram Yerne","डॉ. धनंजय केवलराम येरने")}</h3>
      <p style="color:var(--gold);font-weight:600">{t("Managing Director &amp; CEO · Founder","प्रबंध निदेशक एवं सीईओ · संस्थापक")}</p>
      <blockquote>{t("“A service to man is a service to God.”","“मानव सेवा ही ईश्वर सेवा है।”")}</blockquote>
      <p>{t("An optometrist and vision therapist (M.Sc. Optometry &amp; Ophthalmic Technology, Mewar University; D.O.T., Nagpur, 1995), Dr. Yerne has run free eye check-ups since 1998 at Maharashtra Hospital &amp; Optical, Nagpur. He founded Vishvabhartiya Manav Kalyan Sewa Sanstha and led camps in slums, villages, schools, jails and highway transport hubs.","ऑप्टोमेट्रिस्ट एवं विज़न थेरेपिस्ट (एम.एससी. ऑप्टोमेट्री एवं ऑफ़्थैल्मिक टेक्नोलॉजी, मेवाड़ विश्वविद्यालय; डी.ओ.टी., नागपुर, 1995) डॉ. येरने 1998 से महाराष्ट्र हॉस्पिटल एवं ऑप्टिकल, नागपुर में निःशुल्क नेत्र जाँच कर रहे हैं। उन्होंने विश्वभारतीय मानव कल्याण सेवा संस्था की स्थापना की और बस्तियों, गाँवों, विद्यालयों, कारागृहों एवं राजमार्ग परिवहन केंद्रों में शिविरों का नेतृत्व किया।")}</p>
      <p>{t("He is a life member of the Indian Optometric Association (LM-IOA/3481/2025) and has written public-awareness articles on eye health in the Navbharat newspaper. His personal honours are listed under <a href='impact.html#honours'>Founder's Honours &amp; Recognition</a>.","वे इंडियन ऑप्टोमेट्रिक एसोसिएशन के आजीवन सदस्य (LM-IOA/3481/2025) हैं और नवभारत समाचार-पत्र में नेत्र स्वास्थ्य पर जन-जागरूकता लेख लिख चुके हैं। उनके व्यक्तिगत सम्मान <a href='impact.html#honours'>संस्थापक के सम्मान एवं मान्यता</a> में दिए गए हैं।")}</p>
    </div>
  </div>
  <div class="grid g3 mt">
    {BOARD_CARDS()}
    <div class="person"><div class="initials" aria-hidden="true">+</div><div class="body"><h3>{t("Volunteers &amp; associates","स्वयंसेवक एवं सहयोगी")}</h3><span class="role">{t("Our strength","हमारी शक्ति")}</span><p>{t("Doctors, students and citizens who join our camps and drives, including Dr. Dhanashri Dhobale, Yogesh Raut, Shivani Kadam, Roshani Chauhan and Shreya Dandekar.","हमारे शिविरों एवं अभियानों में जुड़ने वाले चिकित्सक, विद्यार्थी एवं नागरिक, जिनमें डॉ. धनश्री ढोबले, योगेश राऊत, शिवानी कदम, रोशनी चौहान और श्रेया दांडेकर शामिल हैं।")}</p><p><a href="contact.html#volunteer">{t("Become a volunteer →","स्वयंसेवक बनें →")}</a></p></div></div>
  </div>
</div></section>
{CTA()}'''
    page("about.html", t("About Us, Vision, Mission &amp; Team","परिचय, दृष्टि, मिशन एवं टीम"),
         t("About Vishavabhartiya Foundation, Nagpur (est. 12 March 2026): founder's legacy since 1998, vision, mission, objectives, milestones and Board of Directors.",
           "विश्वभारतीय फाउंडेशन, नागपुर (स्थापना 12 मार्च 2026): 1998 से संस्थापक की विरासत, दृष्टि, मिशन, उद्देश्य, उपलब्धियाँ एवं निदेशक मंडल।"), body)

def chapter(id_, flip, eyebrow, h2, intro, bullets, tags, planned, imgs):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    tg = "".join(f'<span class="tag">{x}</span>' for x in tags) + "".join(f'<span class="tag planned">{t("Planned","प्रस्तावित")}: {x}</span>' for x in planned)
    m = IMG(imgs[0][0], imgs[0][1], cap=imgs[0][1])
    if len(imgs) > 1: m += '<div class="pair">' + "".join(IMG(s, a, cap=a) for s, a in imgs[1:3]) + '</div>'
    return f'''<article class="chapter{' flip' if flip else ''}" id="{id_}">
  <div class="ch-media">{m}</div>
  <div class="ch-body"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p>{intro}</p><ul>{lis}</ul><div>{tg}</div></div>
</article>'''

def build_programs():
    G = "assets/img/gallery/"
    body = banner(t("Programmes","कार्यक्रम"), t("Focus Areas &amp; Programmes","कार्यक्षेत्र एवं कार्यक्रम"), t("Health and eye care at the centre, with education, women's empowerment, environment and awareness around it.","केंद्र में स्वास्थ्य एवं नेत्र सेवा, और उसके साथ शिक्षा, महिला सशक्तिकरण, पर्यावरण एवं जागरूकता।")) + f'''
<section class="tight"><div class="wrap">
  <div class="note info" style="margin-bottom:28px">{t("Activities dated before March 2026 were carried out by the founder and the earlier organisation, Vishvabhartiya Manav Kalyan Sewa Sanstha. Vishavabhartiya Foundation (incorporated 12 March 2026) carries this work forward.","मार्च 2026 से पहले की गतिविधियाँ संस्थापक एवं पूर्ववर्ती संस्था विश्वभारतीय मानव कल्याण सेवा संस्था द्वारा की गई थीं। विश्वभारतीय फाउंडेशन (स्थापना 12 मार्च 2026) इस कार्य को आगे बढ़ा रहा है।")}</div>
  <div class="grid g3">{focus_cards()}</div></div></section>
<section style="padding-top:0"><div class="wrap">
''' + chapter("health", False, t("Health &amp; Eye Care","स्वास्थ्य एवं नेत्र सेवा"), t("Free eye check-ups — a legacy since 1998","निःशुल्क नेत्र जाँच — 1998 से चली आ रही विरासत"),
  t("The longest-running work of our founder and the earlier Sanstha, and now the Foundation's core programme. Free screening is held at the founder's eye-care centre in Nagpur and at camps wherever people gather, with spectacles for those who cannot afford them.",
    "संस्थापक एवं पूर्ववर्ती संस्था का सबसे पुराना कार्य, जो अब फाउंडेशन का मुख्य कार्यक्रम है। नागपुर स्थित संस्थापक के नेत्र-सेवा केंद्र और जहाँ लोग एकत्र होते हैं वहाँ शिविरों में निःशुल्क जाँच होती है, और ज़रूरतमंदों को चश्मे दिए जाते हैं।"),
  [t("Free eye check-up camps and spectacle distribution in slums, labour colonies and villages","झुग्गी-बस्तियों, मज़दूर कॉलोनियों एवं गाँवों में निःशुल्क नेत्र जाँच शिविर एवं चश्मा वितरण"),
   t("Camps at schools, colleges, anganwadis, gram panchayats and community halls","विद्यालयों, महाविद्यालयों, आंगनवाड़ियों, ग्राम पंचायतों एवं समाज भवनों में शिविर"),
   t("Camps at temples, Buddha viharas, gurudwaras, mosques and churches, open to all","मंदिरों, बुद्ध विहारों, गुरुद्वारों, मस्जिदों एवं चर्चों में सबके लिए खुले शिविर"),
   t("Eye care for inmates at Nagpur Central Jail","नागपुर केंद्रीय कारागृह के बंदियों के लिए नेत्र सेवा"),
   t("Screening for truck, taxi and bus drivers at highway petrol pumps","राजमार्ग पेट्रोल पंपों पर ट्रक, टैक्सी एवं बस चालकों की जाँच"),
   t("Mobile eye clinic van outreach to villages, towns and urban pockets","गाँवों, कस्बों एवं शहरी बस्तियों तक मोबाइल नेत्र क्लिनिक वैन से सेवा"),
   t("Identification and counselling of cataract patients, with referral for surgery","मोतियाबिंद मरीज़ों की पहचान एवं परामर्श, शल्य-क्रिया हेतु रेफ़रल"),
   t("General health check-up and blood donation camps","सामान्य स्वास्थ्य जाँच एवं रक्तदान शिविर"),
   t("Pulse Polio volunteering with Nagpur Municipal Corporation, 1998–2023 (legacy)","नागपुर महानगरपालिका के साथ पल्स पोलियो सेवा, 1998–2023 (विरासत)"),
   t("International Yoga Day 2026 (Foundation programme)","अंतर्राष्ट्रीय योग दिवस 2026 (फाउंडेशन कार्यक्रम)")],
  [t("Eye care","नेत्र सेवा"),t("Health camps","स्वास्थ्य शिविर"),t("Immunisation","टीकाकरण"),t("Yoga","योग")], [t("eye bank and specialised eye hospital","नेत्र बैंक एवं विशेष नेत्र अस्पताल")],
  [(G+"eye-camp-screening.webp",t("Eye screening at a mega eye camp","भव्य नेत्र शिविर में जाँच")),(G+"eye-camp-team.webp",t("Eye camp team","नेत्र शिविर टीम")),(G+"pulse-polio-drops.webp",t("Pulse Polio drops","पल्स पोलियो खुराक"))]) + \
 chapter("education", True, t("Education &amp; Skill Development","शिक्षा एवं कौशल विकास"), t("Building confidence in young people","युवाओं में आत्मविश्वास का निर्माण"),
  t("Work with schools and colleges so that students learn about health, science and citizenship, and get a chance to be recognised.","विद्यालयों एवं महाविद्यालयों के साथ कार्य, ताकि विद्यार्थी स्वास्थ्य, विज्ञान एवं नागरिकता के बारे में सीखें और उन्हें पहचान मिले।"),
  [t("Essay and drawing competitions with prizes and certificates (legacy)","पुरस्कार एवं प्रमाणपत्र के साथ निबंध एवं चित्रकला प्रतियोगिताएँ (विरासत)"),
   t("Personality development camp with UNESCO Club, Nagpur (2004)","यूनेस्को क्लब, नागपुर के साथ व्यक्तित्व विकास शिविर (2004)"),
   t("Science and environment fair with Marathi Vigyan Parishad (2005)","मराठी विज्ञान परिषद के साथ विज्ञान एवं पर्यावरण मेला (2005)"),
   t("Awareness sessions in schools on health, hygiene and the environment","विद्यालयों में स्वास्थ्य, स्वच्छता एवं पर्यावरण पर जागरूकता सत्र"),
   t("Felicitation of students and young volunteers","विद्यार्थियों एवं युवा स्वयंसेवकों का सम्मान")],
  [t("Schools","विद्यालय"),t("Competitions","प्रतियोगिताएँ"),t("Youth","युवा")], [t("vocational and computer skills training for youth","युवाओं के लिए व्यावसायिक एवं कंप्यूटर कौशल प्रशिक्षण")],
  [(G+"school-awareness-programme.webp",t("School awareness programme","विद्यालय जागरूकता कार्यक्रम")),(G+"prize-distribution.webp",t("Prize distribution","पुरस्कार वितरण")),(G+"students-felicitation.webp",t("Student felicitation","विद्यार्थी सम्मान"))]) + \
 chapter("women", False, t("Women Empowerment","महिला सशक्तिकरण"), t("Healthy mothers, confident women","स्वस्थ माताएँ, आत्मविश्वासी महिलाएँ"),
  t("The founder's work began with a mother-and-child health care centre in 1998. The Foundation continues women's health and empowerment programmes and plans livelihood support.","संस्थापक का कार्य 1998 में मातृ-शिशु स्वास्थ्य केंद्र से शुरू हुआ। फाउंडेशन महिला स्वास्थ्य एवं सशक्तिकरण कार्यक्रम जारी रखे हुए है और आजीविका सहायता की योजना बना रहा है।"),
  [t("Maharashtra Public Hospital &amp; Mother and Child Health Care Centre (opened 1 May 1998)","महाराष्ट्र सार्वजनिक अस्पताल एवं मातृ-शिशु स्वास्थ्य केंद्र (1 मई 1998 को आरंभ)"),
   t("Women's health check-up and awareness camps","महिला स्वास्थ्य जाँच एवं जागरूकता शिविर"),
   t("Women empowerment programmes with local groups","स्थानीय समूहों के साथ महिला सशक्तिकरण कार्यक्रम"),
   t("Women volunteers leading community programmes","सामुदायिक कार्यक्रमों का नेतृत्व करती महिला स्वयंसेविकाएँ")],
  [t("Maternal health","मातृ स्वास्थ्य"),t("Women's health","महिला स्वास्थ्य")], [t("self-help groups and livelihood training","स्वयं सहायता समूह एवं आजीविका प्रशिक्षण")],
  [(G+"mother-child-centre.webp",t("Mother and child health care centre","मातृ-शिशु स्वास्थ्य केंद्र"))]) + \
 chapter("environment", True, t("Environment &amp; Plantation","पर्यावरण एवं वृक्षारोपण"), t("If the Earth is not saved, nothing will remain","धरा नहीं बची तो सब धरा रह जाएगा"),
  t("Our MD &amp; CEO's Earth Day message sums up the programme: small steps, taken together, every day.","हमारे एमडी एवं सीईओ का पृथ्वी दिवस संदेश इस कार्यक्रम का सार है: छोटे-छोटे कदम, मिलकर, हर दिन।"),
  [t("Tree plantation drives","वृक्षारोपण अभियान"),
   t("Cleanliness drives under Swachhata Abhiyan on 2 October","2 अक्टूबर को स्वच्छता अभियान"),
   t("Earth Day programme, 22 April 2026 (Foundation programme)","पृथ्वी दिवस कार्यक्रम, 22 अप्रैल 2026 (फाउंडेशन कार्यक्रम)"),
   t("Pledges to reduce single-use plastic","एकल-उपयोग प्लास्टिक कम करने का संकल्प")],
  [t("Plantation","वृक्षारोपण"),t("Cleanliness","स्वच्छता"),t("Plastic-free","प्लास्टिक-मुक्त")], [t("school eco-clubs and a sapling survival tracker","विद्यालय इको-क्लब एवं पौधों की जीवितता का रिकॉर्ड")],
  [(G+"earth-day-2026.webp",t("Earth Day 2026 programme","पृथ्वी दिवस 2026 कार्यक्रम"))]) + \
 chapter("awareness", False, t("Social Awareness &amp; Community Development","सामाजिक जागरूकता एवं सामुदायिक विकास"), t("Awareness in the language people speak","लोगों की अपनी भाषा में जागरूकता"),
  t("Talks at temples, schools, farms, bus stands and under village trees, using hoardings, competitions and local language.","मंदिरों, विद्यालयों, खेतों, बस स्टैंडों और गाँव के पेड़ों के नीचे — होर्डिंग, प्रतियोगिताओं एवं स्थानीय भाषा के माध्यम से संवाद।"),
  [t("HIV/AIDS awareness with government programmes (2004)","सरकारी कार्यक्रमों के साथ HIV/एड्स जागरूकता (2004)"),
   t("Leprosy Elimination Action Programme (LEAP) in Bhandara district villages, promoted by ALERT India and supported by ANESVAD Foundation","भंडारा ज़िले के गाँवों में कुष्ठरोग उन्मूलन कार्य कार्यक्रम (LEAP), ALERT इंडिया द्वारा प्रवर्तित एवं ANESVAD फाउंडेशन द्वारा समर्थित"),
   t("Tobacco awareness campaigns","तंबाकू जागरूकता अभियान"),
   t("Voter enrolment awareness camps in East Nagpur","पूर्व नागपुर में मतदाता पंजीयन जागरूकता शिविर"),
   t("Campaign for city bus services to outskirts and labour colonies","बाहरी बस्तियों एवं मज़दूर कॉलोनियों तक सिटी बस सेवा हेतु अभियान"),
   t("Gandhi Jayanti and Lal Bahadur Shastri Jayanti observed with free eye camps","गांधी जयंती एवं लाल बहादुर शास्त्री जयंती पर निःशुल्क नेत्र शिविर"),
   t("Public-awareness articles on eye health in the Navbharat newspaper","नवभारत समाचार-पत्र में नेत्र स्वास्थ्य पर जन-जागरूकता लेख")],
  [t("Health awareness","स्वास्थ्य जागरूकता"),t("Civic awareness","नागरिक जागरूकता"),t("Rural outreach","ग्रामीण पहुँच")], [],
  [(G+"awareness-session-children.webp",t("Awareness session for children","बच्चों के लिए जागरूकता सत्र")),(G+"community-event-lamp.webp",t("Community programme","सामुदायिक कार्यक्रम")),(G+"pulse-polio-booth.webp",t("Pulse Polio booth","पल्स पोलियो बूथ"))]) + f'''
</div></section>
{CTA()}'''
    page("programs.html", t("Programmes: Health, Eye Care, Education, Women &amp; Environment","कार्यक्रम: स्वास्थ्य, नेत्र सेवा, शिक्षा, महिला एवं पर्यावरण"),
         t("Programmes of Vishavabhartiya Foundation, Nagpur: free eye check-ups, health camps, education, skill development, women empowerment, plantation and social awareness.",
           "विश्वभारतीय फाउंडेशन, नागपुर के कार्यक्रम: निःशुल्क नेत्र जाँच, स्वास्थ्य शिविर, शिक्षा, कौशल विकास, महिला सशक्तिकरण, वृक्षारोपण एवं सामाजिक जागरूकता।"), body)

def build_impact():
    body = banner(t("Impact &amp; Awards","प्रभाव एवं सम्मान"), t("Our Impact, Achievements &amp; Honours","हमारा प्रभाव, उपलब्धियाँ एवं सम्मान"), t("Founder's legacy since 1998, the Foundation's institutional milestones since 2026, and the recognition received — each shown in its own category.","1998 से संस्थापक की विरासत, 2026 से फाउंडेशन की संस्थागत उपलब्धियाँ, और प्राप्त मान्यताएँ — प्रत्येक अपनी अलग श्रेणी में।")) + f'''
<section class="dark"><div class="wrap">
  {STATS()}
  <p class="stats-note">{t("Beneficiary numbers (people screened, spectacles given, trees planted) are being compiled from camp registers and will be published in the Foundation's first annual report. The award count includes only awards and honours; participation and training certificates are listed separately below.","लाभार्थियों की संख्या (जाँचे गए लोग, वितरित चश्मे, लगाए गए पेड़) शिविर रजिस्टरों से संकलित की जा रही है और फाउंडेशन की पहली वार्षिक रिपोर्ट में प्रकाशित होगी। पुरस्कार संख्या में केवल पुरस्कार एवं सम्मान शामिल हैं; सहभागिता एवं प्रशिक्षण प्रमाणपत्र नीचे अलग दिए गए हैं।")}</p>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Reach","पहुँच")}</span><hr class="rule"><h2>{t("Who the work reaches","यह कार्य किन तक पहुँचता है")}</h2></div>
  <div class="grid g4">
    <div class="focus"><span class="ic">{ico("users")}</span><h3>{t("Urban poor","शहरी गरीब")}</h3><p>{t("Slum settlements and labour colonies of Nagpur.","नागपुर की झुग्गी-बस्तियाँ एवं मज़दूर कॉलोनियाँ।")}</p></div>
    <div class="focus"><span class="ic">{ico("leaf")}</span><h3>{t("Rural families","ग्रामीण परिवार")}</h3><p>{t("Farmers and villagers in Nagpur and Bhandara districts.","नागपुर एवं भंडारा ज़िलों के किसान एवं ग्रामीण।")}</p></div>
    <div class="focus"><span class="ic">{ico("book")}</span><h3>{t("Students","विद्यार्थी")}</h3><p>{t("Zilla Parishad schools, colleges and anganwadis.","ज़िला परिषद विद्यालय, महाविद्यालय एवं आंगनवाड़ियाँ।")}</p></div>
    <div class="focus"><span class="ic">{ico("heart")}</span><h3>{t("Often forgotten","जिन्हें अक्सर भुला दिया जाता है")}</h3><p>{t("Prison inmates, highway drivers, the elderly and differently-abled.","कारागृह के बंदी, राजमार्ग चालक, बुज़ुर्ग एवं दिव्यांगजन।")}</p></div>
  </div>
</div></section>

<section class="alt" id="honours" style="scroll-margin-top:100px"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Founder's Honours &amp; Recognition","संस्थापक के सम्मान एवं मान्यता")}</span><hr class="rule"><h2>{t("Personal honours of Dr. Dhananjay K. Yerne","डॉ. धनंजय के. येरने के व्यक्तिगत सम्मान")}</h2>
  <p>{t("These are personal honours of the founder for his social work since 1998. They are not awards to the Foundation as an institution. Click any certificate to view it.","ये 1998 से सामाजिक कार्य हेतु संस्थापक को प्राप्त व्यक्तिगत सम्मान हैं, फाउंडेशन को संस्था के रूप में दिए गए पुरस्कार नहीं। प्रमाणपत्र देखने के लिए क्लिक करें।")}</p></div>
  <div class="cat-head"><h3>{t("Awards &amp; Honours","पुरस्कार एवं सम्मान")}</h3><span>(<span data-count="honours">3</span>)</span></div>
  <div class="grid g2" data-render="honours"></div>
  <div class="cat-head"><h3>{t("Professional Recognition","व्यावसायिक मान्यता")}</h3><span>{t("participation certificate — not counted as an award","सहभागिता प्रमाणपत्र — पुरस्कार में नहीं गिना गया")}</span></div>
  <div class="grid g2" data-render="recognition"></div>
  <div class="cat-head"><h3>{t("Capacity Building / Training","क्षमता निर्माण / प्रशिक्षण")}</h3><span>{t("training certificate — not counted as an award","प्रशिक्षण प्रमाणपत्र — पुरस्कार में नहीं गिना गया")}</span></div>
  <div class="grid g2" data-render="training"></div>
</div></section>

<section id="achievements" style="scroll-margin-top:100px"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Foundation Achievements &amp; Certifications","फाउंडेशन की उपलब्धियाँ एवं प्रमाणन")}</span><hr class="rule"><h2>{t("Institutional milestones since 12 March 2026","12 मार्च 2026 से संस्थागत उपलब्धियाँ")}</h2></div>
  <ul class="tlist">{"".join(f'<li><span><b>{a}</b><br><span class="small muted">{b}</span></span><span class="st ok">{d}</span></li>' for g,a,b,c,d,img,pdf in REGS())}</ul>
  <p class="mt"><a class="btn btn-line" href="registrations.html">{t("View documents","दस्तावेज़ देखें")}</a></p>
</div></section>

<section class="alt" id="collaborations" style="scroll-margin-top:100px"><div class="wrap">
  <div class="partner-box">
    <div class="sec-head" style="margin-bottom:24px"><span class="eyebrow" style="color:var(--sky)">{t("Partner Field Activities","साझेदार संस्था की गतिविधियाँ")}</span><h2>{t("Programmes of a partner organisation","साझेदार संस्था के कार्यक्रम")}</h2>
    <p>{t("These photos show field work of partner organisation <b>Yuva Kaushal Vikas Mandal (YKVM)</b> in Hamirpur and Banda districts, Uttar Pradesh, for which our team provided online support. They are not direct implementation by Vishavabhartiya Foundation and are not counted in our impact figures.","ये फ़ोटो साझेदार संस्था <b>युवा कौशल विकास मण्डल (YKVM)</b> के हमीरपुर एवं बांदा ज़िलों, उत्तर प्रदेश के फ़ील्ड कार्य की हैं, जिनमें हमारी टीम ने ऑनलाइन सहयोग दिया। ये विश्वभारतीय फाउंडेशन द्वारा प्रत्यक्ष रूप से लागू किए गए कार्य नहीं हैं और हमारे प्रभाव-आँकड़ों में शामिल नहीं हैं।")}</p></div>
    <div class="gallery partner" data-render="partners"></div>
  </div>
</div></section>

<section id="activities" style="scroll-margin-top:100px"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Activities &amp; updates","गतिविधियाँ एवं अपडेट")}</span><hr class="rule"><h2>{t("Recent activities","हाल की गतिविधियाँ")}</h2></div>
  <div class="grid g3" data-render="activities"></div>
</div></section>
{CTA()}'''
    page("impact.html", t("Our Impact, Achievements &amp; Honours","हमारा प्रभाव, उपलब्धियाँ एवं सम्मान"),
         t("Impact of Vishavabhartiya Foundation and its founder's legacy since 1998; founder's honours, Foundation certifications, partner activities and recent updates.",
           "विश्वभारतीय फाउंडेशन का प्रभाव एवं 1998 से संस्थापक की विरासत; संस्थापक के सम्मान, फाउंडेशन प्रमाणन, साझेदार गतिविधियाँ एवं नवीनतम अपडेट।"), body)

def build_media():
    body = banner(t("Media","मीडिया"), t("Media Coverage","मीडिया कवरेज"), t("Our programmes as reported by the Nagpur press, from recent Foundation events to archive clippings of the founder's earlier work.","नागपुर के समाचार-पत्रों में हमारे कार्यक्रम — फाउंडेशन के हाल के आयोजनों से लेकर संस्थापक के पूर्व कार्य की पुरानी कतरनों तक।")) + f'''
<section><div class="wrap">
  <div class="grid g3" data-render="media"></div>
  <p class="muted small mt">{t("Clippings marked “archive” relate to the founder and the earlier Sanstha (before 2026). Click a clipping to read it. Journalists may write to","“पुराना संग्रह” वाली कतरनें संस्थापक एवं पूर्ववर्ती संस्था (2026 से पहले) से संबंधित हैं। पढ़ने के लिए कतरन पर क्लिक करें। पत्रकार संपर्क करें:")} {EM("info")}.</p>
</div></section>''' + CTA()
    page("media.html", t("Media Coverage &amp; News","मीडिया कवरेज एवं समाचार"),
         t("Newspaper coverage of Vishavabhartiya Foundation, Nagpur, and archive coverage of the founder's work: The Hitavada, Lokmat, Dainik Bhaskar and more.",
           "विश्वभारतीय फाउंडेशन, नागपुर का समाचार कवरेज एवं संस्थापक के कार्य की पुरानी कतरनें: द हितवाद, लोकमत, दैनिक भास्कर आदि।"), body)

def build_gallery():
    body = banner(t("Gallery","गैलरी"), t("Photo Gallery","फ़ोटो गैलरी"), t("Real photographs, clearly labelled: Foundation activities, the founder's legacy work, and — separately — partner field activities.","वास्तविक फ़ोटो, स्पष्ट लेबल के साथ: फाउंडेशन की गतिविधियाँ, संस्थापक की विरासत, और — अलग से — साझेदार संस्था की गतिविधियाँ।")) + f'''
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Foundation Programmes","फाउंडेशन कार्यक्रम")}</span><hr class="rule"><h2>{t("Foundation &amp; founder's legacy","फाउंडेशन एवं संस्थापक की विरासत")}</h2></div>
  <div class="filters" role="group" aria-label="{t("Filter photos","फ़ोटो छाँटें")}" data-target="g-main">
    <button type="button" data-f="all" aria-pressed="true">{t("All","सभी")}</button>
    <button type="button" data-f="foundation" aria-pressed="false">{t("Foundation activity (2026)","फाउंडेशन गतिविधि (2026)")}</button>
    <button type="button" data-f="legacy" aria-pressed="false">{t("Founder's legacy","संस्थापक की विरासत")}</button>
    <button type="button" data-f="honour" aria-pressed="false">{t("Founder's honours","संस्थापक सम्मान")}</button>
    <button type="button" data-f="health" aria-pressed="false">{t("Health &amp; eye care","स्वास्थ्य एवं नेत्र")}</button>
    <button type="button" data-f="education" aria-pressed="false">{t("Education","शिक्षा")}</button>
    <button type="button" data-f="women" aria-pressed="false">{t("Women &amp; children","महिलाएँ एवं बच्चे")}</button>
    <button type="button" data-f="environment" aria-pressed="false">{t("Environment","पर्यावरण")}</button>
    <button type="button" data-f="community" aria-pressed="false">{t("Community","समुदाय")}</button>
  </div>
  <div class="gallery" id="g-main" data-render="gallery"></div>
</div></section>
<section class="alt" id="partners" style="scroll-margin-top:100px"><div class="wrap"><div class="partner-box">
  <div class="sec-head" style="margin-bottom:24px"><span class="eyebrow" style="color:var(--sky)">{t("Partner Field Activities","साझेदार संस्था की गतिविधियाँ")}</span><h2>{t("Yuva Kaushal Vikas Mandal (YKVM), Uttar Pradesh","युवा कौशल विकास मण्डल (YKVM), उत्तर प्रदेश")}</h2>
  <p>{t("Field work of our partner organisation in Bundelkhand, supported online by our team. Not direct implementation by Vishavabhartiya Foundation.","बुंदेलखंड में साझेदार संस्था का फ़ील्ड कार्य, जिसमें हमारी टीम ने ऑनलाइन सहयोग दिया। यह विश्वभारतीय फाउंडेशन का प्रत्यक्ष कार्यान्वयन नहीं है।")}</p></div>
  <div class="gallery partner" data-render="partners"></div>
</div></div></section>'''
    page("gallery.html", t("Photo Gallery","फ़ोटो गैलरी"),
         t("Photo gallery of Vishavabhartiya Foundation: Yoga Day and Earth Day 2026, the founder's eye camps and Pulse Polio drives, and separately labelled partner activities.",
           "विश्वभारतीय फाउंडेशन की फ़ोटो गैलरी: योग दिवस एवं पृथ्वी दिवस 2026, संस्थापक के नेत्र शिविर एवं पल्स पोलियो अभियान, और अलग से चिह्नित साझेदार गतिविधियाँ।"), body)

def build_registrations():
    G = REG_GROUPS(); rows = ""; cur = None
    for g,a,b,c,d,img,pdf in REGS():
        if g != cur: rows += f'<tr class="grp"><td colspan="3">{G[g]}</td></tr>'; cur = g
        rows += f'<tr><td><b>{a}</b><br><span class="muted small">{b}</span></td><td class="num">{c}</td><td class="num">{d}</td></tr>'
    docs = ""
    for g,a,b,c,d,img,pdf in REGS():
        pic = IMG(f"assets/img/docs/{img}.webp", a, cap=f"{a} — {c}") if img else f'<div style="aspect-ratio:3/4;display:grid;place-items:center;background:var(--cream);border-radius:6px;color:var(--umber)">{ico("file")}</div>'
        dl = f'<a class="dl" href="{R()}assets/docs/{pdf}" target="_blank" rel="noopener">{t("Open PDF","PDF खोलें")} →</a>' if pdf else ""
        docs += f'<div class="doc">{pic}<b>{a}</b><small>{c}</small>{dl}</div>'
    body = banner(t("Registrations","पंजीकरण"), t("Registrations &amp; Certifications","पंजीकरण एवं प्रमाणन"), t("11 key registrations and certifications, grouped by type, with the documents to check.","11 प्रमुख पंजीकरण एवं प्रमाणन, प्रकार के अनुसार, जाँच हेतु दस्तावेज़ों सहित।")) + f'''
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Legal status","वैधानिक स्थिति")}</span><hr class="rule"><h2>{t("Registration ledger","पंजीकरण विवरण")}</h2>
  <p>{t("Vishavabhartiya Foundation is a not-for-profit company limited by guarantee, licensed under Section 8 of the Companies Act, 2013. Its income is applied only to its objects, and no dividend is paid to members. ISO 9001:2015 is an independent (non-government) certification.","विश्वभारतीय फाउंडेशन कंपनी अधिनियम, 2013 की धारा 8 के अंतर्गत लाइसेंस प्राप्त, गारंटी द्वारा सीमित गैर-लाभकारी कंपनी है। इसकी आय केवल इसके उद्देश्यों पर लगाई जाती है और सदस्यों को कोई लाभांश नहीं दिया जाता। ISO 9001:2015 एक स्वतंत्र (गैर-सरकारी) प्रमाणन है।")}</p></div>
  <div class="table-scroll"><table class="ledger">
    <thead><tr><th>{t("Registration","पंजीकरण")}</th><th>{t("Number / validity","संख्या / वैधता")}</th><th>{t("Date","दिनांक")}</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="muted small mt">{t("Verify company details on","कंपनी विवरण सत्यापित करें:")} <a href="https://www.mca.gov.in" target="_blank" rel="noopener">mca.gov.in</a> · {t("NGO Darpan:","NGO दर्पण:")} <a href="https://ngodarpan.gov.in" target="_blank" rel="noopener">ngodarpan.gov.in</a>. {t("FCRA: not registered; donations are accepted from Indian sources only.","FCRA: पंजीकृत नहीं; केवल भारतीय स्रोतों से दान स्वीकार किया जाता है।")}</p>
</div></section>
<section class="alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Documents","दस्तावेज़")}</span><hr class="rule"><h2>{t("Certificates","प्रमाणपत्र")}</h2><p>{t("Click an image to enlarge, or open the PDF where available. Certified copies are available to CSR partners and government departments on request.","बड़ा देखने के लिए चित्र पर क्लिक करें या उपलब्ध PDF खोलें। प्रमाणित प्रतियाँ CSR साझेदारों एवं सरकारी विभागों को अनुरोध पर उपलब्ध हैं।")}</p></div>
  <div class="docs">{docs}</div>
</div></section>
{CTA()}'''
    page("registrations.html", t("Registrations &amp; Certifications — Section 8, 12A, 80G, CSR-1, NGO Darpan","पंजीकरण एवं प्रमाणन — Section 8, 12A, 80G, CSR-1, NGO दर्पण"),
         t("Registrations of Vishavabhartiya Foundation: Section 8 CIN and licence, PAN, TAN, Udyam, 12A, 80G, CSR-1 (CSR00109367), NGO Darpan, e-Anudaan and ISO 9001:2015.",
           "विश्वभारतीय फाउंडेशन के पंजीकरण: Section 8 CIN एवं लाइसेंस, PAN, TAN, उद्यम, 12A, 80G, CSR-1 (CSR00109367), NGO दर्पण, ई-अनुदान एवं ISO 9001:2015।"), body)

def kv(label, val, copy=True):
    btn = f'<button class="copy" type="button" data-copy="{val}">{t("Copy","कॉपी")}</button>' if copy else "<span></span>"
    return f'<dt>{label}</dt><dd>{val}</dd>{btn}'

def HP(): return f'<div class="hp" aria-hidden="true"><label for="hp-{LANG}">Leave empty</label><input class="hp-input" id="hp-{LANG}" name="website" tabindex="-1" autocomplete="off"></div>'

def build_donate():
    body = banner(t("Donate","दान करें"), t("Donate / Support Us","दान / सहयोग करें"), t("Your donation supports free eye care, health camps and community programmes. Donations are eligible for tax benefit under Section 80G.","आपका दान निःशुल्क नेत्र सेवा, स्वास्थ्य शिविरों एवं सामुदायिक कार्यक्रमों में सहायक होता है। दान पर धारा 80G के अंतर्गत कर-लाभ उपलब्ध है।")) + f'''
<section><div class="wrap">
  <div class="note warn" style="margin-bottom:24px"><b>{t("Stay safe:","सावधान रहें:")}</b> {t("Vishavabhartiya Foundation never asks for OTP, UPI PIN, ATM PIN or banking passwords. Before making payment, please verify the beneficiary/account name as <b>VISHAVABHARTIYA FOUNDATION</b>.","विश्वभारतीय फाउंडेशन कभी भी OTP, UPI PIN, ATM PIN या बैंकिंग पासवर्ड नहीं माँगता। भुगतान से पहले कृपया लाभार्थी/खाते का नाम <b>VISHAVABHARTIYA FOUNDATION</b> अवश्य जाँच लें।")}</div>
  <div class="donate-grid">
  <div class="panel">
    <h3>{t("Bank transfer (NEFT / RTGS / IMPS)","बैंक ट्रांसफ़र (NEFT / RTGS / IMPS)")}</h3>
    <dl class="kv">
      {kv(t("Account name","खाते का नाम"),"VISHAVABHARTIYA FOUNDATION")}
      {kv(t("Account number","खाता संख्या"),ORG["acc"])}
      {kv(t("Account type","खाते का प्रकार"),t("Current account","चालू खाता"),False)}
      {kv("IFSC",ORG["ifsc"])}
      {kv(t("Bank","बैंक"),t("Punjab National Bank, Nandanwan, Nagpur 440009","पंजाब नेशनल बैंक, नंदनवन, नागपुर 440009"),False)}
    </dl>
    <div class="note mt">{t("<b>Tax benefit:</b> donations are eligible under Section 80G (provisional approval, AY 2026-27 to AY 2028-29) as per the Income Tax Act. Cash donations above ₹2,000 do not qualify for deduction.","<b>कर-लाभ:</b> आयकर अधिनियम के अनुसार दान धारा 80G (अस्थायी अनुमोदन, निर्धारण वर्ष 2026-27 से 2028-29) के अंतर्गत पात्र है। ₹2,000 से अधिक नकद दान पर कटौती नहीं मिलती।")}</div>
  </div>
  <div class="panel qr">
    <h3>{t("Scan &amp; pay with any UPI app","किसी भी UPI ऐप से स्कैन करके भुगतान करें")}</h3>
    {IMG("assets/img/upi-qr.webp", t("UPI QR code for Vishavabhartiya Foundation","विश्वभारतीय फाउंडेशन का UPI QR कोड"))}
    <dl class="kv" style="margin-top:14px;text-align:left">{kv("UPI ID",ORG["upi"])}</dl>
    <p class="muted small" style="margin-top:10px">{t("The app should show the payee name VISHAVABHARTIYA FOUNDATION.","ऐप में प्राप्तकर्ता का नाम VISHAVABHARTIYA FOUNDATION दिखना चाहिए।")}</p>
  </div>
  </div>
  <p class="muted small mt">{t("How donations are used: your donation supports programme delivery — screening, spectacles, camp materials and awareness activities — which can also include necessary administrative, compliance and logistics costs, as permitted by law. Details will be reported in our annual report.","दान का उपयोग: आपका दान कार्यक्रमों — जाँच, चश्मे, शिविर सामग्री एवं जागरूकता गतिविधियों — में सहायक होता है, जिसमें कानून द्वारा अनुमत आवश्यक प्रशासनिक, अनुपालन एवं परिवहन व्यय भी शामिल हो सकते हैं। विवरण हमारी वार्षिक रिपोर्ट में दिया जाएगा।")} <a href="donation-policy.html">{t("Donation &amp; Refund Policy","दान एवं धनवापसी नीति")}</a></p>
</div></section>

<section class="alt" id="receipt" style="scroll-margin-top:100px"><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">{t("80G receipt","80G रसीद")}</span><hr class="rule">
    <h2>{t("Request 80G Donation Receipt","80G दान रसीद का अनुरोध")}</h2>
    <p>{t("After you donate, fill in this form so we can issue your receipt. Your PAN is needed for the receipt and for the donation statement the Foundation files with the Income Tax Department.","दान के बाद यह फ़ॉर्म भरें, ताकि हम आपकी रसीद जारी कर सकें। रसीद और आयकर विभाग में फाउंडेशन द्वारा दाखिल दान-विवरण के लिए आपका PAN आवश्यक है।")}</p>
    <ul class="checks">
      <li>{ico("check")} {t("Keep a screenshot of your payment; we may ask for it to match the transaction.","भुगतान का स्क्रीनशॉट रखें; लेन-देन मिलाने के लिए हम उसे माँग सकते हैं।")}</li>
      <li>{ico("check")} {t("We will never ask for OTP, UPI PIN, ATM PIN or passwords.","हम कभी OTP, UPI PIN, ATM PIN या पासवर्ड नहीं माँगेंगे।")}</li>
      <li>{ico("check")} {t("Questions: ","प्रश्न: ")}{EM("donations")} · {ORG["ph1"]}</li>
    </ul>
  </div>
  <div class="panel">
    <form data-vbf-form="receipt-80g" data-email-role="donations" data-subject="{t("80G receipt request","80G रसीद अनुरोध")}" novalidate>
      {HP()}
      <div class="row">
        <div class="field"><label for="rc-name">{t("Donor name (as per PAN)","दानदाता का नाम (PAN अनुसार)")}</label><input id="rc-name" name="donor_name" autocomplete="name" required></div>
        <div class="field"><label for="rc-pan">PAN</label><input id="rc-pan" name="pan" data-rule="pan" maxlength="10" required placeholder="ABCDE1234F" style="text-transform:uppercase"></div>
      </div>
      <div class="field"><label for="rc-addr">{t("Full address","पूरा पता")}</label><textarea id="rc-addr" name="address" rows="2" autocomplete="street-address" required></textarea></div>
      <div class="row">
        <div class="field"><label for="rc-amt">{t("Donation amount (₹)","दान राशि (₹)")}</label><input id="rc-amt" name="amount" inputmode="decimal" data-rule="amount" required></div>
        <div class="field"><label for="rc-date">{t("Donation date","दान की तिथि")}</label><input id="rc-date" name="donation_date" type="date" required></div>
      </div>
      <div class="row">
        <div class="field"><label for="rc-mode">{t("Payment mode","भुगतान का माध्यम")}</label><select id="rc-mode" name="payment_mode" required><option value="">{t("Select","चुनें")}</option><option>UPI</option><option>NEFT</option><option>RTGS</option><option>IMPS</option><option>{t("Cheque","चेक")}</option><option>{t("Other","अन्य")}</option></select></div>
        <div class="field"><label for="rc-utr">{t("UTR / Transaction ID","UTR / ट्रांज़ैक्शन आईडी")}</label><input id="rc-utr" name="utr" required></div>
      </div>
      <div class="row">
        <div class="field"><label for="rc-email">{t("Email","ईमेल")}</label><input id="rc-email" name="email" type="email" data-rule="email" autocomplete="email" required></div>
        <div class="field"><label for="rc-mob">{t("Mobile number","मोबाइल नंबर")}</label><input id="rc-mob" name="mobile" type="tel" data-rule="mobile" autocomplete="tel" required></div>
      </div>
      <button class="btn btn-gold" type="submit">{t("Submit receipt request","रसीद अनुरोध भेजें")}</button>
      <p class="form-msg" aria-live="polite"></p>
      <p class="muted small">{t("Your details are used only to issue your receipt and meet legal reporting requirements.","आपकी जानकारी केवल रसीद जारी करने एवं वैधानिक रिपोर्टिंग हेतु उपयोग होगी।")} <a href="privacy.html">{t("Privacy policy","गोपनीयता नीति")}</a></p>
    </form>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("What your gift supports","आपका दान किसमें सहायक है")}</span><hr class="rule"><h2>{t("Ways to help","सहयोग के तरीके")}</h2></div>
  <div class="grid g4">
    <div class="focus"><span class="ic">{ico("eye")}</span><h3>{t("Spectacles","चश्मे")}</h3><p>{t("Support spectacles for patients screened at camps.","शिविरों में जाँचे गए मरीज़ों के चश्मों में सहयोग।")}</p></div>
    <div class="focus"><span class="ic">{ico("heart")}</span><h3>{t("A health camp","स्वास्थ्य शिविर")}</h3><p>{t("Support an eye or health check-up camp in a village or slum.","गाँव या बस्ती में नेत्र/स्वास्थ्य जाँच शिविर में सहयोग।")}</p></div>
    <div class="focus"><span class="ic">{ico("leaf")}</span><h3>{t("Saplings","पौधे")}</h3><p>{t("Support plantation drives and the care of young trees.","वृक्षारोपण एवं पौधों की देखभाल में सहयोग।")}</p></div>
    <div class="focus"><span class="ic">{ico("users")}</span><h3>{t("Your time","आपका समय")}</h3><p>{t("Volunteer as a doctor, student, photographer or organiser.","चिकित्सक, विद्यार्थी, फ़ोटोग्राफ़र या आयोजक के रूप में स्वयंसेवा।")}</p></div>
  </div>
</div></section>

<section class="alt" id="csr" style="scroll-margin-top:100px"><div class="wrap split">
  <div><span class="eyebrow">{t("CSR partnership","CSR साझेदारी")}</span><hr class="rule"><h2>{t("Are you a company?","क्या आप एक कंपनी हैं?")}</h2>
  <p>{t("We are registered to implement CSR projects (CSR-1: ","हम CSR परियोजनाएँ लागू करने हेतु पंजीकृत हैं (CSR-1: ")}<span class="mono">{ORG["csr"]}</span>). {t("See thematic areas, methodology and reporting on our CSR page.","विषय-क्षेत्र, कार्य-पद्धति एवं रिपोर्टिंग हमारे CSR पृष्ठ पर देखें।")}</p>
  <a class="btn btn-gold" href="csr.html">{t("CSR Partnerships","CSR साझेदारी")}</a></div>
  <div class="photo-stack">{IMG("assets/img/gallery/eye-camp-team.webp", t("Eye camp team","नेत्र शिविर टीम"))}</div>
</div></section>'''
    page("donate.html", t("Donate / Support Us — 80G Tax Benefit","दान / सहयोग — 80G कर-लाभ"),
         t("Donate to Vishavabhartiya Foundation, Nagpur by UPI or bank transfer, and request your 80G receipt online. Account name: VISHAVABHARTIYA FOUNDATION.",
           "UPI या बैंक ट्रांसफ़र से विश्वभारतीय फाउंडेशन, नागपुर को दान करें और 80G रसीद का ऑनलाइन अनुरोध करें। खाते का नाम: VISHAVABHARTIYA FOUNDATION।"), body)

def build_csr():
    TH = [("eye",t("Health care &amp; sanitation","स्वास्थ्य सेवा एवं स्वच्छता"),t("Eye screening and spectacles, health camps, hygiene awareness.","नेत्र जाँच एवं चश्मे, स्वास्थ्य शिविर, स्वच्छता जागरूकता।"),"Sch. VII (i)"),
          ("book",t("Education &amp; skills","शिक्षा एवं कौशल"),t("School health and awareness programmes, youth skill training.","विद्यालय स्वास्थ्य एवं जागरूकता कार्यक्रम, युवा कौशल प्रशिक्षण।"),"Sch. VII (ii)"),
          ("woman",t("Women empowerment","महिला सशक्तिकरण"),t("Women's health camps, awareness and livelihood support.","महिला स्वास्थ्य शिविर, जागरूकता एवं आजीविका सहायता।"),"Sch. VII (iii)"),
          ("leaf",t("Environmental sustainability","पर्यावरणीय स्थिरता"),t("Plantation with survival tracking, plastic-reduction and cleanliness drives.","जीवितता-रिकॉर्ड सहित वृक्षारोपण, प्लास्टिक-कमी एवं स्वच्छता अभियान।"),"Sch. VII (iv)"),
          ("users",t("Rural development","ग्रामीण विकास"),t("Village outreach camps and awareness in Nagpur and Bhandara districts.","नागपुर एवं भंडारा ज़िलों में ग्रामीण शिविर एवं जागरूकता।"),"Sch. VII (x)")]
    th = "".join(f'<div class="focus"><span class="ic">{ico(i)}</span><h3>{a}</h3><p>{b}</p><span class="small muted">{t("Companies Act 2013,","कंपनी अधिनियम 2013,")} {c}</span></div>' for i,a,b,c in TH)
    PROJ = [(t("Community eye-care &amp; spectacles programme","सामुदायिक नेत्र-सेवा एवं चश्मा कार्यक्रम"),[t("Camps in slums, villages, schools and transport hubs","बस्तियों, गाँवों, विद्यालयों एवं परिवहन केंद्रों में शिविर"),t("Refraction, spectacles, referral for treatment","दृष्टि-जाँच, चश्मे, उपचार हेतु रेफ़रल")]),
            (t("School health &amp; awareness","विद्यालय स्वास्थ्य एवं जागरूकता"),[t("Vision screening of students","विद्यार्थियों की दृष्टि-जाँच"),t("Hygiene, tobacco and environment sessions","स्वच्छता, तंबाकू एवं पर्यावरण सत्र")]),
            (t("Women's health camps","महिला स्वास्थ्य शिविर"),[t("Screening and awareness for women","महिलाओं की जाँच एवं जागरूकता"),t("Linkage to government health schemes","सरकारी स्वास्थ्य योजनाओं से जुड़ाव")]),
            (t("Green neighbourhoods","हरित बस्तियाँ"),[t("Plantation with survival tracking","जीवितता-रिकॉर्ड सहित वृक्षारोपण"),t("Plastic-reduction and cleanliness drives","प्लास्टिक-कमी एवं स्वच्छता अभियान")])]
    proj = "".join(f'<div class="focus"><h3>{a}</h3><ul>{"".join(f"<li>{x}</li>" for x in b)}</ul></div>' for a,b in PROJ)
    KPI = [t("People screened (by age group and gender)","जाँचे गए लोग (आयु-वर्ग एवं लिंग अनुसार)"),t("Spectacles distributed","वितरित चश्मे"),t("Patients referred and treatment completed","रेफ़र किए गए एवं उपचार पूर्ण करने वाले मरीज़"),t("Camps held, by location","स्थान अनुसार आयोजित शिविर"),t("Students and women reached through awareness sessions","जागरूकता सत्रों से जुड़े विद्यार्थी एवं महिलाएँ"),t("Saplings planted and surviving after 12 months","लगाए गए पौधे एवं 12 माह बाद जीवित पौधे")]
    STEPS = [(t("Needs discussion","आवश्यकता पर चर्चा"),t("Understand the partner's priorities, geography and budget.","साझेदार की प्राथमिकताएँ, क्षेत्र एवं बजट समझना।")),
             (t("Proposal &amp; budget","प्रस्ताव एवं बजट"),t("Project proposal with activities, timeline, KPIs and a line-item budget.","गतिविधियों, समय-सीमा, KPI एवं मदवार बजट सहित प्रस्ताव।")),
             (t("MoU &amp; baseline","MoU एवं आधार-रेखा"),t("Sign an MoU; record baseline data in the project area.","MoU पर हस्ताक्षर; परियोजना क्षेत्र में आधार-रेखा आँकड़े दर्ज करना।")),
             (t("Implementation","कार्यान्वयन"),t("Camps and sessions with registers, photographs and attendance records.","रजिस्टर, फ़ोटो एवं उपस्थिति रिकॉर्ड के साथ शिविर एवं सत्र।")),
             (t("Monitoring","निगरानी"),t("Periodic progress reports against agreed KPIs; field visits welcome.","तय KPI के आधार पर नियमित प्रगति रिपोर्ट; फ़ील्ड विज़िट का स्वागत।")),
             (t("Closure &amp; reporting","समापन एवं रिपोर्टिंग"),t("Completion report, utilisation certificate and impact summary.","समापन रिपोर्ट, उपयोगिता प्रमाणपत्र एवं प्रभाव सारांश।"))]
    steps = "".join(f'<li><span class="when">{i+1:02d}</span><b>{a}</b><p>{b}</p></li>' for i,(a,b) in enumerate(STEPS))
    body = banner(t("CSR Partnerships","CSR साझेदारी"), t("CSR Partnerships","CSR साझेदारी"), t("A CSR-registered implementing agency in Nagpur for health, eye care, education, women's empowerment and the environment.","स्वास्थ्य, नेत्र सेवा, शिक्षा, महिला सशक्तिकरण एवं पर्यावरण हेतु नागपुर की CSR-पंजीकृत कार्यान्वयन संस्था।")) + f'''
<section><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">{t("About the Foundation","फाउंडेशन के बारे में")}</span><hr class="rule">
    <h2>{t("Who you would be partnering with","आप किसके साथ साझेदारी करेंगे")}</h2>
    <p>{LEGACY()}</p>
    <p>{t("Governed by a three-member Board of Directors led by Dr. Dhananjay K. Yerne, Managing Director &amp; CEO.","प्रबंध निदेशक एवं सीईओ डॉ. धनंजय के. येरने के नेतृत्व में तीन सदस्यीय निदेशक मंडल द्वारा संचालित।")}</p>
    <p><a class="btn btn-gold" href="contact.html#csr">{t("Partner With Us","हमसे साझेदारी करें")}</a> <a class="btn btn-line" href="contact.html#csr">{t("Discuss a CSR Project","CSR परियोजना पर चर्चा करें")}</a></p>
  </div>
  <div class="panel">
    <h3>{t("CSR registration &amp; eligibility","CSR पंजीकरण एवं पात्रता")}</h3>
    <dl class="kv">
      {kv("CSR-1",ORG["csr"],False)}
      {kv(t("Entity","संस्था का प्रकार"),t("Section 8 company (Licence 181714)","Section 8 कंपनी (लाइसेंस 181714)"),False)}
      {kv("CIN",ORG["cin"],False)}
      {kv("12A / 80G",t("Provisional, AY 2026-27 – 2028-29","अस्थायी, AY 2026-27 – 2028-29"),False)}
      {kv("PAN",ORG["pan"],False)}
      {kv(t("NGO Darpan","NGO दर्पण"),ORG["darpan"],False)}
    </dl>
    <p class="mt"><a href="registrations.html">{t("View all certificates →","सभी प्रमाणपत्र देखें →")}</a></p>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Thematic areas","विषय-क्षेत्र")}</span><hr class="rule"><h2>{t("Aligned with Schedule VII","अनुसूची VII के अनुरूप")}</h2></div>
  <div class="grid g3">{th}</div>
</div></section>

<section><div class="wrap grid g2">
  <div><span class="eyebrow">{t("Geographic reach","भौगोलिक पहुँच")}</span><hr class="rule"><h2 style="font-size:1.6rem">{t("Nagpur and Bhandara districts, Maharashtra","नागपुर एवं भंडारा ज़िले, महाराष्ट्र")}</h2>
  <p>{t("Urban Nagpur (slums, labour colonies, schools) and rural villages of Nagpur and Bhandara districts, where the founder's team has worked since 1998. Other locations can be considered with the partner.","शहरी नागपुर (बस्तियाँ, मज़दूर कॉलोनियाँ, विद्यालय) तथा नागपुर एवं भंडारा ज़िलों के गाँव, जहाँ संस्थापक की टीम 1998 से कार्यरत है। साझेदार के साथ अन्य स्थानों पर भी विचार किया जा सकता है।")}</p></div>
  <div><span class="eyebrow">{t("Target beneficiaries","लक्षित लाभार्थी")}</span><hr class="rule"><h2 style="font-size:1.6rem">{t("People who are hardest to reach","जिन तक पहुँचना सबसे कठिन है")}</h2>
  <ul><li>{t("Low-income urban families and daily-wage labourers","कम आय वाले शहरी परिवार एवं दिहाड़ी मज़दूर")}</li><li>{t("Farmers and rural families","किसान एवं ग्रामीण परिवार")}</li><li>{t("School children and adolescents","स्कूली बच्चे एवं किशोर")}</li><li>{t("Women, the elderly and differently-abled people","महिलाएँ, बुज़ुर्ग एवं दिव्यांगजन")}</li><li>{t("Truck, taxi and bus drivers","ट्रक, टैक्सी एवं बस चालक")}</li></ul></div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Proposed project areas","प्रस्तावित परियोजना क्षेत्र")}</span><hr class="rule"><h2>{t("Where a CSR partnership can start","CSR साझेदारी कहाँ से शुरू हो सकती है")}</h2>
  <p>{t("Indicative project areas based on our existing work. Scope, budget and duration are finalised with each partner after a needs discussion — we do not publish fixed budgets.","हमारे मौजूदा कार्य पर आधारित संकेतात्मक क्षेत्र। दायरा, बजट एवं अवधि हर साझेदार के साथ आवश्यकता-चर्चा के बाद तय होते हैं — हम कोई निश्चित बजट प्रकाशित नहीं करते।")}</p></div>
  <div class="grid g4">{proj}</div>
  <div class="grid g2 mt">
    <div class="panel"><h3>{t("Indicative budget","संकेतात्मक बजट")}</h3><p class="muted">{t("Prepared per project as a line-item budget after the needs discussion and shared with the proposal.","हर परियोजना के लिए आवश्यकता-चर्चा के बाद मदवार बजट बनाकर प्रस्ताव के साथ साझा किया जाता है।")}</p></div>
    <div class="panel"><h3>{t("Project duration","परियोजना अवधि")}</h3><p class="muted">{t("Agreed with each partner in the MoU; can be a single campaign or a multi-month programme.","हर साझेदार के साथ MoU में तय; एकल अभियान या कई महीनों का कार्यक्रम हो सकता है।")}</p></div>
  </div>
</div></section>

<section><div class="wrap split" style="align-items:start">
  <div><span class="eyebrow">{t("Outputs / KPIs","आउटपुट / KPI")}</span><hr class="rule"><h2>{t("What we measure","हम क्या मापते हैं")}</h2>
  <p class="muted">{t("Indicators we propose to track; targets are set per project.","जिन संकेतकों को हम ट्रैक करने का प्रस्ताव रखते हैं; लक्ष्य हर परियोजना के लिए तय होते हैं।")}</p>
  <ul class="checks">{"".join(f"<li>{ico('chart')} {k}</li>" for k in KPI)}</ul></div>
  <div><span class="eyebrow">{t("Implementation methodology","कार्यान्वयन पद्धति")}</span><hr class="rule"><h2>{t("How a project runs","परियोजना कैसे चलती है")}</h2>
  <ol class="timeline inst">{steps}</ol></div>
</div></section>

<section class="alt"><div class="wrap grid g2">
  <div class="panel"><h3>{t("Monitoring &amp; reporting","निगरानी एवं रिपोर्टिंग")}</h3><ul><li>{t("Camp registers and attendance sheets","शिविर रजिस्टर एवं उपस्थिति पत्रक")}</li><li>{t("Periodic progress reports against KPIs","KPI के आधार पर नियमित प्रगति रिपोर्ट")}</li><li>{t("Partner field visits welcome","साझेदार की फ़ील्ड विज़िट का स्वागत")}</li><li>{t("Quality system certified to ISO 9001:2015","ISO 9001:2015 प्रमाणित गुणवत्ता प्रणाली")}</li></ul></div>
  <div class="panel"><h3>{t("Documentation &amp; impact reporting","दस्तावेज़ीकरण एवं प्रभाव रिपोर्टिंग")}</h3><ul><li>{t("Photographs with date and location (with consent)","दिनांक एवं स्थान सहित फ़ोटो (सहमति के साथ)")}</li><li>{t("Utilisation certificate and completion report","उपयोगिता प्रमाणपत्र एवं समापन रिपोर्ट")}</li><li>{t("Impact summary for the partner's CSR report","साझेदार की CSR रिपोर्ट हेतु प्रभाव सारांश")}</li><li>{t("Receipts as applicable","लागू अनुसार रसीदें")}</li></ul></div>
</div></section>

<section><div class="wrap"><div class="cta-band">
  <div><h2>{t("CSR partnership enquiry","CSR साझेदारी हेतु संपर्क")}</h2><p>{t("Tell us your focus area and location. We will respond with a concept note tailored to your priorities. Our organisation profile and registration documents are shared on request.","अपना विषय-क्षेत्र एवं स्थान बताइए। हम आपकी प्राथमिकताओं के अनुसार अवधारणा-पत्र भेजेंगे। संस्था प्रोफ़ाइल एवं पंजीकरण दस्तावेज़ अनुरोध पर साझा किए जाते हैं।")}</p>
  <p class="small" style="margin-top:8px">{t("CSR email:","CSR ईमेल:")} <span style="color:#fff">{EM("csr", link=False)}</span></p></div>
  <div class="ctas"><a class="btn btn-gold" href="contact.html#csr">{t("Discuss a CSR Project","CSR परियोजना पर चर्चा करें")}</a><a class="btn btn-light" href="contact.html#profile">{t("Request Organisation Profile","संस्था प्रोफ़ाइल माँगें")}</a></div>
</div></div></section>'''
    page("csr.html", t("CSR Partnerships — CSR-1 Registered NGO in Nagpur","CSR साझेदारी — नागपुर की CSR-1 पंजीकृत संस्था"),
         t("Partner with Vishavabhartiya Foundation (CSR-1: CSR00109367) on health, eye care, education, women's empowerment and environment projects in Nagpur and Bhandara.",
           "नागपुर एवं भंडारा में स्वास्थ्य, नेत्र सेवा, शिक्षा, महिला सशक्तिकरण एवं पर्यावरण परियोजनाओं के लिए विश्वभारतीय फाउंडेशन (CSR-1: CSR00109367) के साथ साझेदारी करें।"), body)

def build_transparency():
    def row(label, href=None, note=None, internal=False):
        if href:
            tgt = "" if internal else ' target="_blank" rel="noopener"'
            h = href if internal else R() + href
            return f'<li><span>{label}</span><a class="st ok" href="{h}"{tgt}>{t("View","देखें")} →</a></li>'
        return f'<li><span>{label}</span><span class="st na">{note or t("Not yet published","अभी प्रकाशित नहीं")}</span></li>'
    body = banner(t("Transparency","पारदर्शिता"), t("Transparency &amp; Governance","पारदर्शिता एवं शासन"), t("Our constitutional documents, registrations and governance information. Documents are added here as they are adopted or published.","हमारे संवैधानिक दस्तावेज़, पंजीकरण एवं शासन संबंधी जानकारी। दस्तावेज़ अपनाए या प्रकाशित होते ही यहाँ जोड़े जाते हैं।")) + f'''
<section><div class="wrap grid g2">
  <div><h2 style="font-size:1.5rem">{ico("file")} {t("Legal / Corporate","वैधानिक / कॉर्पोरेट")}</h2><ul class="tlist">
    {row(t("Certificate of Incorporation","निगमन प्रमाणपत्र"),"assets/docs/certificate-of-incorporation.pdf")}
    {row(t("Section 8 Licence (No. 181714)","Section 8 लाइसेंस (सं. 181714)"),"assets/docs/section-8-licence.pdf")}
    {row(t("Memorandum of Association (MOA)","मेमोरेंडम ऑफ़ एसोसिएशन (MOA)"),"assets/docs/memorandum-of-association-moa.pdf")}
    {row(t("Articles of Association (AOA)","आर्टिकल्स ऑफ़ एसोसिएशन (AOA)"),"assets/docs/articles-of-association-aoa.pdf")}
    {row(t("12A &amp; 80G provisional approval (Form 10AC)","12A एवं 80G अस्थायी अनुमोदन (फ़ॉर्म 10AC)"),"assets/docs/12a-80g-provisional-approval.pdf")}
    {row(t("All registrations &amp; certificates","सभी पंजीकरण एवं प्रमाणपत्र"),"registrations.html",internal=True)}
  </ul></div>
  <div><h2 style="font-size:1.5rem">{ico("chart")} {t("Financial Transparency","वित्तीय पारदर्शिता")}</h2><ul class="tlist">
    {row(t("Annual Report","वार्षिक रिपोर्ट"), note=t("Not yet published — first financial year in progress","अभी प्रकाशित नहीं — पहला वित्तीय वर्ष जारी"))}
    {row(t("Audited Accounts","अंकेक्षित लेखे"), note=t("Not yet published — first financial year in progress","अभी प्रकाशित नहीं — पहला वित्तीय वर्ष जारी"))}
  </ul>
  <h2 style="font-size:1.5rem;margin-top:28px">{ico("users")} {t("Board / Governance","मंडल / शासन")}</h2><ul class="tlist">
    {row(t("Board of Directors (3 members)","निदेशक मंडल (3 सदस्य)"),"about.html#team",internal=True)}
    {row(t("Grievance mechanism","शिकायत निवारण व्यवस्था"),"grievance.html",internal=True)}
  </ul></div>
</div></section>
<section class="alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t("Policies","नीतियाँ")}</span><hr class="rule"><h2>{t("Policies and statements","नीतियाँ एवं वक्तव्य")}</h2>
  <p>{t("Published statements are linked below. Board policies (CSR, Finance, Procurement, POSH, Safeguarding) will be published here once adopted by the Board.","प्रकाशित वक्तव्य नीचे दिए गए हैं। मंडल की नीतियाँ (CSR, वित्त, क्रय, POSH, सेफ़गार्डिंग) मंडल द्वारा अपनाए जाने के बाद यहाँ प्रकाशित की जाएँगी।")}</p></div>
  <div class="grid g2"><ul class="tlist">
    {row(t("Safeguarding statement","सेफ़गार्डिंग वक्तव्य"),"safeguarding.html",internal=True)}
    {row(t("Donation &amp; refund policy","दान एवं धनवापसी नीति"),"donation-policy.html",internal=True)}
    {row(t("Photo &amp; media consent policy","फ़ोटो एवं मीडिया सहमति नीति"),"photo-consent.html",internal=True)}
    {row(t("Privacy policy","गोपनीयता नीति"),"privacy.html",internal=True)}
    {row(t("Terms of use","उपयोग की शर्तें"),"terms.html",internal=True)}
  </ul><ul class="tlist">
    {row(t("CSR Policy","CSR नीति"), note=t("Awaiting Board adoption","मंडल की स्वीकृति प्रतीक्षित"))}
    {row(t("Finance Policy","वित्त नीति"), note=t("Awaiting Board adoption","मंडल की स्वीकृति प्रतीक्षित"))}
    {row(t("Procurement Policy","क्रय नीति"), note=t("Awaiting Board adoption","मंडल की स्वीकृति प्रतीक्षित"))}
    {row(t("POSH Policy","POSH नीति"), note=t("Awaiting Board adoption","मंडल की स्वीकृति प्रतीक्षित"))}
    {row(t("Safeguarding Policy (full)","सेफ़गार्डिंग नीति (पूर्ण)"), note=t("Awaiting Board adoption","मंडल की स्वीकृति प्रतीक्षित"))}
  </ul></div>
</div></section>'''
    page("transparency.html", t("Transparency &amp; Governance — MOA, AOA, Licence, Board","पारदर्शिता एवं शासन — MOA, AOA, लाइसेंस, मंडल"),
         t("Transparency and governance at Vishavabhartiya Foundation: Certificate of Incorporation, Section 8 licence, MOA, AOA, 12A/80G approval, Board and policies.",
           "विश्वभारतीय फाउंडेशन में पारदर्शिता एवं शासन: निगमन प्रमाणपत्र, Section 8 लाइसेंस, MOA, AOA, 12A/80G अनुमोदन, मंडल एवं नीतियाँ।"), body)

def build_contact():
    maps_reg = "https://www.google.com/maps/search/?api=1&query=" + "3159%2FA%2F3+Diamond+Nagar+Kharbi+Main+Road+Nandanvan+Nagpur+440024"
    maps_svc = "https://www.google.com/maps/search/?api=1&query=" + "Maharashtra+Hospital+and+Optical+Kharbi+Main+Road+Nagpur"
    OPT = [("csr",t("CSR Partnership","CSR साझेदारी")),("donation",t("Donation","दान")),("camp",t("Health / Eye Camp","स्वास्थ्य / नेत्र शिविर")),("programme",t("Programme Partnership","कार्यक्रम साझेदारी")),("volunteer",t("Volunteer","स्वयंसेवा")),("media",t("Media","मीडिया")),("general",t("General Enquiry","सामान्य पूछताछ")),("other",t("Other","अन्य"))]
    opts = "".join(f'<option value="{v}">{l}</option>' for v,l in OPT)
    body = banner(t("Contact","संपर्क"), t("Contact Us","संपर्क करें"), t("Call, write or visit. We reply to every donor, volunteer and CSR enquiry.","फ़ोन करें, लिखें या मिलें। हम हर दानदाता, स्वयंसेवक एवं CSR संदेश का उत्तर देते हैं।")) + f'''
<section><div class="wrap grid g2">
  <div class="loc-card">
    <h3>{ico("pin")} {t("Registered Office","पंजीकृत कार्यालय")}</h3>
    <p class="purpose">{t("Legal registered address of the Foundation (as per MCA records) — for correspondence and official communication.","फाउंडेशन का वैधानिक पंजीकृत पता (MCA रिकॉर्ड अनुसार) — पत्राचार एवं आधिकारिक संवाद हेतु।")}</p>
    <dl><dt>{t("Address","पता")}</dt><dd>{ADDR()}</dd>
        <dt>{t("Phone","फ़ोन")}</dt><dd><a href="tel:+919423632405">{ORG["ph1"]}</a> · <a href="tel:+918669055934">{ORG["ph2"]}</a></dd>
        <dt>{t("Email","ईमेल")}</dt><dd>{EM("info")}</dd>
        <dt>{t("Hours","समय")}</dt><dd>{t("Please call before visiting","आने से पहले कृपया फ़ोन करें")}</dd></dl>
    <a class="btn btn-line" href="{maps_reg}" target="_blank" rel="noopener">{t("Directions","दिशा-निर्देश")}</a>
  </div>
  <div class="loc-card svc">
    <h3>{ico("eye")} {t("Eye Care / Service Centre","नेत्र सेवा / सेवा केंद्र")}</h3>
    <p class="purpose">{t("Maharashtra Hospital &amp; Optical — the founder's eye-care centre where free eye check-ups are held. This is a service location, not the registered office.","महाराष्ट्र हॉस्पिटल एवं ऑप्टिकल — संस्थापक का नेत्र-सेवा केंद्र, जहाँ निःशुल्क नेत्र जाँच होती है। यह सेवा-स्थल है, पंजीकृत कार्यालय नहीं।")}</p>
    <dl><dt>{t("Address","पता")}</dt><dd>{SVC()}</dd>
        <dt>{t("Phone","फ़ोन")}</dt><dd><a href="tel:+919423632405">{ORG["ph1"]}</a></dd>
        <dt>{t("Free check-up","निःशुल्क जाँच")}</dt><dd>{t("Daily, morning hours — please call to confirm timings","प्रतिदिन, सुबह के समय — समय की पुष्टि हेतु कृपया फ़ोन करें")}</dd></dl>
    <a class="btn btn-line" href="{maps_svc}" target="_blank" rel="noopener">{t("Directions","दिशा-निर्देश")}</a>
  </div>
</div></section>
<section class="alt" id="volunteer" style="scroll-margin-top:100px"><div class="wrap split" style="align-items:start">
  <div>
    <h2>{t("Send us a message","हमें संदेश भेजें")}</h2>
    <p class="muted">{t("For CSR proposals, 80G receipts, camp requests, volunteering or media. You can also reach us directly:","CSR प्रस्ताव, 80G रसीद, शिविर अनुरोध, स्वयंसेवा या मीडिया हेतु। आप सीधे भी संपर्क कर सकते हैं:")}</p>
    <ul class="contact-list">
      <li><span class="ic">{ico("phone")}</span><div><b>{t("Phone / WhatsApp","फ़ोन / WhatsApp")}</b><span>{ORG["ph1"]} · {ORG["ph2"]}</span></div></li>
      <li><span class="ic">{ico("mail")}</span><div><b>{t("Email","ईमेल")}</b><span>{EM("info", link=False)}</span></div></li>
      <li><span class="ic">{ico("youtube")}</span><div><b>{t("Follow us","हमसे जुड़ें")}</b>{SOCIAL("social inline")}</div></li>
      <li><span class="ic">{ico("file")}</span><div><b>{t("80G receipt","80G रसीद")}</b><span><a href="donate.html#receipt">{t("Use the receipt request form","रसीद अनुरोध फ़ॉर्म भरें")}</a></span></div></li>
    </ul>
  </div>
  <div class="panel" id="csr" style="scroll-margin-top:100px"><span id="profile"></span>
    <form data-vbf-form="contact" data-email-role="info" data-subject="{t("Website enquiry","वेबसाइट संदेश")}" novalidate>
      {HP()}
      <div class="row">
        <div class="field"><label for="cf-name">{t("Name","नाम")}</label><input id="cf-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="cf-org">{t("Organisation","संस्था")} <span class="opt">({t("optional","वैकल्पिक")})</span></label><input id="cf-org" name="organisation" autocomplete="organization"></div>
      </div>
      <div class="row">
        <div class="field"><label for="cf-mob">{t("Mobile","मोबाइल")}</label><input id="cf-mob" name="mobile" type="tel" data-rule="mobile" data-one-of="email" autocomplete="tel"></div>
        <div class="field"><label for="cf-email">{t("Email","ईमेल")}</label><input id="cf-email" name="email" type="email" data-rule="email" data-one-of="mobile" autocomplete="email"></div>
      </div>
      <div class="row">
        <div class="field"><label for="cf-place">{t("State / District","राज्य / ज़िला")}</label><input id="cf-place" name="state_district" required></div>
        <div class="field"><label for="cf-type">{t("Enquiry type","संदेश का प्रकार")}</label><select id="cf-type" name="enquiry_type" required>{opts}</select></div>
      </div>
      <div class="field"><label for="cf-msg">{t("Message","संदेश")}</label><textarea id="cf-msg" name="message" rows="5" required></textarea></div>
      <p class="muted small">{t("Please give a mobile number or an email so we can reply.","उत्तर देने के लिए कृपया मोबाइल नंबर या ईमेल दें।")}</p>
      <button class="btn btn-gold" type="submit">{t("Send message","संदेश भेजें")}</button>
      <p class="form-msg" aria-live="polite"></p>
      <p class="muted small">{t("Your details are used only to reply to you.","आपकी जानकारी केवल उत्तर देने हेतु उपयोग होगी।")} <a href="privacy.html">{t("Privacy policy","गोपनीयता नीति")}</a></p>
    </form>
  </div>
</div></section>'''
    page("contact.html", t("Contact Us — Registered Office &amp; Eye Care Centre","संपर्क — पंजीकृत कार्यालय एवं नेत्र सेवा केंद्र"),
         t("Contact Vishavabhartiya Foundation: registered office at Diamond Nagar, Kharbi Main Road, Nagpur 440024, and the eye-care service centre. Phone +91 94236 32405.",
           "विश्वभारतीय फाउंडेशन से संपर्क: पंजीकृत कार्यालय डायमंड नगर, खरबी मेन रोड, नागपुर 440024, तथा नेत्र-सेवा केंद्र। फ़ोन +91 94236 32405।"), body)

# ---------------------------------------------------------------- legal / trust pages
def legal_page(fname, crumb, h1, intro, sections, title, desc):
    s = "".join(f"<h2>{h}</h2>{b}" for h, b in sections)
    body = banner(crumb, h1, intro) + f'<section><div class="wrap prose">{s}<p class="muted small mt">{t("Last updated: 1 October 2026.","अंतिम अद्यतन: 1 अक्टूबर 2026।")}</p></div></section>'
    page(fname, title, desc, body)

def build_legal():
    C = lambda: f'{EM("info")} · {ORG["ph1"]}'
    legal_page("privacy.html", t("Privacy Policy","गोपनीयता नीति"), t("Privacy Policy","गोपनीयता नीति"), t("How we handle the information you share with us.","आपकी दी गई जानकारी का हम कैसे उपयोग करते हैं।"), [
      (t("Who we are","हम कौन हैं"), f'<p>{t("This website is run by Vishavabhartiya Foundation (CIN ","यह वेबसाइट विश्वभारतीय फाउंडेशन (CIN ")}{ORG["cin"]}), {ADDR()}.</p>'),
      (t("What we collect","हम क्या एकत्र करते हैं"), f'<ul><li>{t("Details you send through forms, email, phone or WhatsApp: name, organisation, phone, email, location and message.","फ़ॉर्म, ईमेल, फ़ोन या WhatsApp से भेजी गई जानकारी: नाम, संस्था, फ़ोन, ईमेल, स्थान एवं संदेश।")}</li><li>{t("For donations: name, PAN, address, amount, date and transaction reference, needed to issue an 80G receipt and meet Income Tax reporting requirements.","दान हेतु: नाम, PAN, पता, राशि, तिथि एवं लेन-देन संदर्भ — 80G रसीद एवं आयकर रिपोर्टिंग हेतु आवश्यक।")}</li><li>{t("For camps: beneficiary details on camp registers, used for follow-up care and reporting.","शिविर हेतु: शिविर रजिस्टर में लाभार्थी विवरण — फ़ॉलो-अप एवं रिपोर्टिंग हेतु।")}</li></ul>'),
      (t("How we use it","उपयोग कैसे करते हैं"), f'<p>{t("To reply to you, issue receipts, meet legal and audit requirements, and report to partners. Reports to partners use totals and photographs, not personal contact details, unless you agree.","उत्तर देने, रसीद जारी करने, वैधानिक एवं अंकेक्षण आवश्यकताओं और साझेदारों को रिपोर्टिंग हेतु। साझेदारों की रिपोर्ट में कुल संख्या एवं फ़ोटो होते हैं, आपकी सहमति के बिना व्यक्तिगत संपर्क विवरण नहीं।")}</p>'),
      (t("What we do not do","हम क्या नहीं करते"), f'<p>{t("We do not sell, rent or trade personal information. This website does not use advertising or tracking cookies and does not collect card details. UPI and bank payments are processed by your bank.","हम व्यक्तिगत जानकारी बेचते, किराए पर देते या व्यापार नहीं करते। यह वेबसाइट विज्ञापन या ट्रैकिंग कुकीज़ उपयोग नहीं करती और कार्ड विवरण एकत्र नहीं करती। UPI एवं बैंक भुगतान आपके बैंक द्वारा संसाधित होते हैं।")}</p>'),
      (t("Retention and your rights","संरक्षण एवं आपके अधिकार"), f'<p>{t("Donation records are kept for the period required by law; other data only as long as needed. You may ask to see, correct or delete your information:","दान रिकॉर्ड कानून द्वारा निर्धारित अवधि तक रखे जाते हैं; अन्य जानकारी केवल आवश्यकता तक। अपनी जानकारी देखने, सुधारने या हटाने हेतु संपर्क करें:")} {C()}.</p>'),
    ], t("Privacy Policy","गोपनीयता नीति"), t("Privacy policy of Vishavabhartiya Foundation, Nagpur: what we collect, how we use it and your rights.","विश्वभारतीय फाउंडेशन, नागपुर की गोपनीयता नीति: हम क्या एकत्र करते हैं, कैसे उपयोग करते हैं और आपके अधिकार।"))

    legal_page("terms.html", t("Terms of Use","उपयोग की शर्तें"), t("Terms of Use","उपयोग की शर्तें"), t("Conditions for using this website.","इस वेबसाइट के उपयोग की शर्तें।"), [
      (t("Use of this website","वेबसाइट का उपयोग"), f'<p>{t("This website provides information about Vishavabhartiya Foundation and its programmes. By using it you agree to these terms.","यह वेबसाइट विश्वभारतीय फाउंडेशन एवं उसके कार्यक्रमों की जानकारी देती है। इसका उपयोग करके आप इन शर्तों से सहमत होते हैं।")}</p>'),
      (t("Accuracy of information","जानकारी की शुद्धता"), f'<p>{t("We try to keep information accurate and up to date, but it may change. Registration details can be verified on official government portals. If you notice an error, please tell us.","हम जानकारी सही एवं अद्यतन रखने का प्रयास करते हैं, पर उसमें परिवर्तन हो सकता है। पंजीकरण विवरण आधिकारिक सरकारी पोर्टलों पर सत्यापित किए जा सकते हैं। कोई त्रुटि दिखे तो कृपया सूचित करें।")}</p>'),
      (t("Content and images","सामग्री एवं चित्र"), f'<p>{t("Text, logo, photographs and documents on this site belong to the Foundation or are used with permission. Do not reuse them for commercial purposes or in a way that suggests our endorsement without written permission. Partner photos are credited to the partner organisation.","इस साइट का पाठ, लोगो, फ़ोटो एवं दस्तावेज़ फाउंडेशन के हैं या अनुमति से उपयोग किए गए हैं। लिखित अनुमति के बिना इनका व्यावसायिक उपयोग या हमारे समर्थन का आभास देने वाला उपयोग न करें। साझेदार की फ़ोटो पर साझेदार संस्था का श्रेय दिया गया है।")}</p>'),
      (t("External links","बाहरी लिंक"), f'<p>{t("Links to other websites are provided for convenience; we are not responsible for their content.","अन्य वेबसाइटों के लिंक सुविधा हेतु दिए गए हैं; उनकी सामग्री के लिए हम उत्तरदायी नहीं हैं।")}</p>'),
      (t("Donations","दान"), f'<p>{t("Donations are governed by our","दान हमारी")} <a href="donation-policy.html">{t("Donation &amp; Refund Policy","दान एवं धनवापसी नीति")}</a>{t(".", " के अधीन हैं।")}</p>'),
      (t("Contact","संपर्क"), f'<p>{C()}</p>'),
    ], t("Terms of Use","उपयोग की शर्तें"), t("Terms of use of the Vishavabhartiya Foundation website.","विश्वभारतीय फाउंडेशन वेबसाइट के उपयोग की शर्तें।"))

    legal_page("donation-policy.html", t("Donation &amp; Refund Policy","दान एवं धनवापसी नीति"), t("Donation &amp; Refund Policy","दान एवं धनवापसी नीति"), t("How donations are received, receipted and, where appropriate, refunded.","दान कैसे प्राप्त होते हैं, उनकी रसीद कैसे मिलती है और उचित स्थिति में धनवापसी कैसे होती है।"), [
      (t("Nature of donations","दान का स्वरूप"), f'<p>{t("Donations are voluntary contributions to support the Foundation’s charitable objects. They support programme delivery, which can include necessary administrative, compliance and logistics costs as permitted by law. Donations are accepted from Indian sources only (the Foundation is not FCRA-registered).","दान फाउंडेशन के धर्मार्थ उद्देश्यों के लिए स्वैच्छिक योगदान है। यह कार्यक्रमों के संचालन में सहायक होता है, जिसमें कानून द्वारा अनुमत आवश्यक प्रशासनिक, अनुपालन एवं परिवहन व्यय शामिल हो सकते हैं। केवल भारतीय स्रोतों से दान स्वीकार किया जाता है (फाउंडेशन FCRA-पंजीकृत नहीं है)।")}</p>'),
      (t("Receipt process","रसीद प्रक्रिया"), f'<ol><li>{t("Donate by UPI or bank transfer to the account named VISHAVABHARTIYA FOUNDATION.","VISHAVABHARTIYA FOUNDATION नाम के खाते में UPI या बैंक ट्रांसफ़र से दान करें।")}</li><li>{t("Submit the","भरें:")} <a href="donate.html#receipt">{t("80G receipt request form","80G रसीद अनुरोध फ़ॉर्म")}</a> {t("with your PAN and transaction reference.","— PAN एवं लेन-देन संदर्भ सहित।")}</li><li>{t("After the amount is matched in our bank account, a receipt is issued to your email.","राशि बैंक खाते में मिलान होने के बाद आपके ईमेल पर रसीद भेजी जाती है।")}</li></ol><p>{t("80G benefit applies as per the Income Tax Act and the Foundation’s approval (provisional, AY 2026-27 to AY 2028-29). Cash donations above ₹2,000 are not eligible for deduction.","80G लाभ आयकर अधिनियम एवं फाउंडेशन के अनुमोदन (अस्थायी, निर्धारण वर्ष 2026-27 से 2028-29) के अनुसार लागू है। ₹2,000 से अधिक नकद दान कटौती हेतु पात्र नहीं है।")}</p>'),
      (t("Incorrect transaction","गलत लेन-देन"), f'<p>{t("If you donated a wrong amount, paid twice, or sent money to our account by mistake, contact us within 15 days with the transaction reference, date and amount:","यदि आपने गलत राशि दी, दो बार भुगतान किया या गलती से हमारे खाते में पैसे भेजे, तो 15 दिनों के भीतर लेन-देन संदर्भ, तिथि एवं राशि के साथ संपर्क करें:")} {EM("donations")} · {ORG["ph1"]}.</p>'),
      (t("Refund request process","धनवापसी अनुरोध प्रक्रिया"), f'<p>{t("Refund requests are reviewed case by case after verifying the transaction in our bank statement. Where a refund is approved, it is made only to the original source account. A refund is generally not possible once an 80G receipt has been issued and reported, unless the receipt is withdrawn as allowed by law. Payment gateway or bank charges, if any, may not be recoverable.","धनवापसी अनुरोधों की जाँच बैंक विवरण में लेन-देन सत्यापित करने के बाद प्रत्येक मामले में अलग से की जाती है। स्वीकृत होने पर धनवापसी केवल मूल स्रोत खाते में की जाती है। 80G रसीद जारी एवं रिपोर्ट हो जाने के बाद सामान्यतः धनवापसी संभव नहीं होती, जब तक कि कानून अनुसार रसीद वापस न ली जाए। बैंक शुल्क, यदि कोई हो, वापस न मिल सकें।")}</p>'),
      (t("Contact","संपर्क"), f'<p>{C()}</p>'),
    ], t("Donation &amp; Refund Policy","दान एवं धनवापसी नीति"), t("Donation and refund policy of Vishavabhartiya Foundation: receipts, 80G, incorrect transactions and refund requests.","विश्वभारतीय फाउंडेशन की दान एवं धनवापसी नीति: रसीद, 80G, गलत लेन-देन एवं धनवापसी अनुरोध।"))

    legal_page("photo-consent.html", t("Photo &amp; Media Consent","फ़ोटो एवं मीडिया सहमति"), t("Photo &amp; Media Consent Policy","फ़ोटो एवं मीडिया सहमति नीति"), t("How we take and use photographs and videos responsibly.","हम फ़ोटो एवं वीडियो ज़िम्मेदारी से कैसे लेते और उपयोग करते हैं।"), [
      (t("Our approach","हमारा दृष्टिकोण"), f'<p>{t("Photographs help us report honestly to donors and partners. We take them respectfully and only use them in ways that protect the dignity of the people shown.","फ़ोटो से हम दानदाताओं एवं साझेदारों को ईमानदारी से रिपोर्ट करते हैं। हम उन्हें सम्मानपूर्वक लेते हैं और केवल ऐसे उपयोग करते हैं जिससे फ़ोटो में दिखे लोगों की गरिमा बनी रहे।")}</p>'),
      (t("Consent","सहमति"), f'<ul><li>{t("We ask for verbal or written consent before close-up photographs of individuals.","व्यक्तियों की नज़दीकी फ़ोटो से पहले हम मौखिक या लिखित सहमति लेते हैं।")}</li><li>{t("For children, consent is taken from a parent, guardian or the responsible institution.","बच्चों हेतु माता-पिता, अभिभावक या उत्तरदायी संस्था से सहमति ली जाती है।")}</li><li>{t("People may decline to be photographed without any effect on the services they receive.","कोई भी फ़ोटो से मना कर सकता है; इससे मिलने वाली सेवा पर कोई असर नहीं पड़ता।")}</li></ul>'),
      (t("What we avoid","हम किससे बचते हैं"), f'<ul><li>{t("Images during medical examination that expose a person’s body or condition in an undignified way.","चिकित्सा जाँच के दौरान ऐसे चित्र जो किसी के शरीर या स्थिति को अपमानजनक रूप से दिखाएँ।")}</li><li>{t("Publishing names, addresses or health details of beneficiaries alongside their photos.","लाभार्थियों की फ़ोटो के साथ उनके नाम, पते या स्वास्थ्य विवरण प्रकाशित करना।")}</li><li>{t("Presenting a partner’s photographs as our own work.","साझेदार की फ़ोटो को अपने कार्य के रूप में प्रस्तुत करना।")}</li></ul>'),
      (t("Removal requests","हटाने का अनुरोध"), f'<p>{t("If you appear in a photograph on this website and want it removed, write to us; we will remove it promptly.","यदि आप इस वेबसाइट की किसी फ़ोटो में हैं और उसे हटवाना चाहते हैं, तो हमें लिखें; हम उसे शीघ्र हटा देंगे।")} {C()}</p>'),
    ], t("Photo &amp; Media Consent Policy","फ़ोटो एवं मीडिया सहमति नीति"), t("How Vishavabhartiya Foundation takes, uses and removes programme and media photographs responsibly.","विश्वभारतीय फाउंडेशन कार्यक्रम एवं मीडिया फ़ोटो को ज़िम्मेदारी से कैसे लेता, उपयोग करता और हटाता है।"))

    legal_page("safeguarding.html", t("Safeguarding","सेफ़गार्डिंग"), t("Child &amp; Vulnerable Person Safeguarding Statement","बाल एवं असुरक्षित व्यक्ति सुरक्षा (सेफ़गार्डिंग) वक्तव्य"), t("Our commitment to keeping children and vulnerable adults safe in all our work.","हमारे सभी कार्यों में बच्चों एवं असुरक्षित वयस्कों की सुरक्षा के प्रति हमारी प्रतिबद्धता।"), [
      (t("Our commitment","हमारी प्रतिबद्धता"), f'<p>{t("Vishavabhartiya Foundation works with children, the elderly, people with disabilities and others who may be vulnerable. Every person has the right to be safe from abuse, exploitation and neglect. We do not tolerate any form of harm by our directors, staff, volunteers or partners.","विश्वभारतीय फाउंडेशन बच्चों, बुज़ुर्गों, दिव्यांगजनों एवं अन्य असुरक्षित लोगों के साथ काम करता है। हर व्यक्ति को दुर्व्यवहार, शोषण एवं उपेक्षा से सुरक्षित रहने का अधिकार है। हमारे निदेशकों, कर्मचारियों, स्वयंसेवकों या साझेदारों द्वारा किसी भी प्रकार की हानि बर्दाश्त नहीं की जाती।")}</p>'),
      (t("What we do","हम क्या करते हैं"), f'<ul><li>{t("Children at camps and school programmes are attended in the presence of teachers, parents or guardians.","शिविरों एवं विद्यालय कार्यक्रमों में बच्चों की सेवा शिक्षकों, माता-पिता या अभिभावकों की उपस्थिति में होती है।")}</li><li>{t("Volunteers are briefed on respectful conduct before taking part.","भाग लेने से पहले स्वयंसेवकों को सम्मानजनक आचरण की जानकारी दी जाती है।")}</li><li>{t("Photographs follow our","फ़ोटो हमारी")} <a href="photo-consent.html">{t("Photo &amp; Media Consent Policy","फ़ोटो एवं मीडिया सहमति नीति")}</a>{t(".", " का पालन करती हैं।")}</li><li>{t("Personal and health information of beneficiaries is kept confidential.","लाभार्थियों की व्यक्तिगत एवं स्वास्थ्य जानकारी गोपनीय रखी जाती है।")}</li></ul>'),
      (t("Reporting a concern","चिंता की सूचना देना"), f'<p>{t("Anyone can raise a safeguarding concern, including anonymously, through our","कोई भी — गुमनाम रूप से भी — सेफ़गार्डिंग संबंधी चिंता हमारी")} <a href="grievance.html">{t("grievance mechanism","शिकायत निवारण व्यवस्था")}</a>{t(". Concerns are handled confidentially by the Managing Director and, where required, reported to the appropriate authorities. In an emergency involving a child, call Childline 1098 or the police at 112."," के माध्यम से उठा सकता है। चिंताओं का प्रबंध निदेशक द्वारा गोपनीय रूप से निपटारा किया जाता है और आवश्यक होने पर उपयुक्त प्राधिकरण को सूचित किया जाता है। किसी बच्चे से जुड़ी आपात स्थिति में चाइल्डलाइन 1098 या पुलिस 112 पर कॉल करें।")}</p>'),
      (t("Policy status","नीति की स्थिति"), f'<p>{t("A full Safeguarding Policy will be published on the Transparency &amp; Governance page once adopted by the Board.","पूर्ण सेफ़गार्डिंग नीति मंडल द्वारा अपनाए जाने के बाद पारदर्शिता एवं शासन पृष्ठ पर प्रकाशित की जाएगी।")}</p>'),
    ], t("Safeguarding Statement","सेफ़गार्डिंग वक्तव्य"), t("Child and vulnerable person safeguarding statement of Vishavabhartiya Foundation, Nagpur.","विश्वभारतीय फाउंडेशन, नागपुर का बाल एवं असुरक्षित व्यक्ति सुरक्षा वक्तव्य।"))

    legal_page("grievance.html", t("Grievance","शिकायत"), t("Grievance Mechanism","शिकायत निवारण व्यवस्था"), t("How to raise a complaint or concern about our work, and how we respond.","हमारे कार्य के बारे में शिकायत या चिंता कैसे उठाएँ और हम कैसे उत्तर देते हैं।"), [
      (t("Who can raise a grievance","कौन शिकायत कर सकता है"), f'<p>{t("Beneficiaries, donors, volunteers, partners, staff and members of the public can raise a complaint or concern — about a service, a donation or receipt, conduct of any person linked to the Foundation, or misuse of information or photographs.","लाभार्थी, दानदाता, स्वयंसेवक, साझेदार, कर्मचारी एवं आम नागरिक — किसी सेवा, दान या रसीद, फाउंडेशन से जुड़े किसी व्यक्ति के आचरण, या जानकारी/फ़ोटो के दुरुपयोग के बारे में शिकायत कर सकते हैं।")}</p>'),
      (t("Grievance contact","शिकायत हेतु संपर्क"), f'<p><b>{t("Office of the Managing Director, Vishavabhartiya Foundation","प्रबंध निदेशक कार्यालय, विश्वभारतीय फाउंडेशन")}</b><br>{ADDR()}<br>{t("Email:","ईमेल:")} {EM("info")}<br>{t("Phone / WhatsApp:","फ़ोन / WhatsApp:")} {ORG["ph1"]} · {ORG["ph2"]}</p>'),
      (t("How we handle it","हम कैसे निपटाते हैं"), f'<ol><li>{t("We acknowledge your grievance, normally within 7 working days.","हम सामान्यतः 7 कार्य-दिवसों में आपकी शिकायत की पावती देते हैं।")}</li><li>{t("It is reviewed confidentially; anyone involved in the complaint is kept out of the review.","गोपनीय रूप से समीक्षा होती है; शिकायत से जुड़ा व्यक्ति समीक्षा से अलग रखा जाता है।")}</li><li>{t("We aim to share the outcome within 30 days, or explain if more time is needed.","हम 30 दिनों में परिणाम बताने का प्रयास करते हैं, या अधिक समय लगे तो कारण बताते हैं।")}</li><li>{t("Serious matters, including safeguarding concerns, are escalated to the Board and, where required, to the authorities.","सेफ़गार्डिंग सहित गंभीर मामले मंडल तक, और आवश्यक होने पर प्राधिकरण तक पहुँचाए जाते हैं।")}</li></ol>'),
      (t("No retaliation","प्रतिशोध नहीं"), f'<p>{t("No one will be denied services or treated unfairly for raising a concern in good faith. You may raise a concern anonymously, though that can limit our ability to follow up.","सद्भाव से चिंता उठाने पर किसी को सेवा से वंचित या अनुचित व्यवहार नहीं किया जाएगा। आप गुमनाम रूप से भी शिकायत कर सकते हैं, हालाँकि इससे आगे की कार्रवाई सीमित हो सकती है।")}</p>'),
    ], t("Grievance Mechanism","शिकायत निवारण व्यवस्था"), t("How to raise a grievance with Vishavabhartiya Foundation and how complaints are handled.","विश्वभारतीय फाउंडेशन में शिकायत कैसे दर्ज करें और उसका निपटारा कैसे होता है।"))

# ======================================================================= BUILD
for LANG in LANGS:
    build_home(); build_about(); build_programs(); build_impact(); build_media(); build_gallery()
    build_registrations(); build_donate(); build_csr(); build_transparency(); build_contact(); build_legal()

site = CONFIG["site_url"].rstrip("/")
cfg = {"siteUrl": site, "emails": CONFIG["emails"], "whatsapp": CONFIG["whatsapp"], "forms": CONFIG["forms"]}
open(os.path.join(OUT, "assets/js/config.js?v=20261025b"), "w", encoding="utf-8").write(
    "/* Generated from CONFIG in build.py. You may also edit here directly: emails and forms.endpoint take effect without a rebuild. */\nwindow.VBF_CONFIG = " + json.dumps(cfg, indent=2) + ";\n")
open(os.path.join(OUT, "assets/js/img-sizes.js?v=20261025b"), "w").write("window.VBF_SIZES=" + json.dumps(SIZES, separators=(",", ":")) + ";\n")

def loc(lang, f): return site + "/" + ("hi/" if lang == "hi" else "") + ("" if f == "index.html" else f)
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for f in PAGES_BUILT:
    for lang in LANGS:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{loc(l, f)}"/>' for l in LANGS)
        sm.append(f"  <url><loc>{loc(lang, f)}</loc>{alts}<lastmod>2026-10-01</lastmod></url>")
sm.append("</urlset>")
open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /backend/\nSitemap: {site}/sitemap.xml\n")
print("built", len(PAGES_BUILT), "pages x", len(LANGS), "languages")
