from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json
driver = webdriver.Firefox()
driver.get("http://www.fundsupermart.co.in/main/fundinfo/generateTable.svdo")

def main():

	    
	    
        
        #print result
        link = 0
        for r in range(500):
            d = dict()
            result = driver.find_elements_by_class_name('sidetext')
            name = str(result[link].text)
            #print name
            result[link].click()
            
            #driver.get
    	    time.sleep(5)
            tables = driver.find_elements_by_xpath('//table[@bgcolor="#CCCCCC"]')

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
 
            if d['Fundsupermart Risk Rating'] != '-Not Sold By FSM':
                driver.get('http://www.fundsupermart.co.in/main/fundinfo/viewFundcardSnapshot.svdo?sedolnumber='+str(u[len(u)-1].split('.')[0]))
                time.sleep(3)
            else:
                driver.get("http://www.fundsupermart.co.in/main/fundinfo/generateTable.svdo")
                time.sleep(5)
                link += 1
                continue

            tables = driver.find_elements_by_xpath('//table[@bgcolor="#CCCCCC"]')

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
                        
            print d

            driver.get("http://www.fundsupermart.co.in/main/fundinfo/generateTable.svdo")
            time.sleep(5)
            link += 1

main()

