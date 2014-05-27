from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field
from scrapy.spider import BaseSpider
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from scrapy.http import Request
import urlparse
from urlparse import urljoin
import sys

#class logItem(Item):
class FundsupermartSpider(CrawlSpider):

        name = 'fund'
        allowed_domains = ['fundsupermart.co.in']
        link_crawl = 'http://www.fundsupermart.co.in/main/fundinfo/newFunds.svdo?'
        #start_urls = ['http://www.fundsupermart.co.in/main/fundinfo/newFunds.svdo?']
        start_urls = ['http://www.fundsupermart.co.in/']
        rules = [Rule(SgmlLinkExtractor(allow=(link_crawl)), callback='parse_item', follow=True)]
        def parse_item(self,response):
            code = response.body
            #print code
            #print link_crawl
            soup = BeautifulSoup(code)
            ans = soup.find('table', {'border':'0', 'width':'100%', 'cellspacing':'1', 'cellpadding':'3', 'bgcolor':'#CCCCCC'})
            ans1 = ans.findAll('a')
            invalid_tags = ['html', 'body', 'a', 'img']
            names = []
            links = []
            for elem in ans1:
                soup = BeautifulSoup(str(elem))
                names.append(soup.get_text())
                #print soup.get_text()
                links.append('http://fundsupermart.co.in/main'+elem['href'][2:])
                #print elem.string
            for i in range(len(links)):
                if i%2 != 0:
                    links[i] = None
            pt = PrettyTable(field_names=['New Fund Offers', 'Links'])
            pt.align = 'l'
            [pt.add_row((names[i], links[i]))
            for i in range(len(names))]
            #print 'hey'
            print pt
            
            for link in links:
                if link is not None:
                    yield Request(str(link),callback=self.parseSubcategory)
                    #yield Request(str(link), callback = self.parseSubcategory)

        def parseSubcategory(self, response):
            soup = BeautifulSoup(response.body)
            ans = soup.findAll('tr', {'class':'table_bdrow1_style'})
            all_td = []
            all_td1 = []
            for elem in ans:
                soup1 = BeautifulSoup(str(elem))
                f = soup1.find('td', {'class':'table_header_style'}, 'a')
                f1 = soup1.find('td', {'class':'table_bdtext_style'}, 'a')
                if f is not None:
                    all_td.append((f).get_text())
                else:
                    all_td.append('None')
                if f1 is not None:
                    all_td1.append((f1).get_text())
                else:
                    all_td1.append('None')
                
                #all_td.append(soup1.find('td', {'class':'table_header_style'}).get_text())
                #all_td1.append(soup1.find('td', {'class':'table_bdtext_style'}).get_text())
                #all_td.append(soup1.find('td', {'class':'table_header_style'}))
                #all_td1.append(soup1.find('td', {'class':'table_bdtext_style'}))
           
            for i in range(len(all_td1)):
                #x = bytes(all_td1[i]).decode('unicode-escape').encode('ascii','ignore')
                #x = all_td1[i].translate(None, '\n')
                all_td1[i] = all_td1[i].strip()
                all_td[i] = all_td[i].strip()
                
            pt = PrettyTable(field_names=['Categories', 'Result'])
            pt.align = 'l'
            
            [pt.add_row((all_td[i], all_td1[i]))
            for i in range(len(all_td))]
            
            print pt
            
            """print '='*60
            for i in range(len(all_td)):
                print all_td[i].encode('utf-8')
            print '-'*50
            for i in range(len(all_td1)):
                print all_td1[i].encode('utf-8')"""




            



