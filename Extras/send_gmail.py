import os
import smtplib
from email.mime.text import MIMEText

gmail_user = os.environ['GMAIL_USER']
gmail_app_password = os.environ['GMAIL_APP_PASSWORD']
to_email = os.environ.get('TO_EMAIL', gmail_user)  # Default to self
subject = os.environ.get('EMAIL_SUBJECT', 'Test Email from GitHub Actions')
body = os.environ.get('EMAIL_BODY', 'Hello from your GitHub Action!')

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = gmail_user
msg['To'] = to_email

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(gmail_user, gmail_app_password)
        server.sendmail(gmail_user, [to_email], msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
    exit(1)
