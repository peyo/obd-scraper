# -*- coding: utf-8 -*-
import scrapy

class ObdbotSpider(scrapy.Spider):
    name = 'obdbot'
    allowed_domains = ['www.obd-codes.com/gm']
    start_urls = ['https://www.obd-codes.com/gm']

    def parse(self, response):
        #extracting the content using xpath selectors
        All = response.xpath("//p[6]//text()").getall()
      
        AllOne = {i.replace('\n', '') for i in All}
        AllTwo = {i.rstrip() for i in AllOne}
        
        AllThree = []
        for i in AllTwo:
          if i.startswith("DTC "):
            AllThree.append(i[4:])
          else:
            AllThree.append(i)

        DTC = []
        for i in AllThree:
          DTC.append(i[:5])

        Description = []
        for i in AllThree:
          Description.append(i[6:])
        
        #give the extracted content row wise
        for i in zip(DTC, Description):
            #create a dictionary to store the scraped info
            scraped_info = {
                'DTC' : i[0],
                'Description' : i[1]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info