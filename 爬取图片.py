# -*- coding:utf-8 -*-
import requests
import webbrowser
import re
#import click

def main():
    url = input("请输入url:")
    #webbrowser.open(url)
    url = requests.get(url)
    '''
    f = open('F:\\python\\zc.txt','wb')
    f.write(url.content)
    f.close()
    '''
    imglist = get_img(url.text)
    d_img(imglist)


def get_img(text):
    #<img src="http://pic.yjmht.com/art/2018-08-30/j1xhdkqsw33.jpg">
    mode = re.compile('<img src="(.+?).jpg">')
    imglist = mode.findall(text)
    if imglist == []:
        print("not picture")
        exit()
    else:
        return imglist


def d_img(imglist):
    image_name = 0
    for img_url in imglist:
        try:
            img_url = img_url+".jpg"
            print(img_url)
            f = open('F:\\python\\zc_' + str(image_name) + ".jpg",'wb')
            img = requests.get(img_url).content
            f.write(img)
            f.close()
        except Exception as e:
            print(str(img)+" error",e)
        image_name += 1
    print("end! num:%d"%image_name)


if __name__=='__main__':
    main()
