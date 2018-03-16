# -*- coding: utf-8 -*-
import urllib2
import json
import os
from count_dict import count_

        
def spider_image(para_url):
    print 'lining....'
    response=urllib2.urlopen(para_url)
    res=response.read()
    
    index_1=res.find('gallery')
    
    index_2=res.find('gallery',index_1+3)
    
    index_3=res.find('{',index_2)
    data_1=res[index_3:]
   
    index_4=count_(data_1)      #计算字典到哪里终止
    
    data=data_1[0:index_4+1]    #要转化为字典的数据
    
    dict_1=json.loads(data)     #转化为字典的数据
    count=dict_1['count']
    urls=[]                     #存储图片的url
    for dd in dict_1['sub_images']:
        urls.append(dd['url'])
    sizes=0
    for url in urls:
        response_1=urllib2.urlopen(url)
        res_1=response_1.read()
        filename=url.split('/',)[-1]+'.jpg'
        print filename
        path=os.path.join(os.getcwd(),'image/')
        path_1=os.path.join(path,filename)     #用路径相加的方式表示出最后总路径，不然存储格式有问题
        f=open(path_1,'wb')
        print ('writing %s...'%filename)
        f.write(res_1)
        sizes+=os.path.getsize(path_1)/1024
        print ('finish %d %s'%(os.path.getsize(path_1)/1024,'KB'))
        f.close()
    print 'successfully...'
    print 'totally get %d images :%dMB'%(count,round(sizes/1024,2))

        
        
        
    
    
     
    
    
    
