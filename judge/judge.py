import requests
import re
from requests.adapters import HTTPAdapter

urlconfig={
	"loginurl":"https://pt.hnu.edu.cn/zfca/login",
	"jumptojudgeurl":"https://pt.hnu.edu.cn/zfca/login/fakelogin.jsp?ywxtdm=0122579031373493749&yhlx=student&yhm=201508010610&s_ticket=1659"

}
config=urlconfig
#个人门户基类
'''
function:
	
	login

'''
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
		url='http://pt.hnu.edu.cn/dwr/call/plaincall/dropNumAjax.urlDropNum.dwr '
		headers={
			"Origin":"http://pt.hnu.edu.cn"

		}
		response=self.s.post(url,data=postdict,headers=headers)
		#print(response.headers)
		#print(response.text)

	#跳转的url
	def geturl(self):
		url='http://pt.hnu.edu.cn/dwr/call/plaincall/portalAjax.getPicUrlList.dwr'
		
		datas="callCount=1&page=/portal.do?ticket=ST-12492-Odf5INKc3ndfzIYNngpM-zfca&httpSessionId=A72C068638046A2EE91A1351899FDFD0&scriptSessionId=025018557254CCD21B694D88799B6A4D508\
&c0-scriptName=portalAjax\
&c0-methodName=getPicUrlList\
&c0-id=0\
&c0-param0=string:129418789342430599_0101\
&c0-param1=string:6\
&batchId=9"
		#print(datas)
		headers={
			'Origin': 'http://pt.hnu.edu.cn',
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
		url='http://pgfz.hnu.edu.cn/Logon.do?method=logondd'
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

		self.loginjudge(ticket,"201508010610",'287830')
		#成功登录评教

	#对每一个url 进行评教
	def judgeonurl(self):
		url='/hndx_jsxsd/xspj/xspj_edit.do?xnxq01id=2017-2018-2&pj01id=F01B4426639E4CD8A44C18B8F88A8F27&pj0502id=5B281B68272470ACE0530100007F4516&jx02id=083670&jx0404id=20172083670003&xsflid=&zpf=0&jg0101id=2005230&jx02id=083670'
		prefix='http://pgfz.hnu.edu.cn'


		url=prefix+url
		pj06xhlist=[]
		response=self.s.get(url).text

		hiddeninfos=re.findall('<input type="hidden" name="(.*?)" value="(.*?)"',response)
		print(hiddeninfos)
		form=[]
		for info in hiddeninfos:
			
			localdata=(info[0],info[1])
			form.append(localdata)

		#form["issubmit"]=0
		form.append(("issubmit",0))
		#基础表单构造完毕
		#开始选项
		#print(response)

		#这个地方数据一堆\r\t 直接拿前面比较好处理
		c=re.compile('input type="radio" (.*?)>',re.S)
		alloptions=c.findall(response)

		#print(alloptions)
		#这个地方需要考虑一下不是4个选项的时候
		print(len(alloptions))
		count=int(len(alloptions)/4)
		print(count)

		xuan=[i*4 for i in range(count)]

		for x in xuan:
			current=alloptions[x]  #选中的选项

			ids=re.findall('name="(.*?)"',current)[0]
			value=re.findall('value="(.*?)"',current)[0]

			form.append((ids,value))

		print(form)
		#表单构造完毕，开始提交
		url='http://pgfz.hnu.edu.cn/hndx_jsxsd/xspj/xspj_save.do'
		response=self.s.post(url,data=form)
		#print(response.text)
		#print(hiddeninfos)

	#提交评教流程
	def submitprocess(self):
		pass

	def unknows(self):
		url='https://pt.hnu.edu.cn/zfca?yhlx=student&login=0122579031373493749&url=%23'
		response=self.s.get(url)
		#print(response.text)

if __name__=='__main__':

	#basic=basicPersonal(config)

	#basic.login('201508010610','287830')
	j=judge(config)

	print(j.login('201508010610','287830'))
	j.loginprocess()
	j.judgeonurl()
	#j.geturl()
	#j.ticket()
	#j.jumptojudge('287830')
	#j.unknows()