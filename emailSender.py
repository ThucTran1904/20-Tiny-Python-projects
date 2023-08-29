from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'thuc.tran.data@gmail.com'
email_password = password
email_receiver = 'cuong.le322002@gmail.com'

subject = "DCME"
body = """
Dear Ms Thuy,

I would like to send you the internship report for the 28 week.

Thanks for your contributions,

Have an enjoyable weekend,

Sincerely,
em Thuc
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())