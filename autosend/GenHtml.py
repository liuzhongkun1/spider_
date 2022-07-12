# ！/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = "A.L.Kun"
__file__ = "GenHtml.py"
__time__ = "2022/7/12 14:21"
"""
生成HTML页面
"""
from getImg import main1
from getInfo import main2
import datetime
from pyquery import PyQuery


def get_timer():
    week = ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    now = datetime.datetime.now()

    time_ = now.strftime("%Y年%m月%d日")
    week_ = week[int(now.strftime("%w"))]
    return time_, week_

img = main1()
# print(img)
data = main2()
# print(data)
time_, week_ = get_timer()


def main3():
    html = PyQuery(filename="./templates/index.html")
    # 设置时间
    html(".right h1").text(time_)  # 设置当前时间
    html(".right h3").text(week_)  # 设置第几周
    # 设置图片
    html(".img_des").text(img["title"])  # 设置图片的标题
    html(".main a").attr("href", img["url_title"])  # 设置图片链接
    html(".main a img").attr("src", img["url_img"])  # 设置图片
    # 设置新闻显示
    cont = html(".main .content div")
    for index, item in enumerate(data):
        str_ = f"{index + 1}. {item['content']}"
        p = " <p>%s</p>" % str_
        cont.append(p)

    return html.outer_html()



if __name__ == '__main__':
    main3()
