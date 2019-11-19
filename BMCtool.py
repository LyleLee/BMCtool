#!/bin/env python

import json
import sys
import pexpect

lanplus = 'lanplus'
host = '192.168.2.63'
user = 'Administrator'
passwd = 'Admin@9000'
operation = 'sdr'
sdr_promote = "FAN4 Presence"

with open('ipmitool.log', 'w') as fout:
    child = pexpect.spawn('ipmitool -I %s -H %s -U %s -P %s %s' % (lanplus, host, user, passwd, operation))
    child.logfile = fout
    # 将pexpect的输入输出信息输出到标准输出
    # child.logfile = sys.stdout
    index = child.expect([sdr_promote, pexpect.EOF, pexpect.TIMEOUT])

    print(index)
