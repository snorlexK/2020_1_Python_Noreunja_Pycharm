# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NaverCrawlSpider(CrawlSpider):
    name = 'naver_crawl'
    allowed_domains = ['datalab.naver.com']
    start_urls = ['https://datalab.naver.com/keyword/realtimeList.naver']

    rules = (
        Rule(LinkExtractor(allow=r'\?age=all&entertainment=-2&groupingLevel=0&marketing=-2&news=-2&sports=-2'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['naver_01'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[1]/div/span[2]/span').extract()
        i['naver_02'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[2]/div/span[2]/span').extract()
        i['naver_03'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[3]/div/span[2]/span').extract()
        i['naver_04'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[4]/div/span[2]/span').extract()
        i['naver_05'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[5]/div/span[2]/span').extract()
        i['naver_06'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[6]/div/span[2]/span').extract()
        i['naver_07'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[7]/div/span[2]/span').extract()
        i['naver_08'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[8]/div/span[2]/span').extract()
        i['naver_09'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[9]/div/span[2]/span').extract()
        i['naver_10'] = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div/ul[1]/li[10]/div/span[2]/span').extract()

        return i

