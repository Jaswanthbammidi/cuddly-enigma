import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Read from GitHub Secrets / Environment Variables
EMAIL_FROM = "bvenkatasaijaswanth@gmail.com"
EMAIL_TO = "sankarakhil143@gmail.com"
EMAIL_PASSWORD = "simwpeuckldgfjew"

def send_email():
    # Create email
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = "Scheduled Email from GitHub Actions"

    body = """
Hi Team,

This is an automated email triggered by GitHub Actions using a scheduled pipeline.

Regards,
Automation Bot
"""

    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Failed to send email")
        print(str(e))

if __name__ == "__main__":
    send_email()
