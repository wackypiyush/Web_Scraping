import scrapy
import random

from bookscraper.items import BookItem
class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]
    
    # def start_requests(self):
    #     urls = [
    #         "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    #         "https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    
    
    # User Agents list for not so complex websites and number of requests
    # user_agent_list=[
    #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    #     'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2210.121',
    #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
    # ]
            
    def parse(self, response):
        
    # It is to save the whole html of these pages above(URL)
        # page = response.url.split("/")[-2]
        # filename = f"books-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
        
    # Saved the extracted data to csv 
        # all_books=[]
        # cards=response.css(".product_pod")
        # for card in cards:
        #     title=card.css("h3>a").attrib['title']
        #     #print(title)
            
        #     image=card.css(".image_container img").attrib['src']
        #     #print(image)
            
        #     rating=card.css(".star-rating").attrib['class']
        #     #print(rating.split(" ")[-1])
            
        #     price=card.css(".price_color::text").get()
        #     #print(price)
            
        #     stock=card.css(".availability")
        #     if len(stock.css(".icon-ok"))>0:
        #         inStock=True
        #     else:
        #         inStock=False
        #     all_books.append([title, image.replace('../../../../','https://books.toscrape.com/'), rating.split(" ")[-1], price, inStock])
       
        # df=pd.DataFrame(data=all_books, columns=['Title', 'Image', 'Ratings', 'Price', 'Availability'])
        # #print(df)
        # page = response.url.split("/")[-2]
        # df.to_csv(f'{page}.csv', index=False)
        # print("File Saved")
            
            
    # Scraping from each page of the website from next button        
        # cards=response.css(".product_pod")
        # for card in cards:
        #     yield{
        #     'title': card.css("h3>a").attrib['title'],
            
        #     'image':card.css(".image_container img").attrib['src'],
            
        #     'rating':card.css(".star-rating").attrib['class'],
            
        #     'price':card.css(".price_color::text").get()
        # }        
            
        # next_page=response.css("li.next>a").attrib['href']
        # if next_page is not None:
        #     if 'catalogue/' in next_page:
        #         next_page_url='https://books.toscrape.com/' + next_page
        #     else:
        #         next_page_url='https://books.toscrape.com/catalogue/' + next_page
        #     yield response.follow(next_page_url, callback=self.parse)
        
    
    
    # Scraping each books data by going to specific books url from all pages of the website
    # To save file in any extension use command=    scrapy crawl <spider name> -O name.csv
    # Using user_agent_list randomly to pick a user-agent for proxy
        cards=response.css("article.product_pod")
        for card in cards:           
            relative_url=card.css("h3>a").attrib['href']
            if relative_url is not None:
                if 'catalogue/' in relative_url:
                    book_url='https://books.toscrape.com/' + relative_url
                else:
                    book_url='https://books.toscrape.com/catalogue/' + relative_url
                yield response.follow(book_url, callback=self.parse_book_page)
                # ,headers={"User-Agent":self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]}
    
        next_page=response.css("li.next>a").attrib['href']
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url='https://books.toscrape.com/' + next_page
            else:
                next_page_url='https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse)
            # ,headers={"User-Agent":self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]}
    
    # Directly yieling        
    # def parse_book_page(self, response):
    #     page=response.css("article.product_page")
    #     table_rows=response.css("table tr")
    #     yield{
    #         'url':response.url,
    #         'title':page.css(".product_main>h1::text").get(),
    #         'price':page.css(".price_color::text").get(),
    #         'rating':page.css(".star-rating").attrib['class'].split(" ")[-1] ,   
    #         'description':response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
    #         'num_reviews': table_rows[6].css("td::text").get(),
    #         'category':response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
    #     }
    
    
   # Using items.py and pipelines.py to yield 
    def parse_book_page(self, response):
        page=response.css("article.product_page")
        table_rows=response.css("table tr")
        book_item=BookItem()
        
        book_item['url']=response.url,
        book_item['title']=page.css(".product_main>h1::text").get(),
        book_item['price']=page.css(".price_color::text").get(),
        book_item['rating']=page.css(".star-rating").attrib['class_'].split(" ")[-1] ,   
        book_item['description']=response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        book_item['num_reviews']= table_rows[6].css("td::text").get(),
        book_item['category']=response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        
        yield book_item