#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from lib import parser 
from lib import request 

from lib.output import *


class JigsawSearch:
	
	req = request.Request()
	
	def __init__(self,target):
		self.target = target

	def search(self):
		test('Searching "{}" in Jigsaw'.format(self.target))
		url = "http://www.jigsaw.com/FreeTextSearch.xhtml?opCode=search&autoSuggested=True&freeText={}".format(self.target)
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