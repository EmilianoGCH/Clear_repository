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




import scrapy
from guadalajararealstate.items import guadalajararealstate.Item

class ReasState(scrapy, Spider):
    name = 'realstate'

    def start_request(self):
        number_of_pages = 3
        urls = []
        root_url = 'https://link.springer.com/search/page/'
        #"https://link.springer.com/search/page/1?facet-content-type=%22Article%22&query=additive+manufacturing"
        url_sufix = "?facet-content-type=%22Article%22&query=additive+manufacturing"
        for page in range(1,number_of_pages+1):
            urls.append(root_url+str(page)+url_sufix)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.obtain_adresses)

    def obtain_adresses(self,response):
        page_adresses = response.selector.xpath("//*[@id="results-list"]/li[1]/h2/a/@href")
        for page_url in page_adresses:
            yield scrapy.Request(url=""+page_url,callback=self.get_property_information)

    def get_property_information(self, response):
        item['title'] = response.selector.xpath('//*[@id="main-content"]/div/div/article/div/div[1]/div[2]/h1/text()').get()
        yield item
