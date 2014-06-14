from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json
import re
driver = webdriver.Firefox()


def largeCap(i):
    
    driver.get('http://www.moneycontrol.com/mutual-funds/performance-tracker/returns/small-and-mid-cap.html')
    windowHandle()
    d = dict()
    d['i'] = i

    d['name'] = driver.find_element_by_xpath('//*[@id="tCont1"]/div[2]/table/tbody/tr[%s]/td[1]/a'%i).text
    driver.find_element_by_xpath('//*[@id="tCont1"]/div[2]/table/tbody/tr[%s]/td[1]/a'%i).click()
    time.sleep(10)
    d['NAV'] = driver.find_element_by_xpath('//*[@id="Bse_Prc_tick"]/strong').text
    url = driver.current_url
    url = url.split('/')
    url = url[len(url)-1]
    windowHandle()

    driver.get('http://www.moneycontrol.com/india/mutualfunds/mfinfo/investment_info/'+str(url))
    #time.sleep(20)
    windowHandle()
    d['selfGeneratedID'] = str(url)
    #driver.find_element_by_xpath('//*[@id="a_2"]').click()
    #time.sleep(15)
    #windowHandle()
    
    scheme_details = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[1]/div[4]/div[1]')
    details = scheme_details.find_elements_by_xpath('//div[@class="brdb PT3 PB5 b13 PL10"]')
    for elem in details:
        d[elem.text.split('\n')[0]] = elem.text.split('\n')[1] 

    #print (left_scheme)
    #print (right_scheme)
    


    #driver.get('http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_overview/'+str(url))
    driver.get('http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/'+str(url))


    #driver.find_element_by_xpath('//*[@id="a_4"]').click()
    #time.sleep(8)
    windowHandle()

    #holdings = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[1]/div[1]/div[2]/table/tbody')
    #sector_allo = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[1]/div[2]/div[2]/table[2]/tbody')
    #asset = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[2]/div[1]/div[2]/div')
    d['holdings'] = []
    d['sectorAllocation'] = []
    d['assetAllocation'] = []

    holdings1 = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/table[1]/tbody')

    
    hold = holdings1.find_elements_by_tag_name('tr')
    for elem in hold[1:]:
        tmp = []
        td = elem.find_elements_by_tag_name('td')
        tmp.append(td[0].text)
        tmp.append(td[1].text)
        tmp.append(td[2].text)
        tmp.append(td[3].text)
        d['holdings'].append(tmp)


    driver.get('http://www.moneycontrol.com/india/mutualfunds/mfinfo/sector_allocation/'+str(url))
    windowHandle()
    sector_allo1 = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[1]/div[2]/table/tbody')
    sect = sector_allo1.find_elements_by_tag_name('tr')
    for elem in sect[1:]:

        tmp = []
        td = elem.find_elements_by_tag_name('td')
        tmp.append(td[0].text)
        tmp.append(td[1].text)
        tmp.append(td[2].text)
        tmp.append(td[3].text)
        d['sectorAllocation'].append(tmp)

    """driver.get('www.moneycontrol.com/india/mutualfunds/mfinfo/asset_allocation/'+str(url))
    windowHandle()
    asset_breakup = driver.find_element_by_xpath('p//*[@id="mmcnt"]/div[2]/div[2]/div[1]')

    ass = asset_breakup.find_elements_by_xpath('//div[@class="PT3 PB3 brdb PR10"]')

    for elem in ass:
        tmp = []
        tmp.append(elem.text.split('\n')[0])
        tmp.append(elem.text.split('\n')[1])
        d['assetAllocation'].append(tmp)"""
    
    #time.sleep(8)

    #print scheme_details
    #print load_details

    with open('data_moneycontrol_small-mid_cap.json', 'a') as data:
                data.write(json.dumps(d, indent=2))
                data.write(",")

    print json.dumps(d, indent=2)
    #print holdings
    return True

def main():
    i = 4
    chk = True
    while chk:
        chk = largeCap(i)
        i += 1

def windowHandle():
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to_window(windows[1])
        driver.close()
        driver.switch_to_window(windows[0])
    return

main()
