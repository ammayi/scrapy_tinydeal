# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import html

class TinydealPipeline:
    def process_item(self, item, spider):
        return item
    
class CleanHTMLPipeline:
    def process_item(self, item, spirder):
        if 'text' in item:
            
            item['text'] = html.unescape(item['text'])
        
        return item