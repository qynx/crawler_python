# -*- coding: utf-8 -*-
#encoding: utf-8
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib2

import logging
import os
import re
import time
from urlparse import urlparse
import pdfkit

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


html_template='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</heda>
<body>
{content}
</body>
</html>
'''

start_url='https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000'

domain='{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(start_url))

def get_url_list():   #获取URL列表
    response=urllib2.urlopen('https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000')
    soup=BeautifulSoup(response)
    menu_tag=soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls=[]

    for li in menu_tag.find_all("li"):
        url='http://www.liaoxuefeng.com'+li.a.get("href")
        urls.append(url)
    return urls
'''
def parse_to_html(url):
    response=urllib2.urlopen(url)
    soup=BeautifulSoup(response)
    body=soup.find_all(class_="x-wiki-content x-main-content")[0]
    html=str(body)
    pattern="(<img.*?src=\")(.*?)(\")"

    def func(m):
        if not m.group(2).startswith("http"):
            rtn=''.join([m.group(1),domain,m.group(2),m.group(3)])
            return rtn
        else:
            return ''.join([m.group(1),m.group(2),m.group(3)])
      
    html=re.compile(pattern).sub(func,html)  #compile把方式转换为对象 sub提供替换方法
    #html=html_template.format(content=html)
    
    return html
'''
    
pattern="(<img.*?src=\")(.*?)(\")"
def func(m):
        if not m.group(2).startswith("http"):
            rtn=''.join([m.group(1),'http://www.liaoxuefeng.com/',m.group(2),m.group(3)])
            return rtn
        else:
            return ''.join([m.group(1),m.group(2),m.group(3)])
def run():
    start=time.time()
    #print start
    options={
        'page-size':'Letter',
        'margin-top':'0.75in',
        'margin-right':'0.75in',
        'margin-bottom':'0.75in',
        'margin-left':'0.75in',
        'encoding':'UTF-8',
        'custom-header':[
            ('Accept-Encoding','gzip')
            ],
        'cookie':[
            ('cookie-name1','cookie-value1'),
            ('cookie-name2','cookie-value2'),
            ],
        'outline-depth':10,
        }
    htmls=[]
    for index,url in enumerate(get_url_list()):
        print ('waiting...')
        print (url)
        
        response=urllib2.urlopen(url)
        soup=BeautifulSoup(response,"html5lib")
        body=soup.find_all(class_="x-wiki-content x-main-content")[0]
        f_name='.'.join([str(index),"html"])
        html=str(body)
        #html=html.encode('utf-8')
        html=unicode(html,'utf-8')
        pa=re.compile(pattern)
        html=pa.sub(func,html)
        #html=parse_to_html(url)
        
        with open(f_name,'wb') as f:
            f.write(html)
            
        htmls.append(f_name)
        
    pdfkit.from_file(htmls,"liao.pdf",options=options)
    for html in htmls:
        os.remove(html)
    total_time=time.time()-start
    print (u'总共耗时 :%f 秒" %total_time')

run()       
