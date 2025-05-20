import os
import smtplib
import time
from email.mime.text import MIMEText

gmail_user = os.environ['GMAIL_USER']
gmail_app_password = os.environ['GMAIL_APP_PASSWORD']
to_email = os.environ.get('TO_EMAIL', gmail_user)
subject = os.environ.get('EMAIL_SUBJECT', 'Test Email from GitHub Actions')
body = os.environ.get('EMAIL_BODY', 'Hello from your GitHub Action!')
repeat_count = int(os.environ.get('REPEAT_COUNT', 1))
interval_seconds = int(os.environ.get('INTERVAL_SECONDS', 60))

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = gmail_user
msg['To'] = to_email

for i in range(repeat_count):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(gmail_user, gmail_app_password)
            server.sendmail(gmail_user, [to_email], msg.as_string())
        print(f"Email {i+1} sent successfully!")
    except Exception as e:
        print(f"Failed to send email {i+1}: {e}")
    if i < repeat_count - 1:
        time.sleep(interval_seconds)
