"""
Function to send emails
Works when sender is gmail
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email(object):
    def __init__(self, sender_gmail, password):
        self.sender_gmail = sender_gmail
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.sender_gmail, self.password)

    def send(self, dest_email, subject, msg):
        body = MIMEMultipart()
        body['From'] = self.sender_gmail
        body['To'] = dest_email
        body['Subject'] = subject
        body.attach(MIMEText(msg, 'plain'))
        
        self.server.sendmail(self.sender_gmail, dest_email, body.as_string())

    def close(self):
        self.server.quit()

if __name__ == '__main__':
    e = Email('server3.dreamteam@gmail.com', 'dream.mst')
    e.send('server3.dreamteam@gmail.com', 'test', 'this is a test')

