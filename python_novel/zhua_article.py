import threading
import requests
from bs4 import BeautifulSoup
from ur import urls
import time
import queue
import re
import time
'''
url_list=[]
for i in range(0,10):
    url_list.append(urls[i])
'''
url_list=urls
print(len(url_list))
class Getarticle(threading.Thread):
    def __init__(self,queue):      #线程间通过队列通信，每个线程需要用同一个队列初始化
        threading.Thread.__init__(self)
        self.queue=queue
        self.start()
    def run(self): #使用队列实现进程间通信
        while(True):
            try:
                patterns="(第[\u4e00-\u9fa5]{1,3}章)"  #中间表达式标识匹配1到3个汉字
                r=re.compile(patterns)            

                url=self.queue.get()
                print(url)
                response=requests.get(url)
                content=response.content
                text=content.decode('utf-8')

                name=r.findall(text)[0] #匹配章节
                name='hanmen\\'+name
                soup=BeautifulSoup(response.text,'html.parser')
            
                tag=soup.find('div',attrs={'id':'content'})
                filename=name+'.txt'
                
                f=open(filename,'w',encoding='utf-8')
                f.write(str(tag))
                f.close()
            except:
                pass
            

            if self.queue.empty():
                break
            self.queue.task_done() 
def zhua(url,num):
    response=requests.get(url)
    content=response.content
    text=content.decode('utf-8')
    soup=BeautifulSoup(response.text,'html.parser')
    tag=soup.find('div',attrs={'id':'content'})

    print(type(tag))
    #print('-------------',tag.string)
    filename=str(num)+'.txt'
    f=open(filename,'w',encoding='utf-8')
    f.write(str(tag))
    f.close()

def zhua_duo():
    queueq=queue.Queue()
    for i in range(len(url_list)):
        #print(url_list[i])
        queueq.put(url_list[i])

    for i in range(10):
        thread=Getarticle(queueq)
        #threads.append(thread)

start=time.time()
zhua_duo()
end=time.time()
print(end-start)

'''
单线程
start=time.time()    
for count,url in enumerate(url_list):
    zhua(url,count)
end=time.time()
print(end-start)
'''
#https://my.oschina.net/yulongjiang/blog/182508   参考url
# \u4e00-\u9fa5  正则匹配汉字  
