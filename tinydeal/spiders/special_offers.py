import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = "special_offers"
    allowed_domains = ["web.archive.org"]
    start_urls = ["https://web.archive.org/web/20110207093218/http://www.tinydeal.com/specials.html"]

    def parse(self, response):
        products = response.xpath("//ul[@class= 'productlisting-ul']/li/div/div[@class= 'ProductDetails']")
        for product in products:
            title = product.xpath('.//div/div/span/a/text()').get()
            url = product.xpath('.//div/div/span/a/@href').get()
            special_price = product.xpath(".//div/div/div[@class= 'originalprice']/span[1]/text()").get()
            normal_price = product.xpath(".//div/div/div[@class= 'originalprice']/span[1]/text()").get()

            yield{
                'title' : title,
                'url' : url,
                'special_price' : special_price,
                'normal_price' : normal_price
            }

