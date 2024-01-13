# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_price(value):
    return (f'$ {str(value)}')
class BookItem(scrapy.Item):
    url=scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field(serializer=serialize_price)
    rating=scrapy.Field()
    description=scrapy.Field()
    num_reviews=scrapy.Field()
    category=scrapy.Field()
