#!/usr/bin/env python

'''
pynet-rtr1 
IP = 50.242.94.227
SNMP Port = 7961

pynet-rtr2
IP = 50.242.94.227
SNMP Port = 8061

SNMP = galileo
'''

import snmp_helper
import paramiko
from snmp_helper import snmp_get_oid,snmp_extract

# Some defaults 
snmp_community = 'galileo'
snmp_default_port = '161'

# Define my routers
# TODO Pull devices from a text file
router_a = {'host_ip': '50.242.94.227', 'snmp_port': '7961'}
router_b = {'host_ip': '50.242.94.227', 'snmp_port': '8061'}

# Format the device string to work with snmp_get_oid
target1 = (router_a.get('host_ip'), snmp_community, router_a.get('snmp_port', snmp_default_port))
target2 = (router_b.get('host_ip'), snmp_community, router_b.get('snmp_port', snmp_default_port))

# Define My OIDs
oid1 = "1.3.6.1.2.1.1.1.0"  # sysDescr
oid2 = "1.3.6.1.2.1.1.5.0"  # sysName

targets = (target1, target2)
oids = (oid1, oid2)

for item in targets:
  for x in oids:
   snmp_data = snmp_get_oid(item, oid=x, display_errors=True)
   output = snmp_extract(snmp_data)
   print output
