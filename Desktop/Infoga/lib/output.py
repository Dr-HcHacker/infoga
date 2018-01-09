#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from color import *

def plus(string):
	print "%s|+|%s %s"%(green(1),end(),string)

def less(string):
	print "%s|-|%s %s"%(red(1),end(),string)

def warn(string):
	print "%s|!|%s %s"%(red(1),end(),string)

def test(string):
	print "%s|*|%s %s"%(blue(1),end(),string)

def more(string,red=False):
	if red:
		print " %s|%s  %s"%(red(1),end(),string)
	else:
		print " %s|%s  %s"%(green(1),end(),string)

def info(ip,data,email):
	print ""
	plus('Email: {} ({})'.format(str(email),str(ip)))
	try:
		if data['hostnames']:more('Hostnames: {}'.format(data['hostnames'][0]))
		if data['country_code'] and data["country_name"]:more('Country: {} ({})'.format(str(data['country_code']),str(data["country_name"])))
		if data['city'] and data['region_code']:more('City: {} ({})'.format(str(data['city']),str(data['region_code'])))
		if data['asn']:more('ASN: {}'.format(str(data['asn'])))
		if data['isp']:more('ISP: {}'.format(str(data['isp'])))
		if data['latitude'] and data['longitude']:more('Maps: {}'.format('https://www.google.com/maps/@{},{},10z'.format(data['latitude'],data['longitude'])))
		if data['org']:more('Organization: {}'.format(str(data['org'])))
		if data['ports']:more('Ports: {}'.format(str(data['ports'])))
		if data['vulns']:more('Vulns: {}'.format(str(data['vulns'][0])))
	except Exception,e:
		pass