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
            result = driver.find_elements_by_class_name('sidetext')
            #print result[link].text
            result[link].click()
            
            #driver.get
    	    time.sleep(8)

    	    t = driver.find_elements_by_class_name('table_header_style')
    	    t1 = driver.find_elements_by_class_name('table_bdtext_style')

    	    table_dict = dict()
       	    for i in range(15):
                table_dict[t[i].text] = t1[i+1].text
    	    #print result[chk].text
            #print '='*50
            print json.dumps(table_dict, indent=2)

            driver.find_element_by_css_selector("a[href='javascript:viewfundcard();']").click()
            time.sleep(8)
            
            handle = driver.window_handles
            print handle
            driver.switch_to_window(handle[1])

            t2 = driver.find_elements_by_class_name('table_header_style')
            t3 = driver.find_elements_by_class_name('table_bdtext_style')

            d1 = dict()
            d2 = dict()
            d3 = dict()
            d4 = dict()
            d5 = dict()
            d6 = dict()


            fund_info = []
            fund = []
            percent_asset = []
            risk_measures = []
            category_avg = []
            qs = []
            additional = []


 
            for i in range(7):
                fund_info.append(t3[i].text)
                d1[t2[i].text] = t3[i].text
            chk = 7
            for i in range(7, 15):
                fund.append(t3[chk].text)
                category_avg.append(t3[chk+1].text)  
                d2[t2[i].text] = [t3[chk].text, t3[chk+1].text]
                chk += 2
            chk1 = chk+1
            for i in range(15, 18):
                percent_asset.append(t3[chk1].text)
                d3[t2[i].text] = t3[chk1].text
                chk1 += 1
            for i in range(18, 20):
                risk_measures.append(t3[chk1].text)
                d4[t2[i].text] = t3[chk1].text
                chk += 1

            chk2 = chk1+2
            for i in range(20, 25):
                qs.append([t3[chk2].text, t3[chk2+1].text, t3[chk2+2].text, t3[chk2+3].text])
                d5[t2[i].text] = [t3[chk2].text, t3[chk2+1].text, t3[chk2+2].text, t3[chk2+3].text]
                chk2 += 4
            for i in range(25, 32):
                additional.append(t3[chk2].text)
                d6[t2[i].text] = [t3[chk2].text]
                chk2 += 1

            driver.close()
            driver.switch_to_window(handle[0])

            #print '##'*50
            print json.dumps(d1, indent=2)
            #print '='*50
            print json.dumps(d2, indent=2)
            #print '='*50
            print json.dumps(d3, indent=2)
            #print '='*50
            print json.dumps(d4, indent=2)
            #print '='*50
            print json.dumps(d5, indent=2)
            #print '='*50
            print json.dumps(d6, indent=2)

            driver.get("http://www.fundsupermart.co.in/main/fundinfo/generateTable.svdo")
            time.sleep(5)
            link += 1

main()

