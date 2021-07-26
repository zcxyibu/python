from selenium import webdriver
import requests
import re
import time
from selenium.webdriver.common.keys import Keys


def mian():
    url = input("输入地址：")
    p = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    x = webdriver.Chrome(p)
    x.get(url)
    #x = requests.get(url).text
    #mode = re.compile('')
    x.find_element_by_id("kw").send_keys(u"四大名著")
    time.sleep(3)
    x.find_element_by_id("su").click()
    time.sleep(2)


    js="var q=document.documentElement.scrollTop=100000"
    x.execute_script(js)
    #x.find_element_by_xpath('//*[@id="wrapper"]').send_keys(Keys.DOWN)
    time.sleep(3)
    x.quit()


if __name__ == "__main__":
    mian()
