from email.message import EmailMessage
from env import password
import ssl
import smtplib

email_sender = 'huzaifamk@gmail.com'
email_password = password

email_receiver = ''

subject = 'Test Email'
body = 'This is a test email'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendemail(email_sender, email_receiver, em.as_string())