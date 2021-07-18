cat smsinit.py 
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
import phone
import datetime
class HiveOperation(object):
    @staticmethod
    def databaseconn():
        conn = hive.Connection(host='10.45.150.54',port=10000,username='rhino')
        cursor=conn.cursor()
        return cursor

    @staticmethod
    def excutesql(cursor,sql):
        cursor.execute(sql)

    @staticmethod
    def timechuo():
        t=time.time()
        return str(int(t))
    
    @staticmethod
    def create_phone():
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9), }[second]
        suffix = random.randint(9999999, 100000000)
        return "1{}{}{}".format(second, third, suffix)
    
    @staticmethod
    def create_phone_call():
        suffix = random.randint(9999, 99999)
        return "137391{}".format(suffix)
    
    @staticmethod
    def getduanxin(dxlist):
        num=len(dxlist)-1
        n=random.randint(0,num)
        return dxlist[n]

    @staticmethod
    def clength():
        return str(random.randint(1, 15))
    @staticmethod
    def clength1():
        return str(random.randint(100, 150))

    @staticmethod
    def num12():
        aa=random.randint(0,1)
        if aa==1:
            bb=random.randint(0,2)
            return str(aa)+str(bb)
        else:
            bb=random.randint(1,9)
            return str(aa)+str(bb)
    @staticmethod
    def city(phoneNum):
        inphone=phone.Phone().find(phoneNum)
        aa='南京市'
        if inphone != None:
            aa=inphone['city']+'市'
        return aa
    @staticmethod
    def create_phone_calling():
        suffix = random.randint(9999, 99999)
        return "189245{}".format(suffix)
if __name__=='__main__':
    HO=HiveOperation()
    with open('content.txt','r') as load_f:
        listtext=load_f.read()
        dxlist=listtext.split("\n")
    start = datetime.date(2020,8,21)
    start1 = start
    end = datetime.date(2020,8,21)
    a_day=datetime.timedelta(days=1)
    list1=[]
    while start<=end:
       list1.append(start.strftime("%Y-%m-%d"))
       start+=a_day
    tol=1
    for i in list1:
       a1=(int(i.split('-')[0]),int(i.split('-')[1]),int(i.split('-')[2]),0,0,0,0,0,0)
       a2=(int(i.split('-')[0]),int(i.split('-')[1]),int(i.split('-')[2]),23,59,59,0,0,0)
       starttime=time.mktime(a1)
       endtime=time.mktime(a2)
       f1=open('fz_fraud_clue_note_base.txt','w')
       f2=open('fz_fraud_clue_note_hour.txt','w')
       f3=open('fz_fraud_clue_note_day.txt','w')
       f4=open('fz_easily_affect_person.txt','w')
       f5=open('fz_action_sms_receiv.txt','w')
       f6=open('fz_person_data_message_day.txt','w')
       print i
       for j in range(100):
           t=random.randint(starttime,endtime)
           t1=t+3600
           date_touble=time.localtime(t)
           datetemp=time.strftime("%Y-%m-%d %H:%M:%S",date_touble)
           r=str(random.randint(100,500))
           date_touble1=time.localtime(t1)
           datetemp1=time.strftime("%Y-%m-%d %H:%M:%S",date_touble1)
           foundtime=datetemp
           recenttime=datetemp1
           calling=HO.create_phone()
           citylistcalling=["460032000","460032001","460032002","460032003","460032004","460032005","460032006","460032007","460032008","460032009","460032010","460032011","460032012","460032013","460044001","460044002","460044003","460044004","460044005","460044006","460044007","460044008","460044009","460044012","460044013","460044014","460044015","460044016","460044017","460044018","460044019"]
           callingphone=HO.getduanxin(citylistcalling)
           called=HO.create_phone()
           citylistcalled=["460032000","460032001","460032002","460032003","460032004","460032005","460032006","460032007","460032008","460032009","460032010","460032011","460032012","460032013"]
           calledphone=HO.getduanxin(citylistcalled)
           operatetype=HO.getduanxin(["3","1","2"])
           tol=tol+1
           type=[101,102,103,104,105,201,301,302,303,304,305,306]
           ftype=HO.getduanxin(type)
           str1=calling+","+callingphone+","+operatetype+",0086,,,"+foundtime+","+recenttime+","+str(ftype)+",0,0,,,,,,"
           str_hour=calling+","+callingphone+","+str(ftype)+","+foundtime+","+HO.clength()+","+HO.clength()+","+HO.clength()+","+HO.clength()+",,"
           str_day=calling+","+callingphone+","+str(ftype)+","+str(start1)+","+HO.clength()+","+HO.clength()+","+HO.clength()+","+HO.clength()+",,"
           str_p=calledphone+","+HO.getduanxin(["1","2"])+","+called+","+str(ftype)+","+HO.getduanxin(["1","2","3"])+","+str(start1)
           #str_p=calledphone+","+HO.getduanxin(["1","2"])+","+called+","+str(ftype)+","+HO.getduanxin(["1","2","3"])+","+foundtime
           str_r=calling+"|"+called+"|"+HO.getduanxin(dxlist)+"|"+str(t)+"||||"+callingphone+"|0086|0086|"+HO.getduanxin(["1","2","3"])+"|||||"+HO.getduanxin(["1","2","3","4"])+"|||"+foundtime+"|"+str(ftype)
           str_m=recenttime+","+HO.clength()+","+HO.clength()+","+called
           f1.write(str1+'\n')
           f2.write(str_hour+'\n')
           f3.write(str_day+'\n')
           f4.write(str_p+'\n')
           f5.write(str_r+'\n')
           f6.write(str_m+'\n')
       f1.close()
       f2.close()
       f3.close()
       f4.close()
       f5.close()
       f6.close()
       time.sleep(1)
       commands.getoutput('echo "copy oceanautifraud.fz_fraud_clue_note_base from \'/home/daedb/note_base.txt\' with delimiter \',\' null \'\'" | psql -d zach_database)
       commands.getoutput('echo "copy oceanautifraud.fz_fraud_clue_note_hour from \'/home/daedb/note_hour.txt\' with delimiter \',\' null \'\'" | psql -d zach_database)
