#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class AskSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Ask'.format(self.target))
		url = "http://www.ask.com/web?q=%40{}&pu=100&page=0".format(self.target)
		try:
			resp = self.req.send(
				method = "GET",
				url = url
				)
			return self.getmail(resp.content,self.target)
		except Exception,e:
			raise

	def getmail(self,content,target):
		return parser.parser(content,target).email()