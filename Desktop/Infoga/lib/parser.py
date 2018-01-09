#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

import re
import string

class parser:
	
	def __init__(self,content,target):
		self.target = target
		self.content = content

	def email(self):
		pattern = re.compile('[a-zA-Z0-9.\-_+#~!$&\',;=:]+'+'@'+'[a-zA-Z0-9.-]*'+self.target)
		temp = pattern.findall(self.clean())
		email = []
		for x in temp:
			if x not in email:
				email.append(x)
		return email

	def clean(self):
		self.content = re.sub('<em>'    , '', self.content)
		self.content = re.sub('<b>'     , '', self.content)
		self.content = re.sub('</b>'    , '', self.content)
		self.content = re.sub('</em>'   , '', self.content)
		self.content = re.sub('%2f'     , '', self.content)
		self.content = re.sub('%3a'     , '', self.content)
		self.content = re.sub('<strong>', '', self.content)
		self.content = re.sub('</strong>','', self.content)
		self.content = re.sub('<wbr>'   , '', self.content)
		self.content = re.sub('</wbr>'  , '', self.content)

		for x in ('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C'):
			self.content = string.replace(self.content, x, ' ')
		return self.content