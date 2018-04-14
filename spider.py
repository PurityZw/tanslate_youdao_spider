# -*- coding:utf-8 -*-
import urllib
import urllib2
import time
import random
import hashlib  # 用于md5加密
import json
from utlis.utlis import SpiderVarible

ROOT_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


def translate_spider(search_str):
    proxy_addr = SpiderVarible().get_random_proxy_addr()
    user_agent = SpiderVarible().get_random_user_agent()

    # 生成salt
    # salt = "" + ((newDate).getTime() + parseInt(10 * Math.random(), 10))
    salt = str(int(time.time() * 1000) + random.randint(0, 10))
    # print salt

    S = "fanyideskweb"
    n = search_str
    r = salt
    # 该加密内容会不定时修改, 爬取失败时需要重新查找js修改
    D = "ebSeFb%=XZ%T[KZ)c(sy!"
    # 进行MD5加密
    sign = hashlib.md5(S + n + r + D).hexdigest()
    # print sign

    form_data = {
        "i": search_str,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    form_str = urllib.urlencode(form_data)
    # print len(form_str)

    headers = {
        "Content-Length": len(form_str),
        "Cookie": "_ntes_nnid=f77d53cb936304b5333b304b767a4958,1506087321856; OUTFOX_SEARCH_USER_ID_NCOO=971893961.4325761; OUTFOX_SEARCH_USER_ID=-1480774266@10.169.0.83; JSESSIONID=aaaouUJJcJbTucFMz-8kw; ___rl__test__cookies=1523590284588",
        "Referer": "http://fanyi.youdao.com/",
    }

    proxy_handler = urllib2.ProxyHandler({'http': proxy_addr})
    opener = urllib2.build_opener(proxy_handler)
    request = urllib2.Request(ROOT_URL, form_str, headers=headers)
    request.add_header('User-Agent', user_agent)
    response = json.loads(opener.open(request).read())
    result = response['translateResult'][0][0]['tgt']
    print result


if __name__ == '__main__':
    search_str = raw_input('查询内容:')
    translate_spider(search_str)
