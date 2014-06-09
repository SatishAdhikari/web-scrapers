from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json
import re
driver = webdriver.Firefox()
driver.get("http://www.fundsupermart.co.in/main/fundinfo/generateTable.svdo")

def main():

        
        
        
        #print result
        #attr = {}
        link = 65
        for r in range(500):
            d = dict()
            attr = dict()
            bttr = dict()
            cttr = dict()
            result = driver.find_elements_by_class_name('sidetext')
            name = str(result[link].text)
            d['name'] = name
            #print name
            result[link].click()
            
            #driver.get
            time.sleep(5)
            tables = driver.find_elements_by_xpath('//table[@bgcolor="#CCCCCC"]')
            #print tables

            for table in tables:
                rows = table.find_elements_by_tag_name('tr')
                for row in rows:
                    if row.get_attribute('class') != 'table_headline_style':
                        columns = row.find_elements_by_tag_name('td')
                        key = columns[0].text
                        value = []
                        for elem in columns[1:]:
                            value.append(elem.text)
                        if len(value) == 1:
                            d[key] = value[0]
                        else:
                            d[key] = value
                    else:
                        pass        
        
            url = driver.current_url
            u = url.split('-')

            fh = driver.find_elements_by_xpath('//td[@colspan="3"][@class="articlepg_bdtext"]')
            tag = fh[len(fh)-1].find_element_by_tag_name('a')
            href = tag.get_attribute('href')
            driver.get(href)
            time.sleep(2)
            fund_house = dict()
            url1 = driver.current_url
            u1 = url1.split('=')[1]


            tables = driver.find_elements_by_xpath('//table[@width="100%"][@border="0"][@cellspacing="0"][@cellpadding="0"]')
            table = tables[len(tables)-2]
            rows = table.find_elements_by_tag_name('tr')
            d['fundhouse_name'] = driver.find_element_by_class_name('articlepg_subhead').text
            for i in range(len(rows)):
                if i == 0:
                    add = rows[i].text.replace('\n', ' ')
                    d['fundhouse_address'] = add
                    d['fundhouse_country'] = rows[i].text.split('\n')[len(rows[i].text.split('\n'))-1]
                else:
                    d[rows[i].text.split(':')[0]] = rows[i].text.split(':')[1]
            #print fund_house
            #print 

            #print d
            
            if d['Fundsupermart Risk Rating'] != '-Not Sold By FSM':
                driver.get('http://www.fundsupermart.co.in/main/fundinfo/viewFundcardSnapshot.svdo?sedolnumber='+str(u[len(u)-1].split('.')[0]))
                time.sleep(3)
            else:
                driver.get("http://www.fundsupermart.co.in/main/fundinfo/generateTable.svdo")
                time.sleep(5)
                link += 1
                continue

            tables = driver.find_elements_by_xpath('//table[@bgcolor="#CCCCCC"]')
            heading = driver.find_elements_by_xpath('//td[@class="articlepg_subhead"]')
            count = 0
            sentinel = -9999

            for table in tables:
                rows = table.find_elements_by_tag_name('tr')
                temp_list = []
                for row in rows:
                    if row.get_attribute('class') != 'table_headline_style':

                        columns = row.find_elements_by_tag_name('td')
                        if heading[count].text == 'TOP 5 HOLDING' or heading[count].text == 'COMPOSITION' or heading[count].text == 'TOP 5 SECTORS' or heading[count].text == 'TOP 5 HOLDING' or heading[count].text == 'NEW ENTRY' or heading[count].text == 'NEW EXIT':
                            
                            temp = {}
                            key = columns[0].text
                            value = columns[1].text
                            temp[key] = value
                            temp_list.append(temp)
                            sentinel = 9999

                        else:
                            
                            key = columns[0].text
                            value = []
                            for elem in columns[1:]:
                                value.append(elem.text)
                            if len(value) == 1:
                                d[key] = value[0]
                            else:
                                d[key] = value
                    else:
                        pass

                if sentinel == 9999 and len(temp_list) != 0:
                    d[heading[count].text] = temp_list
                else:
                    pass
                count += 1
            #attr = d            
            #print json.dumps(d, indent=2)

            attr['fundCategory']                = d.get('Fund Category')
            attr['fundClass']                   = d.get('Fund Class')
            attr['FundType']                    = d.get('Fund Type')
            attr['options']                     = d.get('Options')
            attr['name']                        = d.get('name')
            attr['founded']                     = d.get('Launch Date')
            attr['startDate']                   = d.get('Launch Date')
            attr['endDate']                     = d.get('End Date')
            attr['minSubsequentInvest']         = d.get('Minimum Subsequent Investment')
            attr['minInitialInvest']            = d.get('Minimum Initial Investment')
            attr['minRedemptionAmount']         = d.get('Minimum Redemption Amount')
            attr['transactionTimeRedemption']   = d.get('Transaction Time for Redemption')
            attr['entryLoad']                   = d.get('Entry Load')
            attr['exitLoad']                    = d.get('Exit Load')
            attr['top5Holding']                 = d.get('TOP 5 HOLDING')
            attr['top5Sectors']                 = d.get('TOP 5 SECTORS')
            attr['composition']                 = d.get('COMPOSITION')
            attr['newEntry']                    = d.get('NEW ENTRY')
            attr['newExit']                     = d.get('NEW EXIT')
            attr['benchmark']                   = d.get('Benchmark')[0]
            attr['country']                     = d.get('fundhouse_country')
            attr['fundHouseId']                 = str(u1)
            attr['link']                        = link + r

            bttr['name']                        = d.get('fundhouse_name')
            bttr['email']                       = d.get('Email ')
            bttr['addressName']                 = d.get('fundhouse_address')
            bttr['country']                     = d.get('fundhouse_country')
            bttr['phone']                       = d.get('Tel ')
            bttr['aum']                         = d.get('AUM (Cr.)')

            temp_date = re.search('\((.*)\)', d['Latest NAV Price (Click here for price history)']).group()[1:-1]
            #temp_date = 0
            cttr['fundId']                      = str(u[len(u)-1].split('.')[0])
            cttr['price']                       = d.get('NAV')
            cttr['threeYearSharpeRatioDate']    = temp_date
            cttr['threeYearSharpeRatioPrice']   = d.get('3 yr Sharpe ratio')
            cttr['threeYearVolatilityDate']     = temp_date
            cttr['threeYearVolatility']         = d.get('3 yr Annualised Volatility')
            cttr['threeMonthsReturnDate']       = temp_date
            cttr['threeMonthsReturnPrice']      = d.get('NAV Returns (%) - INR')[2]
            cttr['sixMonthsReturnDate']         = temp_date
            cttr['sixMonthsReturnPrice']        = d.get('NAV Returns (%) - INR')[3]
            cttr['oneYearReturnPrice']          = [d.get('1 Year')[0], d.get('1 Year')[1]]
            cttr['twoYearReturnPrice']          = [d.get('2 Year')[0], d.get('2 Year')[1]]
            cttr['threeYearReturnPrice']        = [d.get('3 Year')[0], d.get('3 Year')[1]]
            cttr['fiveYearReturnPrice']         = [d.get('5 Year')[0], d.get('5 Year')[1]]
            cttr['oneYearStandardDeviation']    = d.get('Standard Deviation')       
            
            if d.get('NAV') != None:
                cttr['priceDate']               = re.search('\((.*)\)', d['NAV']).group()[1:-1]






            for key in attr:
                if attr[key] == None:
                    attr[key] = 'N/A'


            print json.dumps(attr, indent=2)
            print json.dumps(bttr, indent=2)
            print json.dumps(cttr, indent=2)
            final = dict()
            bttr_final = dict()
            cttr_final = dict()
            final['a'] = attr
            final['b'] = bttr
            final['c'] = cttr
            with open('fundhouse1.json', 'a') as fundhouse:
                fundhouse.write(json.dumps(bttr, indent=2))
                fundhouse.write(',')
            with open('fundmetrics1.json', 'a') as fundmetrics:
                fundmetrics.write(json.dumps(cttr, indent=2))
                fundmetrics.write(',')
            with open('funds1.json', 'a') as funds:
                funds.write(json.dumps(attr, indent=2))
                funds.write(',')


            with open('data1.json', 'a') as data:
                data.write(json.dumps(final, indent=2))
                data.write(",")

            driver.get("http://www.fundsupermart.co.in/main/fundinfo/generateTable.svdo")
            time.sleep(5)
            link += 1

main()

