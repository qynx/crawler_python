# -*- coding: utf-8 -*-
import json
from pprint import pprint
#from docopt import docopt
import urllib2
print('帮助文档\n\
Usage:\n\
    get [url] <> <> <>\n\
Options:\n\
    -h	    显示帮助文档\n\
Example:\n\
    get [url]\n\
')

def get(url):
    #url='http://www.toutiao.com/search_content/?offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1'
    #url='http://www.toutiao.com/search_content/?offset=0&format=json&keyword=jiepai&autoload=true&count=20&cur_tab=1'
    url='http://www.toutiao.com/search_content/?offset=50&format=json&keyword=jiepai&autoload=true&count=100&cur_tab=1'
    response=urllib2.urlopen(url)
    res=response.read()
    data=json.loads(res)


    d=data.get('data')
    f=open('data1.txt','w')

    f.write(res)
    f.close()
    urls=[article.get('article_url') for article in d if article!=None]
    return urls
