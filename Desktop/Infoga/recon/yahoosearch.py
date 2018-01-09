#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class YahooSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Yahoo'.format(self.target))
		url = "http://search.yahoo.com/search?p=%40{}&b=0&pz=10".format(self.target)
		headers = {
		            'Host' : 'search.yahoo.com'
		            }
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