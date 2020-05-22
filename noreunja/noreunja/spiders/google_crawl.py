# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GoogleCrawlSpider(CrawlSpider):
    name = 'google_crawl'
    allowed_domains = ['trends.google.co.kr']
    start_urls = ['https://trends.google.co.kr/trends/?geo=KR']

    # rules = (
    #     Rule(LinkExtractor(allow=r'.*'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        i = {}

        i['google_01'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[1]/a/div/div[1]/text()'
        ).extract()
        i['google_02'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[2]/a/div/div[1]/text()'
        ).extract()
        i['google_03'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[3]/a/div/div[1]/text()'
        ).extract()
        i['google_04'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[4]/a/div/div[1]/text()'
        ).extract()
        i['google_05'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[5]/a/div/div[1]/text()'
        ).extract()
        i['google_06'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[6]/a/div/div[1]/text()'
        ).extract()
        i['google_07'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[7]/a/div/div[1]/text()'
        ).extract()
        i['google_08'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[8]/a/div/div[1]/text()'
        ).extract()
        i['google_09'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[9]/a/div/div[1]/text()'
        ).extract()
        i['google_10'] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/ng-include/div/recently-trending/div/div[3]/div/recently-trending-list-item[10]/a/div/div[1]/text()'
        ).extract()
        i['google_time'] = datetime.now()

        return i
