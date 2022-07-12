# ！/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = "A.L.Kun"
__file__ = "getImg.py"
__time__ = "2022/7/12 11:20"
"""获取到每日图片"""

from requests import get
from fake_useragent import UserAgent


def getResp():
    url = "https://cn.bing.com/HPImageArchive.aspx"
    resp = get(url, headers={
        "user-agent": UserAgent().random,
    }, params={
        "format": "js",
        "idx": 1,  # 获取前一天的图片
        "n": 1
    })
    print(resp)
    return resp.json()


def main1():
    src = getResp()
    url_img = "https://www.bing.com" + src["images"][0]["url"]
    title = src["images"][0]["copyright"]
    url_title = src["images"][0]["copyrightlink"]
    return {
        "url_img": url_img,
        "title": title,
        "url_title": url_title
    }


if __name__ == '__main__':
    print(main1())
