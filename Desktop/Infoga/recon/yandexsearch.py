#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class YandexSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Yandex'.format(self.target))
		url = "http://yandex.com/search?text=%40{}&numdoc=50&lr=10".format(self.target)
		headers = {
		            'Host' : 'yandex.com'
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