import requests
import re
from pprint import pprint

url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025'
response=requests.get(url,verify=False)
stations=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text) #用content 报错 不能把一个字符串模版 查询字节型对象

pprint (dict(stations),indent=4)
