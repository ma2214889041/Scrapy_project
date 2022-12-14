# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl

class DoubanPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.activate
        self.ws.titles = 'TopBooks'
        self.ws.append(('title', 'author', 'subject'))

    def close_spider(self, spider):
        self.wb.save('bookinfo.xlsx')

    def process_item(self, item, spider):
        title = item.get('title', '')
        author = item.get('author', '')
        subject = item.get('subject', '')
        self.ws.append(title, author, subject)
        return item

