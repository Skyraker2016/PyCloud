#coding=utf-8
import os
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import json



def getcomment(id):
    url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_"+str(id)+"?csrf_token="
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
    data = {
        "params": "59OD/06HMoReAdkmVazOzgmWTmJiX0OS0AqF6QSfHNjMs9jBb4K0DexRdwm9QNzXmiB+f2ZFItwcNUykB+0HNIg7MeLNcWkzcw/OVe/bLI97IQALGUtBjLlxOutZPtG8We554AiGlIqXWREGKM17BXP3+Vk5+EfOtc3hgdNVFDQZD9R859yhtMiwPg7kILLz",
        "encSecKey": "bb70e3e64115946fae03e3d60d21c16bf39cd54f6e2de3aa815eb956a781ea13a637608538e49bc7856541041daf45474b7e27b30bc30b6f21bbabd339ff2d54cb1ff4587b6309be52acc2ed2ae6a0a6417220b934852fe84db3b9753f3bb458409c2252fa874557ce85d85b2b6d0127aa2a208f899f5891c0d144f2467a1d53"
    }
    postdata = parse.urlencode(data).encode('utf8')
    req = request.Request(url, headers=header, data=postdata)
    rep = request.urlopen(req).read().decode('utf8')
    json_dict=json.loads(rep)   #获取json
    hot_commit=json_dict['hotComments']  #获取json中的热门评论
    res = ""
    for item in hot_commit:
        res += item['content'] + '\n'
    return res



