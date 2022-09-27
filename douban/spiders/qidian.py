import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from douban.items import DoubanItem


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']

    def start_requests(self):
        for i in range(1):
            yield Request(url=f'https://www.qidian.com/rank/hotsales/page{i}/')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#book-img-text > ul > li')

        for item in list_items:
            bookitem = DoubanItem()
            bookitem['bookname'] = item.css('h2 a::text').extract_first()
            bookitem['author'] = item.css('a.name::text').extract_first()
            bookitem['abstract'] = item.css('p.intro::text').extract_first()
            yield bookitem
