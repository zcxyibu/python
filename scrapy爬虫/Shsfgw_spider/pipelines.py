
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import pymysql
from itemadapter import ItemAdapter

class ShsfgwSpiderPipeline:
    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open("0000620_01.txt", "wb")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write((item['title']+'|').encode("utf-8"))
        self.file.write((item['content'] + '|').encode("utf-8"))
        self.file.write((item['attachment'] + '|').encode("utf-8"))
        self.file.write((item['time'] + '|').encode("utf-8"))
        self.file.write(b"\n")
        return item
