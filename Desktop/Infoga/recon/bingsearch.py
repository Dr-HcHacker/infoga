#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class BingSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Bing'.format(self.target))
		url = "http://bing.com/search?q=%40{}".format(self.target)
		try:
			resp = self.req.send(
				method = "GET",
				url = url,
				cookie = "SRCHHPGUSR=ADLT=DEMOTE&NRSLT=100"
				)
			return self.getmail(resp.content,self.target)
		except Exception,e:
			raise

	def getmail(self,content,target):
		return parser.parser(content,target).email()