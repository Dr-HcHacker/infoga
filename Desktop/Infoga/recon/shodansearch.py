#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

import json 
import shodan

from lib.output import *


class ShodanSearch:
	def __init__(self,ip):
		self.ip = ip 
		self.key = "UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy"
		self.api = shodan.Shodan(self.key)

	def search(self):
		if self.key is "":
			exit(warn('Shodan API key not found!'))
		try:
			host = self.api.host(self.ip)
			return host
		except Exception,e:
			raise
			
