import scrapy
from amazon.items import Product_Scrap 

class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.in"]
    #start_urls = ["http://amazon.in/"]
    
    def start_requests(self):
        url_='https://www.amazon.in/s?k=analog+watches&crid=12TMAWYQSLLHB&sprefix=%2Caps%2C290&ref=nb_sb_ss_recent_5_0_recent'
        yield scrapy.Request(url=url_, callback=self.parse)
        

    def parse(self, response):
        cards=response.css('div.puis-card-container')
        for card in cards:
            product_url=card.css('a.a-link-normal').attrib['href']
            #print('*********************************************', product_url)
            if product_url is not None:
                yield response.follow(url=product_url, callback=self.product_scrap)
                
        next_page_url=response.xpath('//span[@class="s-pagination-item s-pagination-disabled"]/following-sibling::a').attrib['href']
        if next_page_url is not None:
            next_page='https://www.amazon.in/'+next_page_url
            yield response.follow(url=next_page, callback=self.parse)
        #print('8******************************************', next_page_url)
        
        
    def product_scrap(self, response):
        product_detail=Product_Scrap()
        product_detail['title']=response.css('span#productTitle::text').get().strip(' ')
        product_detail['rating']=response.xpath('//span[contains(@class, "a-size-base") and contains(@class, "a-color-base")]/text()').get()
        product_detail['num_ratings']=response.css('span#acrCustomerReviewText::text').get()
        product_detail['discount']=response.xpath('//span[contains(@class, "a-color-price savingPriceOverride") and contains(@class, "reinventPriceSavingsPercentageMargin savingsPercentage")]/text()').get()
        product_detail['mrp']=response.css('span.a-offscreen::text').get()
        product_detail['sp']=response.css('span.a-price-whole::text').get()
        product_detail['img']=response.css('img#landingImage').attrib['src']
        
        product_detail['pay_on_delivery']=response.css('div#PAY_ON_DELIVERY').get()
        product_detail['returnable']=response.css('div#RETURNS_POLICY').get()
        if product_detail['returnable'] is not None and product_detail['pay_on_delivery'] is not None:
            product_detail['pay_on_delivery']=True
            product_detail['returnable']=True
        else:  
            product_detail['pay_on_delivery']=False
            product_detail['returnable']=False
             
        tr_elements = response.xpath('//div[@class="a-column a-span6 a-spacing-base a-ws-span6"]//table[@id="technicalSpecifications_section_1"]//tr')
        data_dict = {}
        if tr_elements is not None:
            for tr in tr_elements:
                key = tr.xpath('th[@class="a-span5 a-size-base"]/text()').get()
                value = tr.xpath('td[@class="a-span7 a-size-base"]/text()').get()
                if key is not None and value is not None:
                    data_dict[key.strip()] = value.strip()
        if data_dict is not None:    
            product_detail['band_color']=data_dict.get('Band Color' ,'NA')
            product_detail['band_material']=data_dict.get('Band Material' ,'NA')
            product_detail['band_width']=data_dict.get('Band Width' ,'NA')
            product_detail['manufacturer']=data_dict.get('Brand' ,'NA')
            product_detail['case_diameter']=data_dict.get('Case Diameter' ,'NA')
            product_detail['case_material']=data_dict.get('Case Material' ,'NA')
            product_detail['case_thickness']=data_dict.get('Case Thickness' ,'NA')
            product_detail['item_weight']=data_dict.get('Item Weight' ,'NA')
            product_detail['warranty']=data_dict.get('Warranty Description' ,'NA')
        
        
        yield product_detail