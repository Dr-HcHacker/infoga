#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

def red(n):
	return "\033[%s;31m"%(n)

def green(n):
	return "\033[%s;32m"%(n)

def yellow(n):
	return "\033[%s;33m"%(n)

def blue(n):
	return "\033[%s;34m"%(n)

def end():
	return "\033[0m"