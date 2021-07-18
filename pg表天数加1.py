#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
@author: zach
'''

import random
import time
import math
import commands
import time
#import phone
import datetime

#设置增加天数
num="1"
with open('/home/daedb/cctest/timeset/table_day.txt','r') as load_f:
   listtext=load_f.read()
   listtext=listtext.split("\n")
list2=[]
for i in listtext:
   list2.append(i.split(','))
print list2
if list2[-1]==['']:
   list2.remove(list2[-1])
print list2
for j in list2:
    #print 'echo "update oceanautifraud.%s set %s = (%s + interval \'%s D\') where 1=1" | psql -d fz_demo'%(j[0],j[1],j[1],num)
    commands.getoutput('echo "update oceanautifraud.%s set %s = (%s + interval \'%s D\') where 1=1" | psql -d fz_demo'%(j[0],j[1],j[1],num))
    
######
#cat /home/daedb/cctest/timeset/table_day.txt（需要执行的表和列）
#note_daybymonth,fraud_date
#cdr_daybymonth,fraud_date
