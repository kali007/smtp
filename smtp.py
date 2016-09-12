#coding:utf-8
import smtplib  
from email.mime.text import MIMEText 

def sm(receiver, title, body):
        host = 'smtp.qq.com'
        port = 465
        sender = 'xxx@qq.com'
        pwd = 'xxx'

        msg = MIMEText(body, 'html')
        msg['subject'] = title
        msg['from'] = sender
        msg['to'] = receiver

        s = smtplib.SMTP_SSL(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())

        print 'The mail named %s to %s is sended successly.' % (title, receiver)
		
sm('收件人','标题','内容')