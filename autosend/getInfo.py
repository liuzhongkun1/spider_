# ！/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = "A.L.Kun"
__file__ = "getInfo.py"
__time__ = "2022/7/12 10:08"
"""获取到每日新闻"""
from requests import get
from fake_useragent import UserAgent


def get_resp():
    url = "https://news.topurl.cn/api"
    resp = get(url, headers={
        "user-agent": UserAgent().random
    }, params={
        "count": 20,
    })
    resp.encoding = resp.apparent_encoding
    return resp.json()


def main2():
    data_ = get_resp()
    temp = []
    for i in data_["data"]['newsList']:
        temp.append({
            "content": i["title"],
        })
    return temp


if __name__ == '__main__':
    print(main2())
