from huaban_geturl import get_url
from pa_image import get_image

pin_ids=get_url()
for pin_id in pin_ids:
    try:
        url='http://huaban.com/pins/'+str(pin_id)+'/'
        print url
        get_image(url)
    except:
        continue
    
        
