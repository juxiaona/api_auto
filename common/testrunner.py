import sys
sys.path.append("../")
import time
from common.HTMLTestRunner import HTMLTestRunner
from common.sendmail import SendMail
import unittest
from config import read_config

class TestRunner():

	def __init__(self,cases,title,description):
		
		self.cases=cases
		self.title=title
		self.description=description



	def run(self):

		#定义discover
		discover=unittest.defaultTestLoader.discover(self.cases,pattern="*.py")
		
		#定义测试报告的文件名
		now=time.strftime('%Y-%m-%d_%H_%M_')
		filename="../report/"+now+"report.html"
		#打开测试报告写文件
		fp=open(filename,"wb")
		#运行并生成测试报告
		runner=HTMLTestRunner(stream=fp,title=self.title,description=self.description)

		runner.run(discover)

		fp.close()
		'''发送邮件'''
		#从配置文件读取邮箱的相关信息
		server=read_config.mail_server
		username=read_config.mail_username
		password=read_config.mail_password
		receiver=read_config.mail_receiver

		#定义一个SendMail对象
		mail=SendMail(server,username,password,receiver)
		#执行发送邮件
		#mail.sendmail(filename)

		

