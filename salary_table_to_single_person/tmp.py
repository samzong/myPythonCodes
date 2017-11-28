import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from email.mime.application import MIMEApplication

smtplib.SMTP()

msg = MIMEMultipart()
user_mail = '573578678@qq.com'
filename = '工资单.xlsx'
tfile = "/Users/Alex/GitHub/myPythonCodes/salary_table_to_single_person/money.xlsx"
print(tfile)

# att1 = MIMEMultipart(open(tfile,'rb').read(), 'base64', 'gb2312')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename=%s' % filename
# msg.attach(att1)

msg['From'] = 'lucj@visionet.com.cn'
msg['To'] = user_mail
msg['Date'] = formatdate(localtime = True)
msg['Subject'] = '工资表'
# msg.attach(MIMEText(file("/Users/Alex/GitHub/myPythonCodes/salary_table_to_single_person/money.xlsx").read(), 'base64', 'gb2312'))

part = MIMEBase('application', "octet-stream")
part = MIMEApplication(open("/Users/Alex/GitHub/myPythonCodes/salary_table_to_single_person/money.xlsx",'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="aaaa.xlsx"')
msg.attach(part)

text = '本邮件为自动发送，若有任何疑问请与人事部联系，谢谢！'
part = MIMEText(text, 'plain', _charset='utf-8')
msg.attach(MIMEText(text))
msg.attach(part)

smtp = smtplib.SMTP('smtp.263.net')
smtp.login('lucj@visionet.com.cn','Lcj921010')
smtp.sendmail('lucj@visionet.com.cn', user_mail, msg.as_string())
smtp.quit()
