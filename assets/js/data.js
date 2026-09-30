/* =====================================================================
   VISHAVABHARTIYA FOUNDATION — WEBSITE CONTENT FILE (English + हिंदी)
   ---------------------------------------------------------------------
   नई गतिविधि, अख़बार कवरेज, फ़ोटो या पुरस्कार जोड़ने के लिए केवल यही फ़ाइल बदलें।
   To add a new activity, news clipping, photo or award, edit ONLY this file:
     1. Upload the photo (WebP or JPG) to assets/img/gallery, /media or /awards.
     2. Copy one { ... } block, paste it at the TOP of its list, change the text.
        Every text has an English (en) and Hindi (hi) version.
     3. Dates are YYYY-MM-DD. Newest items appear first automatically.
   Gallery "era":  "foundation" = Vishavabhartiya Foundation activity (from 12 Mar 2026)
                   "legacy"     = founder / earlier Sanstha activity (1998–2025)
   Partner photos go ONLY in the "partners" list, never in "gallery".
   ===================================================================== */

window.VBF = {

  /* Home page photo slideshow: seconds each photo stays before changing */
  heroSlideSeconds: 5,

  /* ---------- Latest activities & announcements ---------- */
  activities: [
    { date: "2026-10-10", upcoming: true, img: "assets/img/awards/global-sustainability-2026.webp",
      tag: { en: "Founder's honour", hi: "संस्थापक सम्मान" },
      title: { en: "Founder named winner, Global Sustainability Awards 2026 — Individual Changemaker",
               hi: "संस्थापक को ग्लोबल सस्टेनेबिलिटी अवॉर्ड्स 2026 — इंडिविजुअल चेंजमेकर श्रेणी में विजेता घोषित" },
      text: { en: "Dr. Dhananjay K. Yerne, MD & CEO, is recognised for health-awareness work in Nagpur and Bhandara districts since 1998. The award is to be presented at Miranda House, University of Delhi.",
              hi: "एमडी एवं सीईओ डॉ. धनंजय के. येरने को नागपुर और भंडारा ज़िलों में 1998 से स्वास्थ्य-जागरूकता कार्य के लिए चुना गया है। पुरस्कार मिरांडा हाउस, दिल्ली विश्वविद्यालय में प्रदान किया जाना है।" } },
    { date: "2026-06-21", img: "assets/img/gallery/yoga-day-2026.webp",
      tag: { en: "Health", hi: "स्वास्थ्य" },
      title: { en: "International Yoga Day celebrated with citizens of all ages", hi: "सभी आयु वर्ग के नागरिकों के साथ अंतर्राष्ट्रीय योग दिवस" },
      text: { en: "A community yoga session on building a healthy nation through daily practice, organised with Hindurashtra Sangh. Reported by The Hitavada, Nagpur, 22 June 2026.",
              hi: "दैनिक योग से स्वस्थ राष्ट्र निर्माण विषय पर सामुदायिक योग सत्र, हिंदूराष्ट्र संघ के साथ आयोजित। द हितवाद, नागपुर में 22 जून 2026 को प्रकाशित।" } },
    { date: "2026-04-22", img: "assets/img/gallery/earth-day-2026.webp",
      tag: { en: "Environment", hi: "पर्यावरण" },
      title: { en: "Earth Day: “If the Earth is not saved, nothing will remain”", hi: "पृथ्वी दिवस: “धरा नहीं बची तो सब धरा रह जाएगा”" },
      text: { en: "Students and volunteers pledged to plant trees, cut plastic use and take collective responsibility for the environment.",
              hi: "विद्यार्थियों और स्वयंसेवकों ने पेड़ लगाने, प्लास्टिक कम करने और पर्यावरण के प्रति सामूहिक ज़िम्मेदारी का संकल्प लिया।" } },
    { date: "2026-04-07", img: "assets/img/docs/csr-1-registration.webp",
      tag: { en: "Registration", hi: "पंजीकरण" },
      title: { en: "Registered with MCA to undertake CSR activities (CSR-1)", hi: "CSR गतिविधियों हेतु कॉर्पोरेट कार्य मंत्रालय में पंजीकरण (CSR-1)" },
      text: { en: "Registration number CSR00109367 allows companies to partner with the Foundation for CSR projects.",
              hi: "पंजीकरण संख्या CSR00109367 के ज़रिए कंपनियाँ CSR परियोजनाओं के लिए फाउंडेशन के साथ साझेदारी कर सकती हैं।" } },
    { date: "2026-03-30", img: "assets/img/docs/80g-provisional.webp",
      tag: { en: "Tax exemption", hi: "कर छूट" },
      title: { en: "12A registration and 80G approval granted (provisional)", hi: "12A पंजीकरण और 80G अनुमोदन प्राप्त (अस्थायी)" },
      text: { en: "Granted by the Income Tax Department for AY 2026-27 to AY 2028-29. Donors can claim tax benefit as per law.",
              hi: "आयकर विभाग द्वारा निर्धारण वर्ष 2026-27 से 2028-29 के लिए प्रदान। दानदाता नियमानुसार कर-लाभ ले सकते हैं।" } },
    { date: "2026-03-14", img: "assets/img/docs/ngo-darpan.webp",
      tag: { en: "Registration", hi: "पंजीकरण" },
      title: { en: "Listed on NITI Aayog NGO Darpan and e-Anudaan", hi: "नीति आयोग NGO दर्पण और ई-अनुदान पोर्टल पर पंजीकृत" },
      text: { en: "Unique ID MH/2026/1028763 on NGO Darpan and NGO ID MH/00054145 on the e-Anudaan portal.",
              hi: "NGO दर्पण यूनिक आईडी MH/2026/1028763 तथा ई-अनुदान NGO आईडी MH/00054145।" } },
    { date: "2026-03-12", img: "assets/img/docs/certificate-of-incorporation.webp",
      tag: { en: "Milestone", hi: "उपलब्धि" },
      title: { en: "Vishavabhartiya Foundation incorporated as a Section 8 company", hi: "विश्वभारतीय फाउंडेशन Section 8 कंपनी के रूप में स्थापित" },
      text: { en: "Incorporated under the Companies Act, 2013 (CIN U88900ME2026NPL473814; Section 8 Licence No. 181714).",
              hi: "कंपनी अधिनियम, 2013 के अंतर्गत स्थापना (CIN U88900ME2026NPL473814; Section 8 लाइसेंस संख्या 181714)।" } }
  ],

  /* ---------- Media coverage ---------- */
  media: [
    { date: "2026-06-22", img: "assets/img/media/hitavada-yoga-day-2026.webp",
      paper: { en: "The Hitavada, Nagpur (p. 7)", hi: "द हितवाद, नागपुर (पृ. 7)" },
      title: { en: "International Yog Day — Vishavabhartiya Foundation", hi: "अंतर्राष्ट्रीय योग दिवस — विश्वभारतीय फाउंडेशन" },
      text: { en: "Citizens of all age groups took part; office bearers spoke about making yoga part of daily life.", hi: "सभी आयु वर्ग के नागरिक शामिल हुए; पदाधिकारियों ने योग को दैनिक जीवन का हिस्सा बनाने पर बल दिया।" } },
    { date: "2026-04-23", img: "assets/img/media/earth-day-2026-hindi.webp",
      paper: { en: "Nagpur edition (Hindi daily)", hi: "नागपुर संस्करण (हिंदी दैनिक)" },
      title: { en: "धरा नहीं बची तो सब धरा रह जाएगा : येरने", hi: "धरा नहीं बची तो सब धरा रह जाएगा : येरने" },
      text: { en: "Dr. Dhananjay Yerne's Earth Day address urging citizens to give up plastic and plant more trees.", hi: "पृथ्वी दिवस पर डॉ. धनंजय येरने का प्लास्टिक त्यागने और अधिक पेड़ लगाने का आह्वान।" } },
    { date: "2026-04-23", img: "assets/img/media/earth-day-2026-english.webp",
      paper: { en: "Nagpur edition (English daily)", hi: "नागपुर संस्करण (अंग्रेज़ी दैनिक)" },
      title: { en: "Foundation marks Earth Day with a call to protect the environment", hi: "पृथ्वी दिवस पर पर्यावरण संरक्षण का आह्वान" },
      text: { en: "Speakers highlighted pollution, global warming and plastic waste.", hi: "वक्ताओं ने प्रदूषण, ग्लोबल वार्मिंग और प्लास्टिक कचरे पर चिंता जताई।" } },
    { date: "2025-12-28", img: "assets/img/media/lokmat-vidarbha-bhushan.webp",
      paper: { en: "Lokmat", hi: "लोकमत" },
      title: { en: "Vidarbha Bhushan honour for the founder's social work", hi: "संस्थापक के सामाजिक कार्य के लिए विदर्भ भूषण सम्मान" },
      text: { en: "Coverage of the Vidyabhushan Foundation felicitation of Dr. D. K. Yerne.", hi: "विद्याभूषण फाउंडेशन द्वारा डॉ. डी. के. येरने के सत्कार का समाचार।" } },
    { date: "2004-08-08", when: { en: "8 Aug 2004", hi: "8 अगस्त 2004" }, img: "assets/img/media/city-bus-service.webp", legacy: true,
      paper: { en: "Dainik Bhaskar (archive)", hi: "दैनिक भास्कर (पुराना संग्रह)" },
      title: { en: "New city bus service for Venkatesh Nagar", hi: "वेंकटेश नगर के लिए नई सिटी बस सेवा" },
      text: { en: "Follow-up to the founder's team campaign for bus connectivity to outskirts and labour colonies.", hi: "बाहरी बस्तियों और मज़दूर कॉलोनियों तक बस सुविधा के लिए संस्थापक की टीम के अभियान का परिणाम।" } },
    { date: "2004-01-01", when: { en: "2004", hi: "2004" }, img: "assets/img/media/aids-guidance-camp.webp", legacy: true,
      paper: { en: "Archive clipping", hi: "पुरानी कतरन" },
      title: { en: "AIDS guidance camp organised", hi: "एड्स पर मार्गदर्शन शिविर का आयोजन" },
      text: { en: "Awareness camp by the earlier organisation, Vishvabhartiya Manav Kalyan Sewa Sanstha.", hi: "पूर्ववर्ती संस्था विश्वभारतीय मानव कल्याण सेवा संस्था द्वारा जागरूकता शिविर।" } },
    { date: "2003-01-01", when: { en: "Archive", hi: "पुराना संग्रह" }, img: "assets/img/media/voter-registration-drive.webp", legacy: true,
      paper: { en: "Archive clipping", hi: "पुरानी कतरन" },
      title: { en: "Good response to voter registration drive in East Nagpur", hi: "पूर्व नागपुर में मतदाता पंजीयन अभियान को अच्छा प्रतिसाद" },
      text: { en: "Voter enrolment awareness camp run by the founder's team.", hi: "संस्थापक की टीम द्वारा मतदाता पंजीयन जागरूकता शिविर।" } },
    { date: "2002-01-01", when: { en: "Archive", hi: "पुराना संग्रह" }, img: "assets/img/media/polio-drive-dainik-bhaskar.webp", legacy: true,
      paper: { en: "Dainik Bhaskar (archive)", hi: "दैनिक भास्कर (पुराना संग्रह)" },
      title: { en: "बच्चों ने उत्साह से पी पोलियो की दवा", hi: "बच्चों ने उत्साह से पी पोलियो की दवा" },
      text: { en: "Pulse Polio day coverage; the founder's team volunteered in the NMC polio drive from 1998 to 2023.", hi: "पल्स पोलियो दिवस का समाचार; संस्थापक की टीम ने 1998 से 2023 तक मनपा पोलियो अभियान में सेवा दी।" } }
  ],

  /* ---------- Photo gallery (Foundation + founder legacy; NO partner photos here) ---------- */
  gallery: [
    { src: "assets/img/gallery/yoga-day-2026.webp", cat: "health", era: "foundation",
      title: { en: "International Yoga Day 2026", hi: "अंतर्राष्ट्रीय योग दिवस 2026" }, caption: { en: "Community yoga session, Nagpur", hi: "सामुदायिक योग सत्र, नागपुर" } },
    { src: "assets/img/gallery/earth-day-2026.webp", cat: "environment", era: "foundation",
      title: { en: "Earth Day 2026", hi: "पृथ्वी दिवस 2026" }, caption: { en: "Students and volunteers take the green pledge", hi: "विद्यार्थियों और स्वयंसेवकों का हरित संकल्प" } },
    { src: "assets/img/gallery/eye-camp-screening.webp", cat: "health", era: "legacy",
      title: { en: "Mega eye check-up camp", hi: "भव्य नेत्र जाँच शिविर" }, caption: { en: "Free eye screening (founder's earlier Sanstha)", hi: "निःशुल्क नेत्र जाँच (संस्थापक की पूर्ववर्ती संस्था)" } },
    { src: "assets/img/gallery/eye-camp-team.webp", cat: "health", era: "legacy",
      title: { en: "Eye camp team", hi: "नेत्र शिविर टीम" }, caption: { en: "Volunteers and optometry staff at a camp", hi: "शिविर में स्वयंसेवक और नेत्र-जाँच टीम" } },
    { src: "assets/img/gallery/pulse-polio-drops.webp", cat: "health", era: "legacy",
      title: { en: "Pulse Polio drive", hi: "पल्स पोलियो अभियान" }, caption: { en: "Polio drops for children, Nagpur", hi: "बच्चों को पोलियो की खुराक, नागपुर" } },
    { src: "assets/img/gallery/pulse-polio-booth.webp", cat: "health", era: "legacy",
      title: { en: "Pulse Polio booth", hi: "पल्स पोलियो बूथ" }, caption: { en: "Supporting the NMC immunisation programme", hi: "मनपा टीकाकरण कार्यक्रम में सहयोग" } },
    { src: "assets/img/gallery/mother-child-centre.webp", cat: "women", era: "legacy",
      title: { en: "Mother & child health centre", hi: "माता एवं बाल स्वास्थ्य केंद्र" }, caption: { en: "Opened 1 May 1998, Kharbi Road, Nagpur", hi: "1 मई 1998 को खरबी रोड, नागपुर में शुरू" } },
    { src: "assets/img/gallery/public-hospital-inauguration.webp", cat: "women", era: "legacy",
      title: { en: "Public hospital signboard", hi: "सार्वजनिक अस्पताल का फलक" }, caption: { en: "Primary health care centre, Kharbi Road", hi: "प्राथमिक स्वास्थ्य केंद्र, खरबी रोड" } },
    { src: "assets/img/gallery/school-awareness-programme.webp", cat: "education", era: "legacy",
      title: { en: "School awareness programme", hi: "विद्यालय जागरूकता कार्यक्रम" }, caption: { en: "Mass session and prize distribution", hi: "सामूहिक सत्र और पुरस्कार वितरण" } },
    { src: "assets/img/gallery/prize-distribution.webp", cat: "education", era: "legacy",
      title: { en: "Prize distribution", hi: "पुरस्कार वितरण" }, caption: { en: "Essay and drawing competition winners", hi: "निबंध एवं चित्रकला प्रतियोगिता विजेता" } },
    { src: "assets/img/gallery/students-felicitation.webp", cat: "education", era: "legacy",
      title: { en: "Student felicitation", hi: "विद्यार्थी सम्मान" }, caption: { en: "Recognising students for awareness work", hi: "जागरूकता कार्य के लिए विद्यार्थियों का सम्मान" } },
    { src: "assets/img/gallery/awareness-session-children.webp", cat: "community", era: "legacy",
      title: { en: "Awareness session", hi: "जागरूकता सत्र" }, caption: { en: "Outdoor session for schoolchildren", hi: "स्कूली बच्चों के लिए खुला सत्र" } },
    { src: "assets/img/gallery/community-event-lamp.webp", cat: "community", era: "legacy",
      title: { en: "Community programme", hi: "सामुदायिक कार्यक्रम" }, caption: { en: "Lamp lighting at a public event", hi: "सार्वजनिक कार्यक्रम में दीप प्रज्वलन" } }
  ],

  /* ---------- Partner field activities (YKVM, Uttar Pradesh) — shown separately, never as Foundation work ---------- */
  partners: [
    { src: "assets/img/partner/youth-training.webp", title: { en: "Youth skill training session", hi: "युवा कौशल प्रशिक्षण सत्र" } },
    { src: "assets/img/partner/village-youth-session.webp", title: { en: "Village youth awareness session", hi: "ग्रामीण युवा जागरूकता सत्र" } },
    { src: "assets/img/partner/organic-compost-unit.webp", title: { en: "Organic compost production unit", hi: "जैविक खाद उत्पादन इकाई" } },
    { src: "assets/img/partner/fpo-outlet-visit.webp", title: { en: "Farmer producer company outlet visit", hi: "किसान उत्पादक कंपनी आउटलेट भ्रमण" } },
    { src: "assets/img/partner/fpo-organic-products.webp", title: { en: "Organic products made by farmer groups", hi: "किसान समूहों के जैविक उत्पाद" } },
    { src: "assets/img/partner/agri-input-centre.webp", title: { en: "Agri-input centre for farmers", hi: "किसानों के लिए कृषि-इनपुट केंद्र" } },
    { src: "assets/img/partner/floriculture-exposure-visit.webp", title: { en: "Floriculture exposure visit", hi: "पुष्प-उत्पादन अध्ययन भ्रमण" } },
    { src: "assets/img/partner/handpump-soak-pit.webp", title: { en: "Handpump platform and soak pit", hi: "हैंडपंप चबूतरा और सोख्ता गड्ढा" } },
    { src: "assets/img/partner/traditional-farming.webp", title: { en: "Field work with farmers", hi: "किसानों के साथ खेत पर कार्य" } },
    { src: "assets/img/partner/gram-panchayat-meeting.webp", title: { en: "Gram panchayat committee meeting", hi: "ग्राम पंचायत समिति बैठक" } }
  ],

  /* ---------- OUR PARTNERS (About page) ----------
     To add a logo: put a square PNG/WebP (min 200×200, transparent background) in assets/img/partners/
     and write its path in "logo". Use a logo only with the organisation's permission.
     Without a logo, initials are shown automatically.
     group: "current" = partner of the Foundation (2026 →) · "legacy" = collaborated with the founder / earlier Sanstha */
  partnerOrgs: [
    { group: "current", initials: "YKVM", logo: "assets/img/partners/ykvm.webp",
      name: { en: "Yuva Kaushal Vikas Mandal (YKVM)", hi: "युवा कौशल विकास मण्डल (YKVM)" },
      role: { en: "Programme partner · Uttar Pradesh", hi: "कार्यक्रम साझेदार · उत्तर प्रदेश" },
      text: { en: "Farmer, youth, water and panchayat programmes in Hamirpur and Banda districts, with online support from our team.", hi: "हमीरपुर एवं बांदा ज़िलों में किसान, युवा, जल एवं पंचायत कार्यक्रम, हमारी टीम के ऑनलाइन सहयोग के साथ।" } },
    { group: "current", initials: "HS", logo: "",
      name: { en: "Hindurashtra Sangh", hi: "हिंदूराष्ट्र संघ" },
      role: { en: "Programme collaborator · 2026", hi: "कार्यक्रम सहयोगी · 2026" },
      text: { en: "Co-organised the International Yoga Day programme, 21 June 2026, Nagpur.", hi: "21 जून 2026 को नागपुर में अंतर्राष्ट्रीय योग दिवस कार्यक्रम का सह-आयोजन।" } },
    { group: "current", initials: "CAI", logo: "assets/img/partners/collective-action-india.webp",
      name: { en: "Collective Action India", hi: "कलेक्टिव एक्शन इंडिया" },
      role: { en: "Capacity-building / training partner · 2026", hi: "क्षमता निर्माण / प्रशिक्षण साझेदार · 2026" },
      text: { en: "6-day master class on grant readiness and fundraising (CSR strategy, government grants, proposal writing), 16–21 March 2026.", hi: "ग्रांट-रेडीनेस एवं फंडरेज़िंग पर 6 दिवसीय मास्टर क्लास (CSR रणनीति, सरकारी अनुदान, प्रस्ताव लेखन), 16–21 मार्च 2026।" } },
    { group: "legacy", initials: "NMC", logo: "",
      name: { en: "Nagpur Municipal Corporation", hi: "नागपुर महानगरपालिका" },
      role: { en: "Pulse Polio programme · 1998–2023", hi: "पल्स पोलियो कार्यक्रम · 1998–2023" },
      text: { en: "The founder's team volunteered in the NMC Pulse Polio immunisation drive every year.", hi: "संस्थापक की टीम ने हर वर्ष मनपा पल्स पोलियो टीकाकरण अभियान में स्वयंसेवा की।" } },
    { group: "legacy", initials: "AI", logo: "",
      name: { en: "ALERT India & ANESVAD Foundation", hi: "ALERT इंडिया एवं ANESVAD फाउंडेशन" },
      role: { en: "Leprosy Elimination Action Programme (LEAP)", hi: "कुष्ठरोग उन्मूलन कार्य कार्यक्रम (LEAP)" },
      text: { en: "Community volunteer training across villages of Bhandara district.", hi: "भंडारा ज़िले के गाँवों में सामुदायिक स्वयंसेवक प्रशिक्षण।" } },
    { group: "legacy", initials: "UC", logo: "",
      name: { en: "UNESCO Club, Nagpur", hi: "यूनेस्को क्लब, नागपुर" },
      role: { en: "Personality development camp · 2004", hi: "व्यक्तित्व विकास शिविर · 2004" },
      text: { en: "Jointly organised a personality development camp for youth.", hi: "युवाओं के लिए व्यक्तित्व विकास शिविर का संयुक्त आयोजन।" } },
    { group: "legacy", initials: "MVP", logo: "",
      name: { en: "Marathi Vigyan Parishad", hi: "मराठी विज्ञान परिषद" },
      role: { en: "Science & environment fair · 2005", hi: "विज्ञान एवं पर्यावरण मेला · 2005" },
      text: { en: "Participation in a science and environment fair for students.", hi: "विद्यार्थियों के लिए विज्ञान एवं पर्यावरण मेले में सहभागिता।" } }
  ],

  /* ---------- Partner logo strip (About page, "Our Partners") — add/remove logos here ---------- */
  partnerLogos: [
    { name: "Yuva Kaushal Vikas Mandal (YKVM)", logo: "assets/img/partners/ykvm.webp" },
    { name: "Bandhan Bank", logo: "assets/img/partners/bandhan-bank.webp" },
    { name: "ICAR – Krishi Vigyan Kendra", logo: "assets/img/partners/icar-kvk.webp" },
    { name: "Joint Empowerment Venture Action Foundation (JEVAF)", logo: "assets/img/partners/jevaf.webp" },
    { name: "Collective Action India", logo: "assets/img/partners/collective-action-india.webp", style: "d3" },
    { name: "HDFC Bank", logo: "assets/img/partners/hdfc-bank.webp" },
    { name: "Samunnati", logo: "assets/img/partners/samunnati.webp" },
    { name: "Punjab National Bank", logo: "assets/img/partners/pnb.webp" }
  ],

  /* ---------- Founder's Honours & Recognition (personal awards of Dr. D. K. Yerne) ---------- */
  honours: [
    { year: "2026", img: "assets/img/awards/global-sustainability-2026.webp",
      title: { en: "Global Sustainability Awards 2026 — Winner, Individual Changemaker", hi: "ग्लोबल सस्टेनेबिलिटी अवॉर्ड्स 2026 — विजेता, इंडिविजुअल चेंजमेकर" },
      by: { en: "Global Awards · to be presented 10 Oct 2026, Miranda House, University of Delhi", hi: "ग्लोबल अवॉर्ड्स · 10 अक्टूबर 2026 को मिरांडा हाउस, दिल्ली विश्वविद्यालय में प्रदान किया जाना है" },
      text: { en: "For health-awareness programmes in Nagpur and Bhandara districts from 1998 to 2026.", hi: "नागपुर और भंडारा ज़िलों में 1998 से 2026 तक स्वास्थ्य-जागरूकता कार्यक्रमों के लिए।" } },
    { year: "2026", img: "assets/img/awards/vidyavachaspati-2026.webp",
      title: { en: "Vidyavachaspati (Honorary Doctorate) — Saraswat Samman", hi: "विद्यावाचस्पति (मानद उपाधि) — सारस्वत सम्मान" },
      by: { en: "Pandit Deendayal Upadhyay Hindi Vidyapeeth, Vrindavan Dham, Mathura · 1 Feb 2026", hi: "पंडित दीनदयाल उपाध्याय हिंदी विद्यापीठ, वृंदावन धाम, मथुरा · 1 फ़रवरी 2026" },
      text: { en: "Conferred in recognition of social service.", hi: "समाज सेवा के सम्मान में प्रदान।" } },
    { year: "2025", img: "assets/img/awards/vidarbha-bhushan-2025.webp",
      title: { en: "Vidarbha Bhushan Award 2025", hi: "विदर्भ भूषण पुरस्कार 2025" },
      by: { en: "Vidyabhushan Foundation · 28 Dec 2025", hi: "विद्याभूषण फाउंडेशन · 28 दिसंबर 2025" },
      text: { en: "For outstanding contribution in the field of social work.", hi: "सामाजिक कार्य के क्षेत्र में उल्लेखनीय योगदान के लिए।" } }
  ],

  /* ---------- Professional recognition (founder) ---------- */
  recognition: [
    { year: "—", img: "assets/img/awards/gopha-certificate.webp",
      title: { en: "Certificate of Participation — GOPHA", hi: "सहभागिता प्रमाणपत्र — GOPHA" },
      by: { en: "Global Optometry Public Health Alliance", hi: "ग्लोबल ऑप्टोमेट्री पब्लिक हेल्थ अलायंस" },
      text: { en: "Participation in public eye-health initiatives.", hi: "सार्वजनिक नेत्र-स्वास्थ्य पहल में सहभागिता।" } }
  ],

  /* ---------- Capacity building / training ---------- */
  training: [
    { year: "2026", img: "assets/img/awards/collective-action-india-2026.webp",
      title: { en: "Grant-Ready NGO Master Class — Certificate of Completion", hi: "ग्रांट-रेडी NGO मास्टर क्लास — पूर्णता प्रमाणपत्र" },
      by: { en: "Collective Action India · 16–21 Mar 2026 · ID CAI-GRANTREADY-2026-027", hi: "कलेक्टिव एक्शन इंडिया · 16–21 मार्च 2026 · आईडी CAI-GRANTREADY-2026-027" },
      text: { en: "Completed by Dr. D. K. Yerne on behalf of the Foundation: CSR funding, government grants, proposal writing.", hi: "फाउंडेशन की ओर से डॉ. डी. के. येरने द्वारा: CSR फंडिंग, सरकारी अनुदान, प्रस्ताव लेखन।" } }
  ]
};
