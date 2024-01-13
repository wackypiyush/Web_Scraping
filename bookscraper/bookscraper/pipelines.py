# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter=ItemAdapter(item)
        
        # Strip all whitespaces from strings
        field_names=adapter.field_names()
        for field_name in field_names:
            if field_name!='description':
                value=adapter.get(field_name)
                adapter[field_name]=value[0].strip()
                
        # Making some fields value lowercase
        # lowercase_fields=['category']
        # for lowercase_field in lowercase_fields:
        #     value=adapter.get(lowercase_field)
        #     adapter[lowercase_field]=value.lower()
            
        # Converting num_reviews str to int
        num_reviews_string=adapter.get('num_reviews')
        adapter['num_reviews']=int(num_reviews_string)
        return item
