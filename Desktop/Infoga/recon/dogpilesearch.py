#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class DogpileSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in DogPile'.format(self.target))
		url = "http://www.dogpile.com/search/web?qsi=0&q=%40{}".format(self.target)
		headers = {'Host':'www.dogpile.com'}
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