import scrapy
from additivereview.items import additivereview.Item

class additive_review(scrapy.Spider):
    name = "additivem"

    def start_requests(self):
        number_of_pages = 2220
        urls = []
        root_url_start = 'https://link.springer.com/search/page/'
        root_url_finish = '?facet-content-type="Article"&query=additive+manufacturing'

        for page in range(1,number_of_pages):
            urls.append(root_url+str(page))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.obtain_title)

    def obtain_title(self,response):
        page_addresses = response.selector.xpath('//*[@id="results-list"]')
        for page_url in page_addresses:
            yield scrapy.Request(url=''+page_url,callback=self.get_property_information)

    def get_property_information(self,response):
        item = guadalajararealstateItem()
        item["price"] = response.selector.xpath('').getall()
        yield Item

