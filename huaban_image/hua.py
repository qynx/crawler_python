# -*- coding: utf-8 -*-
from board_pin import board_to_pin
from pa_image import get_image
from datetime import datetime
import os
def diao(boardid):
    pins=board_to_pin(boardid)
    print '预计 %d 张图片'%len(pins)
    for pin in pins:
        try:
            path=get_image(pin)
        except:
            print 'error....'
            continue
    
    s='log.txt'
    filepath=os.path.join(path,s)
    
    f=open(filepath,'w')
    
    f.write(sss)
    now=str(datetime.now())
    s='于'+now+':'
    f.write(now)
    s='      存入 %d张图片' %len(pins)
    f.write(s)
    f.close()
