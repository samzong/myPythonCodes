#!/usr/bin/env python3

'''
# 导入地理位置信息批量获取坐标点

'''
from bmap_api import getlnglat
import csv

file = open(r'./cityandprice.json', 'w')
with open(r'./cityandprice.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        b = line[0].strip()
        c = line[1].strip()
        lng = getlnglat(b)['result']['location']['lng']
        lat = getlnglat(b)['result']['location']['lat']
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
        # str_temp = '{"lat":' + str(lat) + ',"lng:" + str(lng) + ',"count":' + str(c) +'},'
        file.write(str_temp)

file.close()
