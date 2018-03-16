from spider_toutiao import get
from pa_image import spider_image

urls=get(1)
for url in urls:
    try:
        spider_image(url)
    except:
        continue
