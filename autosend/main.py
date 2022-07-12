# ！/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = "A.L.Kun"
__file__ = "main.py"
__time__ = "2022/7/12 15:12"

import sys
from GenHtml import time_, week_, main3
from smtplib import SMTP
from email.mime.text import MIMEText  # 发送文本信息使用的库
from email.header import Header  # 设置请求的头部信息
from email.utils import formataddr  # 格式化
from functools import wraps
import json

f = open("settings.json", "r", encoding="utf-8")
info = json.load(f)
if info["status"] != 200:
    print("JSON数据读取错误！")
    sys.exit(1)
subject = f'{time_}新闻（建议使用电脑查看）'  # 设置邮件的标题
html = main3()


def decorate(fun_):
    username = 'liu.zhong.kun@foxmail.com'  # 发送邮件的qq号
    password_pass = 'asdsdf'  # 授权密码，有的邮箱是使用登录密码
    smtp = SMTP('smtp.qq.com', 587)  # 创建一个SMTP服务器，这里使用qq邮箱
    smtp.starttls()  # 开启tls
    smtp.login(username, password_pass)  # 登录

    @wraps(fun_)
    def func_mail(*args, **kwargs):
        fun_(smtp, username, *args, **kwargs)  # 调用发邮件的函数
        smtp.quit()  # 关闭服务器
        smtp.close()

    return func_mail


@decorate
def mail(smtp, username):
    for receiver_ in info["data"]:
        msgRoot = MIMEText(html, "html", "utf-8")
        msgRoot["Subject"] = Header(subject, "utf-8")  # 设置文本标题
        msgRoot['From'] = formataddr(("A.L.Kun", username))  # 设置发件人信息
        msgRoot['To'] = formataddr((receiver_["name"], receiver_["email"]))  # 设置收件人信息
        smtp.sendmail(username, receiver_["email"], msgRoot.as_string())  # 发送邮件
        print(receiver_["email"], ':发送完成')


if __name__ == '__main__':
    mail()
