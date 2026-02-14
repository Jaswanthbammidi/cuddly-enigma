import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = "Scheduled Email from GitHub Actions"

    body = """Hello Team,

This is an automated email triggered from GitHub Actions.

Regards,
Automation Bot
"""
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        # Step 1: Identify ourselves
        server.ehlo()

        # Step 2: Secure connection
        server.starttls()

        # Step 3: Re-identify after TLS
        server.ehlo()

        # Step 4: Login
        server.login(EMAIL_FROM, EMAIL_PASSWORD)

        # Step 5: Send mail
        server.send_message(msg)

        server.quit()
        print("Email sent successfully")

    except Exception as e:
        print("Failed to send email")
        print(e)

if __name__ == "__main__":
    send_email()
