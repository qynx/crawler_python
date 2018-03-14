# coding: utf-8

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt
from stations import stations
import requests
from duiying import duiying
from prettytable import PrettyTable
from colorama import init,Fore

class trainscollection:
    def __init__(self,available_trains,options):
        self.available_trains=available_trains
        self.options=options
    def _get_duration(self,raw_train):
        duration=raw_train.get('lishi').replace(':','小时')+'分' #历时
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    @property
    def trains(self):
        for raw_train in self.available_trains:
            train_no=raw_train['station_train_code']
            initial=train_no[0].lower()

def chu(lis,options):#处理json数据的result对应的列表
    trains=[]
    for l in lis: #列表的每一项为字符串
        ll=l.split('|') #得到新的列表 每一项的对应关系在duiying.py中注明
        train_no=ll[3]  

        train_type=train_no[0].lower() #获取火车 k t
        from_station=ll[6]
        to_station=ll[7]
        
        #获取的json格式的数据中，所有出发站与到达站都是编码格式的，不是直接的中文，需要在stations反
        #查找出对应的城市名
        from_name=list(stations.keys())[list(stations.values()).index(from_station)]
        to_name=list(stations.keys())[list(stations.values()).index(to_station)]

        
        start_time=ll[8]
        end_time=ll[9]
        lishi=ll[10]
        
        for x in range(23,33):
            if ll[x]==None:
                ll[x]='--'
        if not options or train_type in options:
            train=[
                train_no,
                '\n'.join([Fore.GREEN+from_name+Fore.RESET,Fore.RED+to_name+Fore.RESET]),
                '\n'.join([Fore.GREEN+start_time+Fore.RESET,Fore.RED+end_time+Fore.RESET]),
                lishi,
                ll[32],
                ll[31],
                ll[30],
                ll[23],
                ll[28],
                ll[29],
                ll[26],
                ]
            trains.append(train)
    return trains
header='车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 硬座 无座'.split()
def pretty_print(trains):
    pt=PrettyTable()
    pt._set_field_names(header)
    for train in trains:
        pt.add_row(train)
    print (pt)

                
        
        
        
if __name__=='__main__':
    '''command-line interface'''
    init()
    arguments=docopt(__doc__)
    from_station=stations.get(arguments['<from>'])
    to_station=stations.get(arguments['<to>'])
    date=arguments['<date>']
    url='https://kyfw.12306.cn/otn/leftTicket/query?\
leftTicketDTO.train_date={}&\
leftTicketDTO.from_station={}&\
leftTicketDTO.to_station={}&\
purpose_codes=ADULT'.format(date,from_station,to_station)
    headers={'Accept':'application/json','Cache-Control':'no-cache','User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
    print (url)
    r=requests.get(url,headers=headers,verify=False)
    #print (r.json())

    #提取返回json数据中的信息
    available_trains=r.json()['data']['result'] #列表 每一项记录一个车次信息
    
    options=''.join([key for key,value in arguments.items() if value is True])
    trains=[]
    trains=chu(available_trains,options)
    pretty_print(trains)

    

    
