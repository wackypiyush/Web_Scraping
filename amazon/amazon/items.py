# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Product_Scrap(scrapy.Item):
    title=scrapy.Field()
    rating=scrapy.Field()
    num_ratings=scrapy.Field()
    discount=scrapy.Field()
    mrp=scrapy.Field()
    sp=scrapy.Field()
    img=scrapy.Field()
    case_diameter=scrapy.Field()
    case_thickness=scrapy.Field()
    case_material=scrapy.Field()
    band_color=scrapy.Field()
    band_material=scrapy.Field()
    warranty=scrapy.Field()
    band_width=scrapy.Field()
    item_weight=scrapy.Field()
    #country_of_Origin=scrapy.Field()
    #about_the_item=scrapy.Field()
    manufacturer=scrapy.Field()
    pay_on_delivery=scrapy.Field()
    returnable=scrapy.Field()
    