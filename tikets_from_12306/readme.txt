注意url请求返回的数据可能不是json格式的，首先确保查询语句（包括格式）的正确，也可以加上headers

stationcode.py

对request返回的对象 用正则语句查询
request.get().content 与 .text的区别
pprint


列表中是 tuple 可用dict方法
列表中是string 用str方法

tickets.py

request中不加 verify=False请求 报错

raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='kyfw.12306.cn', port=443): Max retries exceeded with url: /otn/leftTicket/query?leftTicketDTO.train_date=2017-09-10&leftTicketDTO.from_station=YJT&leftTicketDTO.to_station=ODP&purpose_codes=ADULT (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)'),))


查询语句 request:
日期： 2017-01-09 标准格式
加上headers 要求返会json格式 否则是text/html 
headers={'Accept':'application/json','Cache-Control':'no-cache','User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'} （尚存疑问）


预订|49000K11620B|K1159（车次）|YAK|GZQ|XUN（信阳）|CSQ（长沙）|03:31（出发时间）|11:29（达到时间）|07:58（历时）|Y|%2Fn4LfUiFNqFYCNlm3MnqWVSrVfpafWSjmz8BdF56cXoDdzi4Aa30ysEwHos%3D|20170830|3|K1|28|35|0|0||||无|||有||无|18|||||10401030|1413"

预订|490000Z17002|Z167|QDK|GGQ|XUN|CSQ|04:33|10:34|06:01|Y（是否有票）|rE1bHxkxD2uh6ZNxg91YMIMNNaYx9hBduRkjxMCHJtBmVZAv9H6VyEk9Wts%3D|20170830|3|KA|17|21|0|0||||无|||有||2|20|||||10403010|1431

I8rPF0RrwrNqyfFBieMLNFtYTffSl8xgNRzJCd%2BLBthxZj5hRfSsiwWU0wuSYtCfx3el%2Fo1Id5Nd%0AERPqKWQrKq%2F5Upu3tkP%2FLpHv4IzDuDVtz2o6Se8NZ55UkKs6weDSEHyynisppTW7Rx%2B4mcHfjqeh%0A4c8kmWb1mKfXQui8PfkAuy0BV2PxdwGQ9LNVZgolFdtWyKN2vO7vmLM2q1881Y23J%2BwSNaJQU5ed%0AGD3Inmg27RQj34mmaQ%3D%3D|预订|49000K11620B|K1159|YAK|GZQ|XUN|CSQ|03:31|11:29|07:58|Y|QuGBDId5usidmfNad%2B%2BW%2FWV030NyJz9S6XakEZLVZYw0myfmZrcZqiyNJM0%3D|20170830|3|K1|28|35|0|0||||无|||有||无|18|||||10401030|1413

汉字编码 \u4e00-\u9fa5

预订|390000G55109|G551|LBN|IOQ|OYN|CWQ|
08:54|11:27|02:33|Y|yECO%2BO3BD79pN66OndNfx5r2UlqGJT48cIWqkI3hxohPRRw2|20170831|3|N2|04|09|0|0|||||||||||有|有|20||O0M090|OM9

预订|490000Z17002|Z167|QDK|GGQ|XUN|CSQ|04:33|10:34|06:01|Y|pEuSpaTaLfphbrAGvJDEblXuXF9DzsT2N40v

%2BLbZXskDZZCn25giLJywDek%3D|20170830|3|KA|17|21|0|0||||无软卧|||有无座||2硬卧|20 硬座|二等|一等|商务组||10401030|1413

预订|130000T36906|T369|DLT|GZQ|XUN|CSQ|14:38|21:10|06:32|Y|S4PhS0EdYQVe6EBpv2gPlrCw0GDtaQAlBI1PZwYKFH%2F3js%2BgPvyGQIkLBcU%3D|20170830|3|T2|25|33|0|0||||无软卧|||有无座||无硬卧|无硬座|二等|一等|商务||10401030|1413

预订|390000G55109|G551|LBN|IOQ|OYN|CWQ|08:54|11:27|02:33|Y|yECO%2BO3BD79pN66OndNfx5r2UlqGJT48cIWqkI3hxohPRRw2|20170831|3|N2|04|09|0|0|||||||||||有二等座|有一等座|20商务座||O0M090|OM9



在ticket.py中对from docopt import docopt 的引用要放到__doc__的后面 并且__doc__的书写格式有严格的要求，错误一点即会报错  注意-g 后面的汉字与它相聚一个tab usage中声明的格式要与调用时格式一致


list根据value反推key的方法

>>> dicxx = {'a':'001', 'b':'002'}
>>> list(dicxx.keys())[list(dicxx.values()).index("001")]
'a'
>>>

dicxx = {'a':'001', 'b':'002'}
new_dict = {v:k for k,v in dicxx.items()}  # {'001': 'a', '002': 'b'}
new_dict['001']  # 'a'

原文使用yield添加进prettytable 但对yield和class 不是很熟悉 还是分开写成函数 用list添加进 prettytable的对象

@2017/08/23/ 21:53