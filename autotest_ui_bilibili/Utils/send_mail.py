#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys

import zmail

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from Config.conf import cm


def send_report():
    """发送报告"""
    with open(cm.REPORT_FILE, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': '1277490394@qq.com',
            'subject': '测试报告',
            'content_html': content_html,
            'attachments': [cm.REPORT_FILE, ]
        }
        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESSEE, mail)
        print("测试邮件发送成功！")
    except Exception as e:
        print("Error: 无法发送邮件，{}！".format(e))
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    send_report()
