import requests
import urllib2
import json


def get_url(board_id='24431205'):
    pin_ids=[]
    board_ids=[]
    url='http://huaban.com/favorite/beauty/'
    params={'j65xsfdr':'','max':board_id,'limit':'20','wfl':'1',}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Accept':'application/json','X-Request':'JSON','X-Requested-With':'XMLHttpRequest'}

    z1=requests.get(url=url,params=params,headers=headers)
    print z1.status_code

    dic=z1.json()


    js=json.dumps(dic)


    #response=urllib2.urlopen('http://huaban.com/boards/favorite/beauty/?j65sbffd&max=24431205&limit=20&wfl=1')


    #print type(z1)       #response
    #print type(response) #instance
    #data=response.read()
    #js=json.loads(data)
    f=open('huaban.txt','w')
    f.write(json.dumps(dic))
    f.close()
    #print type(dic['pins'])
    #for key in dic['pins']:
       # print key
    #print dic['pins'][0]
    for i in dic['pins']:
        #print i['pin_id']
        pin_ids.append(i['pin_id'])
        
    #print 'ss %s'%pin_ids[(len(pin_ids)-1)]
    #get_url(pin_ids[(len(pin_ids)-1)])
        
    return pin_ids
   


