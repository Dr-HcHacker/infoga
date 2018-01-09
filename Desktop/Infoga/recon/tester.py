#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

import re 
from lib import parser 
from lib import request 

from lib.output import *


class Tester:
	
	req = request.Request()
	
	def __init__(self,email):
		self.email = email

	def search(self):
		data = { 'lang' : 'en' }
		data['email'] = self.email
		url = "http://mailtester.com/testmail.php"
		try:
			resp = self.req.send(
				method = "POST",
				url = url,
				data = data
				)
			return self.getip(resp._content)
		except Exception,e:
			raise

	def getip(self,content):
		pattern = re.compile(r"[0-9]+(?:\.[0-9]+){3}")
		return pattern.findall(content)