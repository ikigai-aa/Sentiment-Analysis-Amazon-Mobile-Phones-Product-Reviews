# Importing Scrapy Library
import scrapy

# Creating a new class to implement Spide
class AmazonReviewSpider(scrapy.Spider):

    # Spider name
    name = 'amazon_review'
	
	# Domain names to scrape
    allowed_domains = ['https://www.amazon.in/']
	
	# Base URL for the Product "All Reviews" page
    myBaseUrl = 'Put the link of the page you want to scrape '+'&pageNumber='
    start_urls=[]
 
    # Creating list of urls to be scraped by appending page number a the end of base url but here for the assigment,
	# we're scrapping 1st page of review only as there are many phones to be scrapped.
    for i in range(1,2):
        start_urls.append(myBaseUrl+ str(i))
 
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
 
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
 
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
 
            # Combining the results
            for review in star_rating:
                yield{'Brand': 'Put the Brand Name you are scraping',
					  'Model': 'Put the Name of the mobile whose reviews you are scraping',
				      'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath('.//text()').extract())
					  
                     }
                count=count+1
    
