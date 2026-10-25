/**
 * Vishavabhartiya Foundation — form backend (Google Apps Script)
 * Saves website form submissions (contact + 80G receipt request) to a Google Sheet
 * and emails a copy to the Foundation.
 *
 * SETUP (one time, ~10 minutes):
 *  1. Create a Google Sheet named "VBF Website Forms" in the Foundation's Google account.
 *  2. Extensions → Apps Script → paste this file → set NOTIFY_EMAIL below → Save.
 *  3. Deploy → New deployment → type "Web app" → Execute as: Me → Who has access: Anyone → Deploy.
 *  4. Copy the Web app URL and paste it into CONFIG["forms"]["endpoint"] in build.py
 *     (or directly into assets/js/config.js → forms.endpoint). Re-upload config.js.
 *  5. Test both forms on the live site; check the Sheet and the notification email.
 */
var NOTIFY_EMAIL = "vishavabhartiya.foundation@gmail.com";   // TODO: change to csr@/donations@ once domain email is live
var ALLOWED = ["contact", "receipt-80g"];

function doPost(e) {
  try {
    var p = e.parameter || {};
    if (p.website) return out_({ ok: true });                       // honeypot: silently ignore bots
    if (ALLOWED.indexOf(p.form) < 0) return out_({ ok: false, error: "unknown form" });
    var lock = LockService.getScriptLock(); lock.waitLock(10000);
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sh = ss.getSheetByName(p.form) || ss.insertSheet(p.form);
    var keys = Object.keys(p).filter(function (k) { return k !== "website"; }).sort();
    if (sh.getLastRow() === 0) sh.appendRow(["received_at"].concat(keys));
    var head = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0];
    keys.forEach(function (k) { if (head.indexOf(k) < 0) { head.push(k); sh.getRange(1, head.length).setValue(k); } });
    sh.appendRow(head.map(function (h) { return h === "received_at" ? new Date() : String(p[h] || "").slice(0, 2000); }));
    lock.releaseLock();
    var body = keys.map(function (k) { return k + ": " + p[k]; }).join("\n");
    MailApp.sendEmail(NOTIFY_EMAIL, "[Website] " + p.form + " — " + (p.name || p.donor_name || ""), body);
    return out_({ ok: true });
  } catch (err) {
    return out_({ ok: false, error: String(err) });
  }
}
function out_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
