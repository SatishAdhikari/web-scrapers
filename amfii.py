from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json
import re
driver = webdriver.Firefox()
driver.get("https://www.amfiindia.com/net-asset-value")

def main():
    
    driver.find_element_by_xpath("""//*[@id="divfundname"]/span/a/span[2]""").click()
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="ui-id-6"]/li[1]""").click()
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="divopenendscheme"]/span/a/span[2]""").click()
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="ui-id-7"]/li[2]""").click()
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="divcloseendscheme"]/span/a/span[2]""").click()
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="ui-id-8"]/li[2]""").click()
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="hrfNav"]""").click()
    time.sleep(5)

    all_tr = driver.find_elements_by_tag_name('tr') # This will take a lot of time !! about 60-90 seconds
    time.sleep(90)

    ans = []
    for tr in all_tr[5:30]:
        temp = []
        all_td = tr.find_elements_by_tag_name('td')
        if all_td == []:
            continue
        else:
            for td in all_td:
                temp.append(td.text)
        ans.append(temp)
    print ans

    
    

main()
