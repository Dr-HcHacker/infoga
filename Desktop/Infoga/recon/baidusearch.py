#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class BaiduSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Baidu'.format(self.target))
		url = "http://www.baidu.com/s?wd=%40{}&pn=0".format(self.target)
		headers = {'Host':'www.baidu.com'}
		try:
			resp = self.req.send(
				method = "GET",
				url = url,
				headers = headers
				)
			return self.getmail(resp.content,self.target)
		except Exception,e:
			raise

	def getmail(self,content,target):
		return parser.parser(content,target).email()