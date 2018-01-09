#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class ExaleadSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Exalead'.format(self.target))
		url = "http://www.exalead.com/search/web/results/?q=%40{}&elements_per_page=50&start_index=0".format(self.target)
		headers = {
		            'Host'    : 'www.exalead.com',
		            'Referer' : 'http://exalead.com/search/web/results/?q=%40{}'.format(self.target)
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