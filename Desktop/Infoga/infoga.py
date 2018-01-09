#!/usr/bin/python
# -*- coding: utf-8 -*-

import os 
import sys 
import getopt

from recon import *
from lib.output import *
from lib.request import *
from lib.color import *
from lib.urlparser import *

r = red(1)
g = green(1)
y = yellow(0)
b = blue(1)
e = end() 

def banner():
	print r+"          .                                                      ."+e
	print r+r"        .n                   .                 .                  n."+e
	print r+r"  .   .dP                  dP                   9b                 9b.    ."+e
	print r+r" 4    qXb         .       dX                     Xb       .        dXp     t"+e
	print r+r"dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb"+e
	print r+r"9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP"+e
	print r+r" 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP"+e
	print r+r"  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'"+e
	print r+r"    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'"+e
	print r+r"        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~"+e
	print r+r"                        )b.  .dbo.dP'`v'`9b.odb.  .dX("+e
	print r+r"                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb."+e
	print r+r"                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb"+e
	print r+r"                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb"+e
	print r+r"                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP"+e
	print r+r"                     `'      9XXXXXX(   )XXXXXXP      `'"+e
	print r+r"                              XXXX X.`v'.X XXXX"+e
	print r+r"                              XP^X'`b   d'`X^XX"+e
	print r+r"                              X. 9  `   '  P )X"+e
	print r+r"                              `b  `       '  d'"+e
	print "\n|| Infoga - Dr-HcHacker"
	print "||"+y+" http://github.com/Dr-HcHacker\n"+e

def usage(e=False):
	banner()
	print "Usage: %s [options]:\n"%sys.argv[0].split('.')[0]
	print "\t-t --target\tDomain to search"
	print """\t-s --source\tData source (all,ask,baidu,bing,dogpile,\n\t\t\texalead,jigsaw,pgp,yahoo,yandex)"""
	print "\t-i --info\tGet email informations"
	print "\t-v --verbose\tVerbose"
	print "\t-h --help\tShow this help and exit\n"
	print "Example:"
	print "\t%s --target site.com --source all"%sys.argv[0].split('.')[0]
	print "\t%s --target site.com --source google"%sys.argv[0].split('.')[0]
	print "\t%s --info test@site.com -v\n"%sys.argv[0].split('.')[0]
	if e: exit()

def sources(s):
	wh = ['all','ask','baidu','google','bing','dogpile','exalead','jigsaw','pgp','yahoo','yandex']
	if s not in wh:
		exit(warn('Invalid search engine!'))
	return s

def email(e):
	if '@' not in e: 
		exit(warn('Invalid email!'))
	return str(e)

class infoga(object):

	def uIp(self,ip):
		FinalIP = []
		for i in ip:
			if i not in FinalIP: 
				FinalIP.append(ip)
		return FinalIP

	def uEmail(self,email):
		FinalEmails = []
		for e in email:
			if e not in FinalEmails:
				FinalEmails.append(e)
		return FinalEmails
	
	def ask(self,target):
		emails = self.uEmail(asksearch.AskSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def baidu(self,target):
		emails = self.uEmail(baidusearch.BaiduSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def bing(self,target):
		emails = self.uEmail(bingsearch.BingSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def dogpile(self,target):
		emails = self.uEmail(dogpilesearch.DogpileSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def exalead(self,target):
		emails = self.uEmail(exaleadsearch.ExaleadSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def google(self,target):
		emails = self.uEmail(googlesearch.GoogleSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def jigsaw(self,target):
		emails = self.uEmail(jigsawsearch.JigsawSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]               
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def pgp(self,target):
		emails = self.uEmail(pgpsearch.PGPSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def shodan(self,target):
		return shodansearch.ShodanSearch(target).search()
	
	def yahoo(self,target):
		emails = self.uEmail(yahoosearch.YahooSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def yandex(self,target):
		emails = self.uEmail(yandexsearch.YandexSearch(target).search())
		for email in emails:
			ips = self.uIp(self.tester(email))[0]
			for ip in ips:
				info(ip,self.shodan(ip),email)

	def tester(self,email):
		return tester.Tester(email).search()

	def all(self,target):
		self.ask(target)
		self.baidu(target)
		self.bing(target)
		self.dogpile(target)
		self.exalead(target)
		self.google(target)
		self.jigsaw(target)
		self.pgp(target)
		self.yahoo(target)
		self.yandex(target)

	def main(self):
		if len(sys.argv) <= 1:
			usage(True)
		try:
			opts,args = getopt.getopt(sys.argv[1:],'t:s:i:vh:',['target=','source=',
				'info=','verbose','help'])
		except getopt.error,e:
			usage(True)
		banner()
		for opt,arg in opts:
			if opt in ('-t','--target'):
				self.target = check(arg)
			if opt in ('-s','--source'):
				source = sources(arg)
				if source == "ask":
					self.ask(self.target)
				elif source == "baidu":
					self.baidu(self.target)
				elif source == "bing":
					self.bing(self.target)
				elif source == "dogpile":
					self.dogpile(self.target)
				elif source == "exalead":
					self.exalead(self.target)
				elif source == "google":
					self.google(self.target)
				elif source == "jigsaw":
					self.jigsaw(self.target)
				elif source == "pgp":
					self.pgp(self.target)
				elif source == "yahoo":
					self.yahoo(self.target)
				elif source == "yandex":
					self.yandex(self.target)
				elif source == "all":
					self.all(self.target)
				else:
					usage(True)
			if opt in ('-i','--info'):
				test('Checking email info...')
				ips = self.uIp(self.tester(email(arg)))[0]
				for ip in ips:
					info(ip,self.shodan(ip),arg)
			if opt in ('-v','--verbose'):
				self.verbose = True
			if opt in ('-h','--help'):
				usage(True)

if __name__ == "__main__":
	try:
		infoga().main()
	except KeyboardInterrupt,e:
		exit(warn('Interrupt by user, exting...'))
