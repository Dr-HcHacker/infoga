#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

import urllib3
import requests 

class Request:
	
	agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
	
	def send(self,method,url,params=None,data=None,cookie=None,headers=None):
		if headers is None: 
			headers = {}
			headers['User-agent'] = Request.agent # or self.agent
		if cookie is None:  
			cookie = {}
		else:
			cookie = { cookie : '' }
		# init req
		try:
			request = requests.Session()
			# disable requests warnings
			req = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
			req = request.request(
				method = method,
				url = url,
				params = params,
				data = data,
				cookies = cookie,
				verify = False
				)
			# return all req.__attrs__/req.attrs
			return req
		except Exception,e:
			# print raise
			raise