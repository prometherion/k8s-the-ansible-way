#!/usr/bin/python

def ip_extractor(host, visibility):
	custom_addr = host[visibility + '_ip']
	if (custom_addr):
		return custom_addr
	else:
		return host['ansible_default_ipv4']['address']

class FilterModule(object):
	'''
	Extract private or public IPv4 from Ansible host if provided,
	fallback to default IP
	'''

	def filters(self):
		return {
			'ip': ip_extractor
		}


