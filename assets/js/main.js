/* Vishavabhartiya Foundation — site behaviour (v2). Content: data.js · Settings: config.js */
(function () {
  "use strict";
  var D = window.VBF || {}, C = window.VBF_CONFIG || {}, SZ = window.VBF_SIZES || {};
  var LANG = document.documentElement.lang === "hi" ? "hi" : "en";
  var BASE = document.documentElement.getAttribute("data-base") || "";
  var UI = {
    en: { upcoming: "Upcoming", copy: "Copy", copied: "Copied", foundation: "Foundation activity", legacy: "Founder's legacy (pre-2026)",
          partner: "Partner field activity – YKVM, Uttar Pradesh", months: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          fix: "Please correct the highlighted fields.", sending: "Sending…", sent: "Thank you. Your details have been received. We will reply soon.",
          failed: "We could not submit the form online. Your details are not lost — please send them using one of the options below.",
          offline: "Online submission is not connected yet, so nothing has been sent. Please send your details using one of the options below:",
          wa: "Send on WhatsApp", mail: "Send by email", spam: "Please wait a moment and try again.", close: "Close" },
    hi: { upcoming: "आगामी", copy: "कॉपी", copied: "कॉपी हुआ", foundation: "फाउंडेशन गतिविधि", legacy: "संस्थापक की विरासत (2026 से पहले)",
          partner: "साझेदार संस्था की गतिविधि – YKVM, उत्तर प्रदेश", months: ["जनवरी","फ़रवरी","मार्च","अप्रैल","मई","जून","जुलाई","अगस्त","सितंबर","अक्टूबर","नवंबर","दिसंबर"],
          fix: "कृपया चिह्नित जानकारी सही करें।", sending: "भेजा जा रहा है…", sent: "धन्यवाद। आपकी जानकारी प्राप्त हो गई है। हम शीघ्र उत्तर देंगे।",
          failed: "फ़ॉर्म ऑनलाइन जमा नहीं हो सका। आपकी जानकारी सुरक्षित है — कृपया नीचे दिए किसी विकल्प से भेजें।",
          offline: "ऑनलाइन जमा करने की सुविधा अभी जुड़ी नहीं है, इसलिए अभी कुछ भी नहीं भेजा गया है। कृपया नीचे दिए किसी विकल्प से अपनी जानकारी भेजें:",
          wa: "WhatsApp पर भेजें", mail: "ईमेल से भेजें", spam: "कृपया थोड़ी देर बाद पुनः प्रयास करें।", close: "बंद करें" }
  }[LANG];

  function L(x) { return x && typeof x === "object" ? (x[LANG] || x.en || "") : (x || ""); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function fmt(d, when) { if (when) return L(when); var p = String(d).split("-"); return p.length === 3 ? (+p[2]) + " " + UI.months[+p[1] - 1] + " " + p[0] : d; }
  function byDate(a, b) { return String(b.date).localeCompare(String(a.date)); }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function img(src, alt, cls, cap) {
    var s = SZ[src], wh = s ? ' width="' + s[0] + '" height="' + s[1] + '"' : "";
    return '<img' + (cls ? ' class="' + cls + '"' : "") + ' loading="lazy" decoding="async" src="' + esc(BASE + src) + '"' + wh + ' alt="' + esc(alt) + '" data-cap="' + esc(cap || alt) + '">';
  }
  function email(role) { var e = C.emails || {}; return e[role] || e.fallback || ""; }

  /* ---- mobile menu & dropdowns ---- */
  var mb = $(".menu-btn"), nav = $(".nav");
  if (mb && nav) mb.addEventListener("click", function () { var o = nav.classList.toggle("open"); mb.setAttribute("aria-expanded", o ? "true" : "false"); });
  $$(".nav .dd > button").forEach(function (b) {
    b.addEventListener("click", function () { var o = b.parentNode.classList.toggle("open"); b.setAttribute("aria-expanded", o ? "true" : "false"); });
  });
  document.addEventListener("click", function (e) { $$(".nav .dd.open").forEach(function (dd) { if (!dd.contains(e.target)) dd.classList.remove("open"); }); });

  /* ---- renderers ---- */
  function activityCard(a) {
    return '<article class="card">' + img(a.img, L(a.title), "thumb") + '<div class="body"><span class="meta">' + esc(fmt(a.date, a.when)) + ' · ' + esc(L(a.tag)) +
      (a.upcoming ? '<span class="pill-up">' + UI.upcoming + '</span>' : "") + '</span><h3>' + esc(L(a.title)) + '</h3><p>' + esc(L(a.text)) + '</p></div></article>';
  }
  function mediaCard(m) {
    return '<article class="card">' + img(m.img, L(m.title), "thumb contain", L(m.paper) + " — " + L(m.title)) + '<div class="body"><span class="meta">' + esc(fmt(m.date, m.when)) +
      '</span><h3>' + esc(L(m.title)) + '</h3><p>' + esc(L(m.text)) + '</p><span class="src">' + esc(L(m.paper)) + '</span></div></article>';
  }
  function awardCard(a) {
    return '<div class="award">' + img(a.img, L(a.title)) + '<div><span class="yr">' + esc(a.year) + '</span><h3>' + esc(L(a.title)) + '</h3><p><b>' + esc(L(a.by)) + '</b></p><p>' + esc(L(a.text)) + '</p></div></div>';
  }
  function galleryItem(g) {
    var era = g.era === "foundation" ? "foundation" : "legacy";
    return '<figure data-cat="' + esc(g.cat) + '"><span class="src-badge ' + era + '">' + UI[era] + '</span>' + img(g.src, L(g.title), "", L(g.title) + " — " + L(g.caption)) +
      '<figcaption><b>' + esc(L(g.title)) + '</b>' + esc(L(g.caption)) + '</figcaption></figure>';
  }
  function partnerItem(g) {
    return '<figure data-cat="partner"><span class="src-badge partner">' + UI.partner + '</span>' + img(g.src, L(g.title), "", L(g.title) + " — " + UI.partner) +
      '<figcaption><b>' + esc(L(g.title)) + '</b>' + UI.partner + '</figcaption></figure>';
  }
  function fill(sel, list, fn) {
    $$(sel).forEach(function (el) { var n = parseInt(el.getAttribute("data-limit") || "0", 10); el.innerHTML = (n ? list.slice(0, n) : list).map(fn).join(""); });
  }
  fill("[data-render=activities]", (D.activities || []).slice().sort(byDate), activityCard);
  fill("[data-render=media]", (D.media || []).slice().sort(byDate), mediaCard);
  fill("[data-render=honours]", D.honours || [], awardCard);
  fill("[data-render=recognition]", D.recognition || [], awardCard);
  fill("[data-render=training]", D.training || [], awardCard);
  fill("[data-render=gallery]", D.gallery || [], galleryItem);
  fill("[data-render=partners]", D.partners || [], partnerItem);
  function orgCard(o) {
    var mark = o.logo ? '<img src="' + esc(BASE + o.logo) + '" alt="' + esc(L(o.name)) + ' logo" loading="lazy">' : '<span aria-hidden="true">' + esc(o.initials || "") + '</span>';
    return '<div class="org"><div class="org-logo' + (o.logo ? " has-img" : "") + '">' + mark + '</div><div><h3>' + esc(L(o.name)) + '</h3><span class="role">' + esc(L(o.role)) + '</span><p>' + esc(L(o.text)) + '</p></div></div>';
  }
  var orgs = D.partnerOrgs || [];
  fill("[data-render=orgs-current]", orgs.filter(function (o) { return o.group === "current"; }), orgCard);
  fill("[data-render=orgs-legacy]", orgs.filter(function (o) { return o.group === "legacy"; }), orgCard);
  fill("[data-render=logo-strip]", D.partnerLogos || [], function (o) {
    return '<figure class="plogo' + (o.style ? " " + esc(o.style) : "") + '"><img src="' + esc(BASE + o.logo) + '" alt="' + esc(o.name) + '" title="' + esc(o.name) + '" loading="lazy"><figcaption>' + esc(o.name) + '</figcaption></figure>';
  });
  $$("[data-count]").forEach(function (el) { var k = el.getAttribute("data-count"); el.textContent = (D[k] || []).length; });

  /* ---- gallery filters ---- */
  $$(".filters button").forEach(function (b) {
    b.addEventListener("click", function () {
      var c = b.getAttribute("data-f"), g = $("#" + b.parentNode.getAttribute("data-target"));
      $$("button", b.parentNode).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      if (g) $$("figure", g).forEach(function (f) { f.hidden = !(c === "all" || f.getAttribute("data-cat") === c || f.querySelector(".src-badge." + c)); });
    });
  });

  /* ---- lightbox ---- */
  var lb = document.createElement("div");
  lb.className = "lightbox"; lb.hidden = true; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-modal", "true");
  lb.innerHTML = '<button type="button" aria-label="' + UI.close + '">×</button><img alt=""><p></p>';
  document.body.appendChild(lb);
  function closeLb() { lb.hidden = true; }
  lb.addEventListener("click", function (e) { if (e.target === lb || e.target.tagName === "BUTTON") closeLb(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeLb(); });
  document.addEventListener("click", function (e) {
    var t = e.target;
    if (t.tagName === "IMG" && t.hasAttribute("data-cap")) {
      $("img", lb).src = t.currentSrc || t.src; $("img", lb).alt = t.alt; $("p", lb).textContent = t.getAttribute("data-cap");
      lb.hidden = false; $("button", lb).focus();
    }
  });

  /* ---- copy buttons ---- */
  $$(".copy").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.getAttribute("data-copy"), done = function () { b.classList.add("done"); b.textContent = UI.copied; setTimeout(function () { b.classList.remove("done"); b.textContent = UI.copy; }, 1600); };
      try { navigator.clipboard.writeText(v).then(done, function () { selectText(b); }); } catch (e) { selectText(b); }
    });
  });
  function selectText(b) { var dd = b.previousElementSibling; if (!dd) return; var r = document.createRange(); r.selectNodeContents(dd); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); }

  /* ---- email links from central config ---- */
  $$("[data-email]").forEach(function (el) { var e = email(el.getAttribute("data-email")); if (!e) return; el.textContent = e; if (el.tagName === "A") el.href = "mailto:" + e; });

  /* ---- forms: validation → backend (if configured) → honest fallback ---- */
  var RULES = {
    pan: /^[A-Z]{5}[0-9]{4}[A-Z]$/, mobile: /^(\+?91[\s-]?)?[6-9]\d{9}$/, email: /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/, amount: /^\d+(\.\d{1,2})?$/
  };
  function validate(form) {
    var ok = true;
    $$("[name]", form).forEach(function (f) {
      if (f.classList.contains("hp-input")) return;
      var v = (f.value || "").trim(), rule = f.getAttribute("data-rule"), bad = false;
      if (f.required && !v) bad = true;
      else if (v && rule === "pan") { f.value = v = v.toUpperCase(); bad = !RULES.pan.test(v); }
      else if (v && rule && RULES[rule]) bad = !RULES[rule].test(v.replace(/\s+/g, rule === "mobile" ? "" : " "));
      if (v && f.type === "date") { bad = bad || new Date(v) > new Date(); }
      if (f.getAttribute("data-one-of")) {
        var other = form.querySelector('[name="' + f.getAttribute("data-one-of") + '"]');
        if (!v && other && !other.value.trim()) bad = true;
      }
      f.setAttribute("aria-invalid", bad ? "true" : "false"); if (bad) ok = false;
    });
    return ok;
  }
  function summary(form) {
    var lines = [form.getAttribute("data-subject") || "Website enquiry"];
    $$("[name]", form).forEach(function (f) {
      if (f.classList.contains("hp-input") || !f.value.trim()) return;
      var lab = form.querySelector('label[for="' + f.id + '"]');
      lines.push((lab ? lab.textContent.replace(/\(.*?\)/g, "").trim() : f.name) + ": " + f.value.trim());
    });
    return lines.join("\n");
  }
  function fallbackLinks(form, out, msgText) {
    var text = summary(form), role = form.getAttribute("data-email-role") || "info", to = email(role);
    var wa = "https://wa.me/" + (C.whatsapp || "919423632405") + "?text=" + encodeURIComponent(text);
    var mail = "mailto:" + to + "?subject=" + encodeURIComponent(form.getAttribute("data-subject") || "Website enquiry") + "&body=" + encodeURIComponent(text);
    out.className = "form-msg info";
    out.innerHTML = esc(msgText) + '<span class="form-actions"><a class="btn btn-gold" href="' + wa + '" target="_blank" rel="noopener">' + UI.wa + '</a>' +
      (to ? '<a class="btn btn-line" href="' + mail + '">' + UI.mail + '</a>' : "") + '</span>' + (to ? '<span class="small muted">' + esc(to) + '</span>' : "");
  }
  $$("form[data-vbf-form]").forEach(function (form) {
    var started = Date.now(), out = $(".form-msg", form), btn = $("button[type=submit]", form);
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var hp = $(".hp-input", form);
      if (hp && hp.value) return;                                  /* bot filled the hidden field */
      if (Date.now() - started < 3000) { out.className = "form-msg err"; out.textContent = UI.spam; return; }
      if (!validate(form)) { out.className = "form-msg err"; out.textContent = UI.fix; var f = $('[aria-invalid="true"]', form); if (f) f.focus(); return; }
      var endpoint = (C.forms || {}).endpoint;
      if (!endpoint) { fallbackLinks(form, out, UI.offline); return; }   /* TODO(owner): set forms.endpoint in config.js to enable online saving */
      var data = new FormData(form); data.append("form", form.getAttribute("data-vbf-form")); data.append("lang", LANG); data.append("page", location.pathname);
      btn.disabled = true; out.className = "form-msg info"; out.textContent = UI.sending;
      fetch(endpoint, { method: "POST", body: data, mode: "cors" }).then(function (r) { return r.ok ? r.json().catch(function () { return { ok: true }; }) : Promise.reject(r.status); })
        .then(function (j) { if (j && j.ok === false) throw new Error("rejected"); out.className = "form-msg ok"; out.textContent = UI.sent; form.reset(); })
        .catch(function () { fallbackLinks(form, out, UI.failed); })
        .then(function () { btn.disabled = false; });
    });
  });

  /* ---- CSR enquiry pre-select from links like contact.html#csr ---- */
  var sel = $("#cf-type"), map = { csr: "csr", profile: "csr", donation: "donation", camp: "camp", volunteer: "volunteer", media: "media" };
  if (sel && map[location.hash.slice(1)]) sel.value = map[location.hash.slice(1)];
  var msg = $("#cf-msg");
  if (msg && location.hash === "#profile" && !msg.value) msg.value = LANG === "hi" ? "कृपया फाउंडेशन की संस्था प्रोफ़ाइल एवं पंजीकरण दस्तावेज़ भेजें।" : "Please share the Foundation's organisation profile and registration documents.";

  /* ---- home hero: two equal photos, each changes from the gallery ---- */
  var hv = $(".hero-visual"), list = (D.gallery || []).slice();
  if (hv && list.length > 2) {
    var slots = $$(".hv-slot", hv);
    var state = slots.map(function (fig, k) {
      var a = $("img", fig), b2 = document.createElement("img"); b2.alt = ""; b2.decoding = "async"; fig.insertBefore(b2, $("figcaption", fig));
      return { imgs: [a, b2], front: 0, cap: $("figcaption", fig), idx: k };
    });
    function step(st) {
      st.idx = (st.idx + slots.length) % list.length;
      var g = list[st.idx], back = 1 - st.front, nb = st.imgs[back];
      nb.onload = function () { nb.classList.add("on"); st.imgs[st.front].classList.remove("on"); st.front = back; st.cap.textContent = L(g.title); };
      nb.alt = L(g.title); nb.src = BASE + g.src;
    }
    var paused = false, reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    hv.addEventListener("mouseenter", function () { paused = true; });
    hv.addEventListener("mouseleave", function () { paused = false; });
    if (!reduce) setInterval(function () { if (!paused && !document.hidden) state.forEach(step); }, Math.max(2, +D.heroSlideSeconds || 5) * 1000);
  }

  var y = $("#year"); if (y) y.textContent = new Date().getFullYear();
})();
