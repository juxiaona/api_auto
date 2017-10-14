import requests

#重新封装request方法
class Request():

	def __init__(self):

		pass

	def request(self,method,url,param,header={}):

		if method=='post':
			return requests.post(url,data=param,headers=header)

		elif method=='get':
			return requests.get(url,params=param,headers=header)

		elif method=='put':
			return requests.put(url,data=param,headers=header)

		elif method=='delete':
			return requests.delete(url,data=param,headers=header)
