# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoreunjaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 순위 - 키워드
    naver_01 = scrapy.Field()
    naver_02 = scrapy.Field()
    naver_03 = scrapy.Field()
    naver_04 = scrapy.Field()
    naver_05 = scrapy.Field()
    naver_06 = scrapy.Field()
    naver_07 = scrapy.Field()
    naver_08 = scrapy.Field()
    naver_09 = scrapy.Field()
    naver_10 = scrapy.Field()

    # 데이터가 수집된 시간
    google_time = scrapy.Field()
    naver_time = scrapy.Field()
    nate_time = scrapy.Field()
    zum_time = scrapy.Field()

    pass
