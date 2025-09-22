#这个包叫做simple transfer protocal 简单邮件传输协议

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#建立一个邮箱
smtp=smtplib.SMTP()
username='lihao960603@outlook.com'
password='201314lh'     #这里要给专项密码
sender='lihao960603@outlook.com'
receiver='lihao603@outlook.com'
#设置邮件内容
msg=MIMEMultipart('mixed')
msg['Subject']='test'
msg['From']='lihao'
msg['To']='lihao603@outlook.com'

html='''
<html><head>
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Dgb2312">
<style type=3D"text/css" style=3D"display:none;"> P {margin-top:0;margin-bo=
ttom:0;} </style>
</head>
<body dir=3D"ltr">
<div style=3D"font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, =
Calibri, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0);" clas=
s=3D"elementToProof">
=C4=E3=BA=C3=A3=BA</div>
<div style=3D"font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, =
Calibri, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0);" clas=
s=3D"elementToProof">
=D4=D9=BC=FB</div>
</body>
</html>
'''

text_html=MIMEText(html,'html','utf-8')
msg.attach(text_html)
#设置服务器和端口
smtp.connect("smtp.office365.com", 587)

#登录邮箱
smtp.login(username,password)

#发送邮件：设置发件人，收件人和邮件内容
smtp.sendmail(sender,receiver,msg.as_string())

#退出邮箱
smtp.quit()