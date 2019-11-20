#!/bin/env python

import json
import sys
from datetime import datetime

import pexpect
import logging

lanplus = 'lanplus'
host = '192.168.2.63'
user = 'Administrator'
passwd = 'Admin@9000'
operation = 'sdr'
sdr_promote = 'FAN4 Presence"
logfile1 = 'ipmitool.log'
logfile2 = 'logging.log'

with open(logfile1, 'w') as log1:
    child = pexpect.spawn('ipmitool -I %s -H %s -U %s -P %s %s' % (lanplus, host, user, passwd, operation))
    child.logfile = log1.buffer
    logging.basicConfig(filename=logfile2, level=logging.DEBUG)
    # 将pexpect的输入输出信息输出到标准输出
    # child.logfile = sys.stdout
    index = child.expect([sdr_promote, pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f') + f'{operation} run success')
        child.expect(pexpect.EOF)
        print('finish %s' % operation)
    elif index == 1:
        print('meet end')
    elif index == 2:
        logging.warning('fail')
        print('fail')
    print(index)
