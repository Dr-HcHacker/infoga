#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from output import *
from urlparse import urlsplit

def check(url):
	if urlsplit(url).scheme in ['http','https'] or urlsplit(url).path.split('.')[0] == 'www':
		exit(warn('Please try without \'http://\',\'https://\',\'wwww.\''))
	return urlsplit(url).path