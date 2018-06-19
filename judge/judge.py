import requests
import re
#import sys
from requests.adapters import HTTPAdapter
from config import urlconfig


config=urlconfig
#个人门户基类
'''
function:
	
	login

'''
class customException(Exception):
	def __init__(self,info):
		super().__init__()
		self.message=info

	def __str__(self):
		return self.message

class basicPersonal():
	def __init__(self,config):
		
		self.config=config
		self.s=requests.session()
		self.s.mount('http://', HTTPAdapter(max_retries = 3))
		self.s.mount('https://', HTTPAdapter(max_retries = 3))

	#登录
	#正常返回 cookie
	#密码错误返回-1
	def login(self,ids,password):

		url=self.config['loginurl']
		page =self.s.get(url, verify=False, timeout = 3).text

		pat = re.compile(r'name="lt" value="(.*?)"',re.S)
		lt = re.findall(pat, page)[0]
		
		postdict = {
			'useValidateCode':'0',
			'isremenberme':'1',
			'ip':'',
			'username':ids,
			'password':password,
			'losetime':'30',  
			'lt':lt,
			'_eventId':'submit'
        }

		headers = {
    		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
			'Connection':'keep-alive',
			'Content-Type':'application/x-www-form-urlencoded',

		}

		response=self.s.post(url, data = postdict, headers = headers, timeout = 3)
		#print(response.text)
		if response.text.find("用户名或密码错误")!=-1:

			return -1
		#print(requests.utils.dict_from_cookiejar(self.s.cookies))	
		f=open('find.html','w')
		f.write(response.text)
		f.close()
		return requests.utils.dict_from_cookiejar(self.s.cookies)


class judge(basicPersonal):

	def __init__(self,config):
		super(judge,self).__init__(config)
		self.config=config

	def ticket(self):
		postdict = "callCount=1&page=/portal.do?ticket=ST-89755-5kES6oHOXo5cpyeElLUO-zfca&httpSessionId=9C2A1F66724DD28594B55A75C39A8D8E\
&scriptSessionId=3475609DF5CC6ED0E19673ACCA1FA18C9\
&c0-scriptName=dropNumAjax&c0-methodName=urlDropNum&c0-id=0&c0-param0=string:145042052923857768&c0-param1=null:null&batchId=20"
		#print(postdict)
		
		url=self.config['ticket']
		headers={
			"Origin":self.config['origin']

		}
		response=self.s.post(url,data=postdict,headers=headers)
		#print(response.headers)
		#print(response.text)

	#跳转的url
	def geturl(self):
		
		url=self.config['getjumpurl']
		datas="callCount=1&page=/portal.do?ticket=ST-12492-Odf5INKc3ndfzIYNngpM-zfca&httpSessionId=A72C068638046A2EE91A1351899FDFD0&scriptSessionId=025018557254CCD21B694D88799B6A4D508\
&c0-scriptName=portalAjax\
&c0-methodName=getPicUrlList\
&c0-id=0\
&c0-param0=string:129418789342430599_0101\
&c0-param1=string:6\
&batchId=9"
		#print(datas)
		headers={
			'Origin': self.config['origin'],
		}
		response=self.s.post(url,data=datas,headers=headers)
		#print(response.text)
		compiles=re.compile('<li>(.*?)</li>',re.S)
		hrefs=compiles.findall(response.text)
		href=hrefs[len(hrefs)-1]
		result=re.findall('href=\\\\"(.*?)\\\\"',href)[0]
		self.jumpurl=result
		return result

	def loginjudge(self,ticket,username,password):
	
		url=self.config['loginjudge']
		forms={
			"login_id":username,
			"password":password,
			"s_ticket":ticket,
			"null":"student"
		}

		response=self.s.post(url,data=forms)

		#print(response.text)

	#返回ticket
	def getticket(self):

		#print(self.jumpurl)
		response=self.s.post(self.jumpurl)
		#print(response.text)
		result=re.findall('"s_ticket",\'(.*?)\'',response.text)
		#print(result)
		return result

	#登录流程
	def loginprocess(self):

		#获取跳转链接
		self.geturl()

		#获取ticket
		ticket=self.getticket()

		self.loginjudge(ticket,self.config['number'],self.config['password'])
		#成功登录评教
	def getselecturl(self):

		response=self.s.get(self.config['jieduanpingjia'])
		#print(response.text)

		jumpurl=re.findall('<a href="(.*?)" title="点击进入评价">进入评价</a>',response.text)

		if(len(jumpurl)==0):
			raise customException("当前不可阶段评价")

		jumpurl=self.config['prefix']+jumpurl[0]

		response=self.s.get(jumpurl).text
		#print(response)
		pat1='''<a href="javascript:JsOpenWin\('(.*?)',1000,700\)">修改'''
		pat2='''<a href="javascript:JsOpenWin\('(.*?)',1000,700\)">评价'''
		pat='''\[(.*?)\]'''

		c=re.compile(pat,re.S)
		results=c.findall(response)
		urlList=[]
		for r in results:
			#if (r.find("修改")!=-1) or ((r.find("评价")!=-1) and r.find("查看评价详细")==-1):
			#urlList.append(re.findall("javascript:JsOpenWin\('(.*?)',1000,700\)",r)[0])
			#print(r)
			'''
			result1=re.findall("pat1",r)
			result2=re.findall("pat2",r)
			print(result1)
			if len(result1)!=0:
				urlList.append(result1[0])
			elif len(result2)!=0:
				urlList.append(result2[0])
			'''
			if r.find("修改")!=-1:
				urlList.append(re.findall("'(.*?)'",r)[0])
			elif r.find("评价")!=-1 and r.find("查看评价明细")==-1:
				urlList.append(re.findall("'(.*?)'",r)[0])

		#print(urlList)
		return urlList
		#print(urlList[0])
		#for u in urlList:
			#print(u)
			#print('-----------------------------------------------')
		#print(urlList)
	#对每一个url 进行评教
	def judgeonurl(self,url):
		

		prefix=self.config['prefix']
		url=prefix+url
		pj06xhlist=[]
		response=self.s.get(url).text

		hiddeninfos=re.findall('<input type="hidden" name="(.*?)" value="(.*?)"',response)
		#print(hiddeninfos)


		#文档是个好东西

		'''
		http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
		You can also pass a list of tuples to the data argument.
		This is particularly useful when the form has multiple elements 
		that use the same key:
		>>> payload = (('key1', 'value1'), ('key1', 'value2'))
		>>> r = requests.post('http://httpbin.org/post', data=payload)
		>>> print(r.text)
			{
  				...
 			    "form": {
    				"key1": [
      				"value1",
      				"value2"
    						]
  						},
  				...
			}
		'''
		form=[]
		for info in hiddeninfos:
			
			localdata=(info[0],info[1])
			form.append(localdata)

		#form["issubmit"]=0
		form.append(("issubmit",0))
		#基础表单构造完毕(每次提交都一样的东西)
		#开始选项
		#print(response)

		#这个地方数据一堆\r\t 直接拿前面比较好处理
		c=re.compile('input type="radio" (.*?)>',re.S)
		alloptions=c.findall(response)

		#print(alloptions)
		#这个地方需要考虑一下不是4个选项的时候
		#print(len(alloptions))
		count=int(len(alloptions)/4)  #还没有遇到有 e的选择
		#print(count)

		#构造提交的选项
		xuan=[i*4 for i in range(count)]

		for x in xuan:
			current=alloptions[x]  #选中的选项

			ids=re.findall('name="(.*?)"',current)[0]
			value=re.findall('value="(.*?)"',current)[0]

			form.append((ids,value))

		#print(form)
		#表单构造完毕，开始提交
		url=self.config["submitresult"]
		response=self.s.post(url,data=form)
		print(response.text)
		#print(hiddeninfos)

	#提交评教流程
	def submitprocess(self):
		urls=self.getselecturl()
		for url in urls:
			self.judgeonurl(url)
		



if __name__=='__main__':

	j=judge(config)

	j.login(config['number'],config['password'])

	j.loginprocess()
	
	j.submitprocess()
	