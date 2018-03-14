# -*- coding: utf-8 -*-
import urllib2
import json
#from bs4 import BeautifulSoup
import os
def get_image(id):
    url='http://huaban.com/pins/'+id+'/'
    response=urllib2.urlopen(url)
    data=response.read()
    #print data[0:10]
    index_1=data.find('<div class="image-holder">')
    #print index_1
    index_2=data.find('src',index_1)
    index_3=index_2+5
    #print index_3
    index_4=data.find('"',index_3)
    #print index_4
    image_urls=data[index_3:index_4]
    image_url='http:'+image_urls
    #print image_url
    
    responses=urllib2.urlopen(image_url)
    image=responses.read()
    path=os.path.join(os.getcwd(),'image/qingxin')
    image_name=image_url.split('-',)[-1]+'.jpg'
    filepath=os.path.join(path,image_name)
    #print filepath
    f=open(filepath,'wb')
    print 'writing...'
    f.write(image)
    size=os.path.getsize(filepath)/1024
    print 'finish %d KB'%size
    f.close()
    return path
    
    
    
    
