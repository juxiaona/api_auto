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

		discover=unittest.defaultTestLoader.discover(self.cases,pattern="*.py")
		
		now=time.strftime('%Y-%m-%d_%H_%M_')
		filename="../report/"+now+"report.html"
		fp=open(filename,"wb")
		runner=HTMLTestRunner(stream=fp,title=self.title,description=self.description)

		runner.run(discover)

		fp.close()
		'''发送邮件'''
		server=read_config.mail_server
		username=read_config.mail_username
		password=read_config.mail_password
		receiver=read_config.mail_receiver

		mail=SendMail(server,username,password,receiver)
		mail.sendmail(filename)

		

