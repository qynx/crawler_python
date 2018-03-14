import requests,time
from bs4 import BeautifulSoup
from pprint import pprint

'''
要想查看错误原因
则输出
'''
proxies=[{"http": "117.90.0.225:9000"},
         {"http": "186.154.146.26:8080"},
         {"http": "175.155.25.27:808"},
         {"http": "124.88.67.52:843"},
         {"http": "119.5.0.7:808"},]

url='http://zhannei.baidu.com/cse/search?s=920895234054625192&entry=1&q={}'

search=input('Enter the book name you want to search')

url=url.format(search)

print(url)
times=0
while True:
    times+=1
    print("尝试第%s次"%times)
    try:
        if times>5:
            response=requests.get(url,proxies=proxies[times%5])
        else:
            response=requests.get(url)
        break
    except Exception as e:
        #print(e)
        pass
    time.sleep(0.3)
#print("尝试%s次"%time)

content=response.content
text=content.decode('utf-8')
'''
f=open('biquge.html','wb')
f.write(content)
f.close()
#print(response.status_code)
'''
soup=BeautifulSoup(text,'html.parser')
tag=soup.find('a',attrs={'cpos':'title'})
#print(tag)

book_url=tag.get('href')
title=tag.get('title')

#print(book_url,title)

response=requests.get(book_url)
list_html=response.text
soup=BeautifulSoup(list_html,"html.parser")
tag=soup.find('div',attrs={'id':'list'})
#print(tag)
lian=tag.dl
#print(type(lian))
a_urls=lian.find_all('a')
urls=[]
host='http://www.qu.la/'
titles=[]
contents=[]
for a in a_urls:
    urls.append([host+a.get('href'),a.string])
    contents.append(host+a.get('href'))
    
    
f=open('12.txt','w')
f.write(str(urls))
f.close()
#print(urls)
#print(lian)
print('urls=')
pprint(contents)


