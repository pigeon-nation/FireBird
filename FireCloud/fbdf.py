#!/usr/bin/env python3

import requests
import xmlrpc
import socket

class GitHub():
	def __init__(self, repn, author='pigeon-nation'):
		self.repn = repn
		self.author = author
	
	def fetch(self, path):
		path = path.lstrip('/')
		addr = 'https://raw.githubusercontent.com/' + self.author + '/' + self.repn + '/' + path
		
		req = requests.get(addr)
		return req.content()
	
	def fetch_desc(self):
		'''Please note this only works with FireBird or other compatible repositories which include a fetch.desc file at the root. '''
		return self.fetch('fetch.desc')