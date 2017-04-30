#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib
import re
import sys

def check_proxy(ip, port):
	try:
		proxy = {'http' : 'http://' + ip + ':' + str(port)}
		proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
		proxy = re.findall(r'"([^"]*)"', proxy)
		if ip in proxy[1]:
			return True
		else:
			return False
	except KeyboardInterrupt:
		print("Ctrl+C was pressed. Quitting. ")
		sys.exit(0)
	except:
		return "connection lost"

print(check_proxy("65.94.95.178", 3128))
