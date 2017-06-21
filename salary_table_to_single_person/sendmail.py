# coding = utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

msg = MIMEMultipart()

msg['From'] = 'FROM EMAIL ADDRESS'
msg['To'] = 'TO EMAIL ADDRESS'
att_file = 'FILE TO ATTCHMENT MAIL'

msg['Date'] = formatdate(localtime = True)
msg['Subject'] = '工资表'

part = MIMEBase('application', "octet-stream")
part.set_payload(open(att_file, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="sarlary.xlsx"')
msg.attach(part)

text = '本邮件为自动发送，若有任何疑问请与人事部联系，谢谢!'
part = MIMEText(text, 'plain', _charset='utf-8')
msg.attach(MIMEText(text))

smtp_server = 'SMTP SERVER DOMIAN'
stmp_user = "LOGIN_USER"
smtp_password = "LOGIN_PASSWORD"

smtp = smtplib.SMTP(smtp_server)
smtp.login(stmp_user,smtp_password)
smtp.sendmail(msg['From'], msg['To'], msg.as_string())
smtp.quit()
