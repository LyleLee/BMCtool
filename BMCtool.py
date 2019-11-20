#coding=utf-8
#!/usr/bin/env python

import json
import sys
from datetime import datetime
from time import sleep

import pexpect
import logging

lanplus = 'lanplus'
host 	= '192.168.2.63'
user 	= 'Administrator'
password= 'Admin@9000'
operation	= 'sdr'
sdr_promote	= 'FAN4 Presence'
logfile 	= f'{operation}.log'.encode()
interval	= 30
runtimes 	= 0

with open(logfile, 'w+') as log:
    starttime = datetime.now()
    while (datetime.now()-starttime).seconds < 24*60*60:
        child = pexpect.spawn(f'ipmitool -I {lanplus} -H {host} -U {user} -P {password} {operation}')
        child.logfile = log.buffer
        # 将pexpect的输入输出信息输出到标准输出
        # child.logfile = sys.stdout
        index = child.expect([sdr_promote, pexpect.EOF, pexpect.TIMEOUT])
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
        message_success = f'{nowtime}  {operation} run success \r\n'
        message_failed = f'{nowtime}  {operation} run failed \r\n'
        if index == 0:
            child.logfile.write(message_success.encode())
            child.expect(pexpect.EOF)
            print(message_success)
        elif index == 1:
            child.logfile.write(message_failed.encode())
            print(message_failed)
        elif index == 2:
            child.logfile.write(message_failed.encode())
            print(message_failed)
        sleep
    log.close()	
