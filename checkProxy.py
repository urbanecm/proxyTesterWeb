#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
import re
import sys

def check_proxy(ip, port):
	try:
		proxy = {'http' : 'http//' + ip + ':' + str(port)}
		proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
		proxy = re.findall(r'"([^"]*)"', proxy)
		if ip in proxy:
			return True
		else:
			return False
	except KeyboardInterrupt:
		print "Ctrl+c was pressed. Exiting!!!"
		sys.exit(0)
	except:
		return "connection lost"
