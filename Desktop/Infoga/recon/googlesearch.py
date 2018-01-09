#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class GoogleSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Google'.format(self.target))
		url = "https://www.google.it/search?num=1000&hl=en&q=%40{}".format(self.target)
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