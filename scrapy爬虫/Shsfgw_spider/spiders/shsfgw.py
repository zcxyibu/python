import os
import re
import uuid

import requests
import scrapy

from Shsfgw_spider import settings
from Shsfgw_spider.items import ShsfgwSpiderItem


class ShsfgwSpider(scrapy.Spider):
    name = 'shsfgw'
    # allowed_domains = ['fgw.gov.cn']
    start_urls = ['http://fgw.sh.gov.cn/gqgg/']
    base_url = 'http://fgw.sh.gov.cn/'
    base_path = settings.PROJECT_ROOT + '/{}/'.format(str(uuid.uuid4()))
    print(base_path)

    def start_requests(self):
        urls = self.start_urls[0]
        for i in range(39):
            if i == 0:
                url = urls + 'index.html'
            else:
                url = urls + 'index_{}.html'.format(i + 1)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath("//div[@class='xwzx_list']/ul/li/a/@href").extract()
        for url in urls:
            yield scrapy.Request(url=response.urljoin(url), callback=self.detail_parse)

    def detail_parse(self, response):
        item = ShsfgwSpiderItem()
        item['title'] = response.xpath("//title/text()").extract_first()
        item['content'] = ''.join(response.xpath("//div[@class='xwzx_content']/p//text()").extract())
        item['attachment'] = self.download_attach(response)
        time_text = response.xpath("//table//tr//li[contains(text(),'发布日期')]/text()").extract_first()
        item['time'] = re.findall('(\d+-\d+-\d+)', time_text)[0]
        yield item

    def download_attach(self, response):
        attachment_url_base = response.xpath("//div[@class='xwzx_content']/ul/li/a[@id='attach0']/@href").extract_first()
        if attachment_url_base:
            attachment_url = self.base_url + attachment_url_base
            attachment_name = response.xpath(
                "//div[@class='xwzx_content']/ul/li/a[@id='attach0']/text()").extract_first()

            if not os.path.exists(self.base_path):
                os.makedirs(self.base_path)
            try:
                with open(self.base_path + '/{}'.format(attachment_name), 'wb') as f:
                    f.write(self.get_file(attachment_url).content)
            except Exception as reason:
                print("出错啦！" + str(reason))
            filename = self.base_path + '/{}'.format(attachment_name)
            return filename
        else:
            return ""

    def get_file(self, url, num=0):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        if num > 5:
            return None
        num += 1
        try:
            response = requests.get(url=url, headers=headers, timeout=5)
            return response
        except Exception:
            return self.get_file(url, num)
