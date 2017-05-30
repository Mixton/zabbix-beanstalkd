#!/usr/bin/python
import os
import beanstalkc
import netifaces
import argparse
import textwrap
import json

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='zabbix-beanstalkd-discover.py', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
                        TODO
                        '''), epilog="e.g. zabbix-beanstalkd-discover.py -p <beanstralk port> --get <tube> <stat name>")
    parser.add_argument('-p', '--port', help='set beanstalkd port', required=False, default='6014')
    parser.add_argument('--get', nargs = '*', help='get tube stats', required=False)
    parser.add_argument('--discover', help='discover tubes', required=False, action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s v0.1')
    args = parser.parse_args()

    ifaces = netifaces.interfaces()
    ifacesbanned = ('lo', 'dummy')
    ifaces = (iface for iface in ifaces if not any(ifacebanned in iface for ifacebanned in ifacesbanned))
    for iface in ifaces:
        addrs = netifaces.ifaddresses(iface)
        break
    hostname = addrs[netifaces.AF_INET][0]['addr']

    beanstalk = beanstalkc.Connection(host=hostname, port=6014)
    if args.get and len(args.get) == 2:
        tube = args.get[0]
        stat = args.get[1]
#        print tube
#        print stat
        print beanstalk.stats_tube(tube)[stat]
    elif args.discover:
     tubes = beanstalk.tubes()
     data = [{"{#TUBENAME}": tube} for tube in tubes]
     print(json.dumps({"data": data}, indent=4))
#    for tube in tubes:
#        print tube
#        print beanstalk.stats_tube(tube)
#        print "stats:"
#        print  beanstalk.stats()

