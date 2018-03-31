import re
import scrapy
from bs4 import BeautifulSoup
from scrapy import Selector
from scrapy.http import Request
#单独的request模块,跟进url时需要
from movie.items import MovieItem
#定义保存的字段，导入movie项目中的items文件中的MovieItem类

class Myspider(scrapy.Spider):
	name = 'movie'
	allowed_domains = ['x23us.com']
	bash_url = 'http://www.x23us.com/class/'
	bashend = '.html'

	def start_requests(self):
		for i in range(1,11):
			url = self.bash_url + str(i) + '_1' + self.bashend
			yield Request(url,callback =  self.parse)

	#回调函数
	def parse(self,response):
		htmlsel = Selector(response)
		items=[]
        url=htmlsel.xpath('//@href').extract()
        print(urls)

        for url in urls:
            item=MovieItem
            item['name']=url
            items.append(url)
        return items

