#coding=utf-8
#!/usr/bin/env python

import json
import sys
import pexpect

lanplus = 'lanplus'
host = '192.168.2.63'
user = 'Administrator'
passwd = 'Admin@9000'
operation = 'sdr'
sdr_promote = 'FAN4 Presence'

with open('ipmitool.log', 'a+') as fout:
    print('ipmitool -I %s -H %s -U %s -P %s %s' % (lanplus, host, user, passwd, operation))
    child = pexpect.spawn('ipmitool -I %s -H %s -U %s -P %s %s' % (lanplus, host, user, passwd, operation))
    child.logfile = fout.buffer
    # 将pexpect的输入输出信息输出到标准输出
    # child.logfile = sys.stdout.buffer
    index = child.expect(['FAN4 Presence'])
    print(child.before.decode())
    print('------------------')
    print(str(child.after))
    print(str(index))
    fout.close()
    
