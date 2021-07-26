# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import requests
import re
import webbrowser

n = 3

def main():
    global url
    url = input("请输入视频网址：")
    print(url)
    p = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(p)#启动chrome浏览器
    driver.get(url)#打开网址

    print('please wait %ds...'%n)
    time.sleep(n)

    sub_url_list = get_list(url)
    sub_url = select_sub_url(sub_url_list,url)
    driver.get(sub_url)
    #webbrowser.open(sub_url)

    video_url = get_video_list(sub_url)
    driver.get(video_url)
    f = open('F:\\python\\zc_0604.txt','wb')
    f.write(video_url.content)
    f.close()

    #d_video(video_url)

    print('please wait %ds...'%n)
    time.sleep(n)
    driver.quit()#关闭

def get_list(url):
    text = requests.get(url)
    text.encoding='utf-8'
    #content = requests.get(url).content#bak
    mode = re.compile('<a href=(.+?)/a>')
    sub_url_list =  mode.findall(text.text)
    if sub_url_list == []:
        print('no sub_url')
        exit()
    else:
        '''
        f = open('F:\\python\\url.txt','wb')
        f.write(content)
        f.close()
        '''
        return sub_url_list

def select_sub_url(sub_url_list,url):
    for x in sub_url_list:
        sub_mode = re.compile('"(.+?).html">(.+?)<')
        sub_url =  sub_mode.findall(x)
        if sub_url == []:
            pass
        else:
            print(sub_url)
    while True:
        y = input("请输入要进入频道的关键字：")
        for x in sub_url_list:
            if y in x:
                sub_mode = re.compile('\"(.+?)\"')
                sub_url =  sub_mode.findall(x)
                print('%s 的 URL 是：%s' %(y,url+str(sub_url[0])))
                return url+str(sub_url[0])
            else:
                continue
        if sub_url == '' or len(sub_url) == 0:
            z = input("没有这个频道!\n1：退出\n2: 重输\n")
            if z == '1':
                exit()
            else:
                pass

def  get_video_list(sub_url):
    text = requests.get(sub_url)
    text.encoding='utf-8'
    video_mode = re.compile('<a href="(.+?)" target')
    video = video_mode.findall(text.text)
    for v in video:
        if v == []:
            pass
        else:
            print(v)
    while True:
        y = input("请输入视频的关键字：")
        for x in video:
            if y in x:
                global url
                print('%s 的 URL 是：%s' %(y,(url+x)))
                return (url+x)
            else:
                continue
        if x == '' or len(y) == 0:
            z = input("没有这个频道!\n1：退出\n2:重输")
            if z == 1:
                exit()
            else:
                pass

#def d_video(url):




if __name__=='__main__':
    main()
