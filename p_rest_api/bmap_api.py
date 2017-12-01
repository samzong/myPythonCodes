#!/usr/bin/env python3

'''
# getlnglat() 
输入地区名称转换成坐标点
 Input: 上海市长宁区延安西路1146号
 Output: {'status': 0, 'result': {'location': {'lng': 121.43699726448042, 'lat': 31.21635314131498}, 'precise': 1, 'confidence': 80, 'level': '道路'}}
 调用方式： getlnglat('上海市长宁区延安西路1146号')
 模块导入: from bmap_api import getlnglat

 
'''

import json
from urllib.request import urlopen, quote
import requests, csv
import pandas as pd

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '3YY1w6aTFW3k2gDPiQQHxzKkbvdsl2g7'
    add = quote(address)
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    return temp
