# -*- coding:utf-8 -*-

import time

def main():
    print("it's start")
    x1 = 2
    y1 = 4
    lei = zhouchao(x1,y1)
    z1 = lei.zc()
    time.sleep(z1)
    print("run  time is %d"%z1)
    print("it's end")

class zhouchao(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def zc(self):
        z =  self.x * self.y
        return z

if __name__=='__main__':
    main()
