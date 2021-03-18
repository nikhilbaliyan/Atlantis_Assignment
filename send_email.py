import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email():
    def __init__(self, subject, body, recipient_email):
        self.subject = subject
        self.body = body
        self.recipient_email = recipient_email

    def send_email(self):
        email_user = 'nikhilbaliyan113@gmail.com'
        email_password = 'sender_password'
        email_send = self.recipient_email
        subject = self.subject
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        body = self.body
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, text)
        server.quit()


if __name__ == '__main__':
    subject = input('Enter subject: ')
    body = input('Enter body: ')
    recipient_email = input('Enter email of recipient: ')
    email = Email(subject, body, recipient_email)
    email.send_email()
