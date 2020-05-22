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
    google_01 = scrapy.Field()
    google_02 = scrapy.Field()
    google_03 = scrapy.Field()
    google_04 = scrapy.Field()
    google_05 = scrapy.Field()
    google_06 = scrapy.Field()
    google_07 = scrapy.Field()
    google_08 = scrapy.Field()
    google_09 = scrapy.Field()
    google_10 = scrapy.Field()

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

    nate_01 = scrapy.Field()
    nate_02 = scrapy.Field()
    nate_03 = scrapy.Field()
    nate_04 = scrapy.Field()
    nate_05 = scrapy.Field()
    nate_06 = scrapy.Field()
    nate_07 = scrapy.Field()
    nate_08 = scrapy.Field()
    nate_09 = scrapy.Field()
    nate_10 = scrapy.Field()

    zum_01 = scrapy.Field()
    zum_02 = scrapy.Field()
    zum_03 = scrapy.Field()
    zum_04 = scrapy.Field()
    zum_05 = scrapy.Field()
    zum_06 = scrapy.Field()
    zum_07 = scrapy.Field()
    zum_08 = scrapy.Field()
    zum_09 = scrapy.Field()
    zum_10 = scrapy.Field()

    # 데이터가 수집된 시간
    google_time = scrapy.Field()
    naver_time = scrapy.Field()
    nate_time = scrapy.Field()
    zum_time = scrapy.Field()

    pass
