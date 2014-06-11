from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json
import re
driver = webdriver.Firefox()
driver.get("https://www.amfiindia.com/nav-history-download")

def selectFund(i):
	driver.find_element_by_xpath('//*[@id="divNavDownMFName"]/span/a/span[2]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="ui-id-1"]/li[%s]'%i).click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="divNavDownType"]/span/a/span[2]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="ui-id-2"]/li[1]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="dpfrom"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[1]/table/thead/tr[1]/th[2]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[2]/table/thead/tr/th[2]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[3]/table/thead/tr/th[1]/i').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[3]/table/thead/tr/th[1]/i').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[3]/table/tbody/tr/td/span[2]').text
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[3]/table/tbody/tr/td/span[2]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[2]/table/tbody/tr/td/span[1]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr[1]/td[2]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="dpto"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[8]/div[1]/table/tbody/tr[3]/td[4]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="hrDownload"]').click()

selectFund(4)



    