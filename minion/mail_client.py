import smtplib
from email.message import EmailMessage
from minion import MinionConfig


class MailClient:

    def __init__(self, to):
        self.to = to

    def send(self, txt):
        '''txt: string;
        '''
        print('send result to {}'.format(self.to))
        msg = EmailMessage()
        msg.set_content(txt)
        msg['Subject'] = 'Minion: Job Finished'
        msg['From'] = MinionConfig.mail_from
        msg['To'] = self.to

        s = smtplib.SMTP('localhost')
        s.ehlo()
        s.send_message(msg)
        s.quit()
