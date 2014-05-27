from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field
from scrapy.spider import BaseSpider
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from scrapy.http import Request
import urlparse
from urlparse import urljoin
from scrapy.selector import Selector
import json

#class logItem(Item):
class FundsupermartSpider(CrawlSpider):

        name = 'masnet'
        allowed_domains = ['masnet.mas.gov.sg']
        link_crawl = 'http://masnet.mas.gov.sg/opera/sdrprosp.nsf/vewPublicLatestCIS'
        #start_urls = ['http://www.fundsupermart.co.in/main/fundinfo/newFunds.svdo?']
        start_urls = ['http://masnet.mas.gov.sg/opera/sdrprosp.nsf/vewPublicLatestCIS']
        rules = [Rule(SgmlLinkExtractor(allow=(link_crawl)), callback='parse_item', follow=True)]
        def parse_item(self, response):
        	
                sel = Selector(response)
                description = sel.xpath('//table[@cellpadding="2"]/tr/td/font/text()').extract()
                links = sel.xpath('//table[@cellpadding="2"]/tr/td/font/a/text()').extract()             # CIS links
                paths = sel.xpath('//table[@cellpadding="2"]/tr/td/font/a/@href').extract()              # hrefs
                
                
                for i in range(len(paths)):
                    paths[i] = 'http://masnet.mas.gov.sg'+paths[i]


                #print paths
                #print description
                #print '='*160
                #print links
                #print result
                #print json.dumps(result, indent=4)
                
                chk = 0
                offeror = []
                umb_fund = []
                status = []
                scheme_status = []
                while chk < len(description):
                    offeror.append(description[chk])  
                    chk+=4

                chk=1
                while chk < len(description):
                    umb_fund.append(description[chk])  
                    chk+=4  

                chk = 2
                while chk < len(description):
                    status.append(description[chk])  
                    chk+=4

                chk = 3    
                while chk < len(description):
                    scheme_status.append(description[chk])  
                    chk+=4              

                #print offeror

                #pt = PrettyTable(field_names=['CIS Links', 'Offeror', 'Umbrella Fund', 'Status', 'Scheme Status'])
                pt = PrettyTable(field_names=['CIS Links', 'Offeror'])
                pt.align='l'
                [pt.add_row((links[i], offeror[i]))
                for i in range(len(links))]

                pt1 = PrettyTable(field_names=['CIS Links', 'Umbrella Fund'])
                pt1.align = 'l'
                [pt1.add_row((links[i], umb_fund[i]))
                for i in range(len(links))]

                pt2 = PrettyTable(field_names=['CIS Links', 'Status'])
                pt2.align = 'l'
                [pt2.add_row((links[i], status[i]))
                for i in range(len(links))]

                pt3 = PrettyTable(field_names=['CIS Links', 'Scheme Status'])
                pt3.align = 'l'
                [pt3.add_row((links[i], scheme_status[i]))
                for i in range(len(links))]

                print pt
                print pt1
                print pt2
                print pt3

                

                """for path in paths:
                    if path is not None:
                        yield Request(str(path),callback=self.parseSubcategory)
                

        def parseSubcategory(self, response):
                
                sel = Selector(response)
                href_detail = sel.xpath('//table[@class="TableColor"]/tr/td/font/text()').extract()"""





                



                




