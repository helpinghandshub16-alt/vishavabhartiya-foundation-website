# Website forms — backend setup

The contact form and the 80G receipt request form work in two modes:

1. **Not connected (current):** `forms.endpoint` is empty. The website does NOT pretend to submit.
   It validates the form and then shows "nothing has been sent yet" with two buttons that open
   WhatsApp (+91 94236 32405) or email with the details pre-filled.
2. **Connected:** after deploying `google-apps-script.gs` (instructions inside the file) and pasting the
   Web-app URL into `CONFIG["forms"]["endpoint"]` (build.py) or `assets/js/config.js`, submissions are
   saved to a Google Sheet and emailed to the Foundation. If the online save fails, the same
   WhatsApp/email fallback is shown.

Spam protection: hidden honeypot field, 3-second minimum fill time, field validation (PAN, mobile, email, amount, date).

Payment-proof upload is not enabled (no file storage backend). Donors are asked to keep a screenshot.
