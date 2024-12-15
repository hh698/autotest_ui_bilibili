import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from Config.conf import cm

# 配置信息
smtp_server = 'smtp.qq.com'
port = 587
username = '1277490394@qq.com'
password = 'yqboafzrwphugajf'
addressee = '1277490394@qq.com'
report_file = cm.REPORT_FILE

# 创建邮件
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = addressee
msg['Subject'] = '测试报告'

# 读取报告文件
with open(report_file, 'r', encoding='utf-8') as f:
    content_html = f.read()

# 添加 HTML 内容
msg.attach(MIMEText(content_html, 'html', 'utf-8'))

# 添加附件
with open(report_file, 'rb') as f:
    part = MIMEApplication(f.read(), Name=os.path.basename(report_file))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(report_file))
    msg.attach(part)

# 发送邮件
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, addressee, msg.as_string())
    server.quit()
    print("测试邮件发送成功！")
except Exception as e:
    print("Error: 无法发送邮件，{}！".format(e))
    import traceback

    traceback.print_exc()

#  可能是zmail库版本或者不兼容的问题
