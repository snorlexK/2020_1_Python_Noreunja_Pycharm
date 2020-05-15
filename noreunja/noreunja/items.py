# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoreunjaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 검색어
    keyword = scrapy.Field()

    # 데이터 수집 시의 실시간 순위
    rank = scrapy.Field()

    # 데이터가 수집된 시간
    time = scrapy.Field()
    pass
