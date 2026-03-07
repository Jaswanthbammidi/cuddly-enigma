import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Read from GitHub Secrets / Environment Variables
EMAIL_FROM = "bvenkatasaijaswanth@gmail.com"
EMAIL_TO = [
    "vbammidi@gitam.in",
    "bvudadhu@gitam.in",
    "pkilli@gitam.in",
    "bsahu@gitam.in"

]
EMAIL_PASSWORD = "simwpeuckldgfjew"

def send_email():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = ", ".join(EMAIL_TO)
    msg["Subject"] = "Message to My Dearest Friend"

    body = """
Hi Broooooooooooo,

Time ayendiiii padukoooo brooooo.

Regards,
Ojas Gambheera
"""

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)

        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Failed to send email")
        print(str(e))

if __name__ == "__main__":
    send_email()
