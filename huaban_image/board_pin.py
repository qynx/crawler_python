import urllib2
import json
def board_to_pin(board_id):
    if type(board_id)!='str':
        board_id=str(board_id)
    url='http://huaban.com/boards/'+board_id+'/'
    response=urllib2.urlopen(url)
    data=response.read()
    index=0
    pins_id=[]
    while True:
        indexx=data.find('<a href="/pins/',index)
        if indexx==-1:
            break
        
        index1=indexx+15
        index2=data.find('/',index1)
        pins_id.append(data[index1:index2])
        index=index2
    return pins_id
