import os
import json
import pymysql
from pykeyboard import *
from time import sleep
import pyperclip
import time
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

def upload(selectfile):
    k = PyKeyboard()
    k.press_key(k.shift_l_key)  #
    k.release_key(k.shift_l_key)  #
    sleep(2)
    k.type_string(selectfile)
    sleep(1)
    k.press_key(k.enter_key)


def clean_json_content(locate):
    k = PyKeyboard()
    k.press_key(k.control_key)
    k.press_key('a')
    k.release_key('a')
    k.release_key(k.control_key)
    k.press_key(k.delete_key)
    k.release_key(k.delete_key)

    # k.redo_key(k.control_key)
    # k.press_key('C')

#删除浏览器进程
def clean():
    cmd='taskkill /IM "chromedriver.exe" /T /F'
    os.system(cmd)

def cleanDB(businness_name,host_ip,port):
    '''
    Desc:每条用例结束后清除数据库表数据
    :param
    :return: NA
    '''
    config = {
        'host': host_ip,
        "port": int(port),
        "user": 'rhino',
        "password": 'rhino',
        "db": "daas",
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,
    }
    conn = pymysql.connect(**config)
    try:
        with  conn.cursor() as cursor:
            sql = "delete from app_page where AppPageName = '%s'" % businness_name
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            conn.commit()
    finally:
        conn.close()


def executeSQL(self, user, sql):
    '''
        执行sql
    '''
    self.connectDB(user)
    self.cursor.execute(sql)
    self.commitDB()
    self.closeDB()


def executeSQLFromFile(self, user, docu):
    self.connectDB(user)
    f = open(docu, 'r')
    sql = f.readlines()
    f.close()
    for i in sql:
        self.cursor.execute(i)
    self.commitDB()
    self.closeDB()


def writeJson(id, path):
    '''
    Desc:根据传入的ID值，替换json文件中的控件ID
    :param
        id:页面拖拽的控件ID
        path: json文件路径
    :return: NA
    '''
    with open(path, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        print(data)
        for properties in data:
            print(data['properties']['id'])
            data['properties']['id'] = id
            after = data
    # 打开文件并覆盖写入修改后内容
    with open(path, 'w+') as f:
        data = json.dump(after, f)


def retContent(path):
    '''
    Desc:读取json文件内容
    :param
    :return: json文件内容
    '''
    with open(path, 'r') as f:
        # 读取整个文件到一个列表
        data_list = f.readlines()
        print(data_list)
        return data_list

def xierujson(json):
    pyperclip.copy(json)
    time.sleep(0.25)
    k = PyKeyboard()
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)

if __name__ == "__main__":
    id_list = [111, 222, 333, 444]
    path1 = 'C:/Python37/oceaneye/test data/json/Picture_Table_Control/shixu_zuobiaozhou_stock/stock.json'
    # multipleCombobox(id_list,path1,path2,path3)
    stock(id_list, path1)
