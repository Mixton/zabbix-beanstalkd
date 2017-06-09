# zabbix-beanstalkd
beanstalkd module for zabbix

- zabbix >= 2.0

This template discovers every beanstalkd's tube on the host and retrieves the stats. It also creates graphs for each tube.

## DEBIAN
On each oio-sds zabbix agent hosts:
```
wget https://raw.githubusercontent.com/Mixton/zabbix-beanstalkd/master/userparameter_beanstalkd.conf -O /etc/zabbix/zabbix_agentd.conf.d/userparameter_beanstalkd.conf   
apt-get install python-netifaces
apt-get install python-beanstalkc
wget https://raw.githubusercontent.com/Mixton/zabbix-beanstalkd/master/zabbix-beanstalkd-discover.py -O /usr/local/bin/zabbix-beanstalkd-discover.py  
chmod +x /usr/local/bin/zabbix-beanstalkd-discover.py 
systemctl restart zabbix-agent.service  
```

import template 'zbx_beanstalkd_template.xml' and add it to your host  

## CENTOS/RedHat
On each oio-sds zabbix agent hosts:
```
wget https://raw.githubusercontent.com/Mixton/zabbix-beanstalkd/master/userparameter_beanstalkd.conf -O /etc/zabbix/zabbix_agentd.conf.d/userparameter_beanstalkd.conf   
yum install -y python-netifaces.x86_64
yum install -y beanstalkc.noarch
wget https://raw.githubusercontent.com/Mixton/zabbix-beanstalkd/master/zabbix-beanstalkd-discover.py -O /usr/local/bin/zabbix-beanstalkd-discover.py  
chmod +x /usr/local/bin/zabbix-beanstalkd-discover.py 
systemctl restart zabbix-agent.service  
```

import template 'zbx_beanstalkd_template.xml' and add it to your host 
