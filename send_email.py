import os

import sendgrid
from dotenv import load_dotenv
from sendgrid.helpers.mail import Content, Email, Mail, To

load_dotenv()

EMAIL_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>SendGrid Demo</title>
  <!--[if mso]>
  <style type="text/css">
    table { border-collapse: collapse; }
    .fallback-font { font-family: Arial, sans-serif !important; }
  </style>
  <![endif]-->
</head>
<body style="margin:0;padding:0;background-color:#0f1419;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color:#0f1419;">
    <tr>
      <td align="center" style="padding:40px 16px;">
        <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="max-width:600px;width:100%;border-radius:16px;overflow:hidden;box-shadow:0 24px 48px rgba(0,0,0,0.35);">
          <!-- Header -->
          <tr>
            <td style="background:linear-gradient(135deg,#1a56db 0%,#7c3aed 100%);background-color:#1a56db;padding:28px 32px;text-align:center;">
              <p style="margin:0;font-family:Georgia,'Times New Roman',serif;font-size:26px;font-weight:600;color:#ffffff;letter-spacing:-0.02em;">
                SendGrid Demo
              </p>
              <p style="margin:10px 0 0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(255,255,255,0.88);line-height:1.5;">
                A polished transactional-style message
              </p>
            </td>
          </tr>
          <!-- Hero image -->
          <tr>
            <td style="padding:0;line-height:0;">
              <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80"
                   alt="Modern workspace"
                   width="600"
                   style="display:block;width:100%;max-width:600px;height:auto;border:0;outline:none;text-decoration:none;">
            </td>
          </tr>
          <!-- Body -->
          <tr>
            <td style="background-color:#ffffff;padding:36px 32px 28px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
              <h1 style="margin:0 0 12px;font-size:22px;font-weight:700;color:#111827;line-height:1.3;letter-spacing:-0.02em;">
                Hello from your SendGrid demo
              </h1>
              <p style="margin:0 0 20px;font-size:16px;line-height:1.65;color:#4b5563;">
                This email uses table layout and inline styles so it renders consistently in Gmail,
                Outlook, Apple Mail, and other clients. Images load from the public web (Unsplash).
              </p>
              <!-- Feature row with small image -->
              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin:24px 0;">
                <tr>
                  <td width="120" valign="top" style="padding-right:16px;">
                    <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=240&q=80"
                         alt="Team collaboration"
                         width="120"
                         style="display:block;width:120px;max-width:100%;height:auto;border-radius:10px;border:0;">
                  </td>
                  <td valign="top" style="font-size:15px;line-height:1.6;color:#374151;">
                    <strong style="color:#111827;">Built for clarity</strong><br>
                    Short copy, strong hierarchy, and a single clear action help readers scan quickly on mobile and desktop.
                  </td>
                </tr>
              </table>
              <!-- CTA -->
              <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin:28px 0 8px;">
                <tr>
                  <td align="center" style="border-radius:10px;background:linear-gradient(135deg,#2563eb 0%,#7c3aed 100%);background-color:#2563eb;">
                    <a href="https://sendgrid.com" target="_blank" rel="noopener noreferrer"
                       style="display:inline-block;padding:14px 28px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;font-size:15px;font-weight:600;color:#ffffff;text-decoration:none;border-radius:10px;">
                      Explore SendGrid
                    </a>
                  </td>
                </tr>
              </table>
              <p style="margin:24px 0 0;font-size:13px;line-height:1.55;color:#9ca3af;">
                You are receiving this because this address is used in the sendgrid-demo project.
              </p>
            </td>
          </tr>
          <!-- Footer strip -->
          <tr>
            <td style="background-color:#f3f4f6;padding:20px 32px;text-align:center;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;font-size:12px;color:#6b7280;line-height:1.5;">
              <span style="color:#9ca3af;">Photos via</span>
              <a href="https://unsplash.com" style="color:#6366f1;text-decoration:none;">Unsplash</a>
              &nbsp;·&nbsp;
              <span style="color:#9ca3af;">©</span> Demo only
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
""".strip()


def main() -> None:
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        raise RuntimeError("SENDGRID_API_KEY is not set in the environment.")

    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    from_email = Email("kauamcm@gmail.com")
    to = To("kauamcm@gmail.com")
    subject = "SendGrid message demo — designed HTML"
    content = Content("text/html", EMAIL_HTML)
    mail = Mail(from_email, to, subject, content)

    mail_json = mail.get()
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)


if __name__ == "__main__":
    main()
