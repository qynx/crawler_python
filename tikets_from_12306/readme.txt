ע��url���󷵻ص����ݿ��ܲ���json��ʽ�ģ�����ȷ����ѯ��䣨������ʽ������ȷ��Ҳ���Լ���headers

stationcode.py

��request���صĶ��� ����������ѯ
request.get().content �� .text������
pprint


�б����� tuple ����dict����
�б�����string ��str����

tickets.py

request�в��� verify=False���� ����

raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='kyfw.12306.cn', port=443): Max retries exceeded with url: /otn/leftTicket/query?leftTicketDTO.train_date=2017-09-10&leftTicketDTO.from_station=YJT&leftTicketDTO.to_station=ODP&purpose_codes=ADULT (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)'),))


��ѯ��� request:
���ڣ� 2017-01-09 ��׼��ʽ
����headers Ҫ�󷵻�json��ʽ ������text/html 
headers={'Accept':'application/json','Cache-Control':'no-cache','User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'} ���д����ʣ�


Ԥ��|49000K11620B|K1159�����Σ�|YAK|GZQ|XUN��������|CSQ����ɳ��|03:31������ʱ�䣩|11:29���ﵽʱ�䣩|07:58����ʱ��|Y|%2Fn4LfUiFNqFYCNlm3MnqWVSrVfpafWSjmz8BdF56cXoDdzi4Aa30ysEwHos%3D|20170830|3|K1|28|35|0|0||||��|||��||��|18|||||10401030|1413"

Ԥ��|490000Z17002|Z167|QDK|GGQ|XUN|CSQ|04:33|10:34|06:01|Y���Ƿ���Ʊ��|rE1bHxkxD2uh6ZNxg91YMIMNNaYx9hBduRkjxMCHJtBmVZAv9H6VyEk9Wts%3D|20170830|3|KA|17|21|0|0||||��|||��||2|20|||||10403010|1431

I8rPF0RrwrNqyfFBieMLNFtYTffSl8xgNRzJCd%2BLBthxZj5hRfSsiwWU0wuSYtCfx3el%2Fo1Id5Nd%0AERPqKWQrKq%2F5Upu3tkP%2FLpHv4IzDuDVtz2o6Se8NZ55UkKs6weDSEHyynisppTW7Rx%2B4mcHfjqeh%0A4c8kmWb1mKfXQui8PfkAuy0BV2PxdwGQ9LNVZgolFdtWyKN2vO7vmLM2q1881Y23J%2BwSNaJQU5ed%0AGD3Inmg27RQj34mmaQ%3D%3D|Ԥ��|49000K11620B|K1159|YAK|GZQ|XUN|CSQ|03:31|11:29|07:58|Y|QuGBDId5usidmfNad%2B%2BW%2FWV030NyJz9S6XakEZLVZYw0myfmZrcZqiyNJM0%3D|20170830|3|K1|28|35|0|0||||��|||��||��|18|||||10401030|1413

���ֱ��� \u4e00-\u9fa5

Ԥ��|390000G55109|G551|LBN|IOQ|OYN|CWQ|
08:54|11:27|02:33|Y|yECO%2BO3BD79pN66OndNfx5r2UlqGJT48cIWqkI3hxohPRRw2|20170831|3|N2|04|09|0|0|||||||||||��|��|20||O0M090|OM9

Ԥ��|490000Z17002|Z167|QDK|GGQ|XUN|CSQ|04:33|10:34|06:01|Y|pEuSpaTaLfphbrAGvJDEblXuXF9DzsT2N40v

%2BLbZXskDZZCn25giLJywDek%3D|20170830|3|KA|17|21|0|0||||������|||������||2Ӳ��|20 Ӳ��|����|һ��|������||10401030|1413

Ԥ��|130000T36906|T369|DLT|GZQ|XUN|CSQ|14:38|21:10|06:32|Y|S4PhS0EdYQVe6EBpv2gPlrCw0GDtaQAlBI1PZwYKFH%2F3js%2BgPvyGQIkLBcU%3D|20170830|3|T2|25|33|0|0||||������|||������||��Ӳ��|��Ӳ��|����|һ��|����||10401030|1413

Ԥ��|390000G55109|G551|LBN|IOQ|OYN|CWQ|08:54|11:27|02:33|Y|yECO%2BO3BD79pN66OndNfx5r2UlqGJT48cIWqkI3hxohPRRw2|20170831|3|N2|04|09|0|0|||||||||||�ж�����|��һ����|20������||O0M090|OM9



��ticket.py�ж�from docopt import docopt ������Ҫ�ŵ�__doc__�ĺ��� ����__doc__����д��ʽ���ϸ��Ҫ�󣬴���һ�㼴�ᱨ��  ע��-g ����ĺ����������һ��tab usage�������ĸ�ʽҪ�����ʱ��ʽһ��


list����value����key�ķ���

>>> dicxx = {'a':'001', 'b':'002'}
>>> list(dicxx.keys())[list(dicxx.values()).index("001")]
'a'
>>>

dicxx = {'a':'001', 'b':'002'}
new_dict = {v:k for k,v in dicxx.items()}  # {'001': 'a', '002': 'b'}
new_dict['001']  # 'a'

ԭ��ʹ��yield��ӽ�prettytable ����yield��class ���Ǻ���Ϥ ���Ƿֿ�д�ɺ��� ��list��ӽ� prettytable�Ķ���

@2017/08/23/ 21:53