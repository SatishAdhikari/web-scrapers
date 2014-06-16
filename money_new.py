from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json
import re
driver = webdriver.Firefox()

def category(i):
  try:

	driver.get("http://www.moneycontrol.com/mutual-funds/performance-tracker/returns/large-cap.html")
	windowHandle()
	d = dict()
	d['i'] = i
	# name of the fund from the 1st screen
	d['name'] = driver.find_element_by_xpath('//*[@id="tCont1"]/div[2]/table/tbody/tr[%s]/td[1]/a'%i).text
	# aum of the fund from the 1st screen
	d['aum'] = driver.find_element_by_xpath('//*[@id="tCont1"]/div[2]/table/tbody/tr[%s]/td[3]'%i).text
	# crisil rank of the fund from the 1st screen
	d['currentCrisilRank'] = driver.find_element_by_xpath('//*[@id="tCont1"]/div[2]/table/tbody/tr[%s]/td[2]/a[1]'%i).text
	#click and open fund info
	driver.find_element_by_xpath('//*[@id="tCont1"]/div[2]/table/tbody/tr[%s]/td[1]/a'%i).click()
	time.sleep(10)
	windowHandle()			# handling and closing pop up ads on click
	url = driver.current_url
	url = url.split('/')
	url = url[len(url)-1]
	d['selfId'] = str(url)	# ID as given in the link
	# NAV, NAVchange, NAVpercent of the fund given top of the page
	d['nav'] = driver.find_element_by_xpath('//*[@id="Bse_Prc_tick"]/strong').text
	d['navChange'] = driver.find_element_by_xpath('//*[@id="newMFpg"]/div[2]/div/div[1]/div[2]/span/strong').text
	
	temp = driver.find_element_by_xpath("""//*[@id="newMFpg"]/div[2]/div/div[1]/div[2]/span""").text

	# extracting date and nav change percentage by regex
	d['navChangePercentage'] = re.search('\(.*\%\)', temp).group()[1:-2]
	temp = driver.find_element_by_xpath("""//*[@id="newMFpg"]/div[2]/div/div[1]/div[3]""").text
	d['date'] = re.search('NAV as on (.*)', temp).groups()[0]

	d['fundFamily'] = driver.find_element_by_xpath("""//*[@id="newMFpg"]/div[2]/div/div[2]/p[1]/a""").text
	d['fundClass'] = driver.find_element_by_xpath("""//*[@id="newMFpg"]/div[2]/div/div[2]/p[2]/a""").text

	###############
	#   returns   #
	###############

	tbl = driver.find_elements_by_xpath('//table[@class="tblporhd"]')

	#p = driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[3]/div[1]/table/tbody""")
	p = tbl[0]
	q = p.find_elements_by_tag_name('tr')
	d['returns'] = []
	for elem in q[1:]:
		r = elem.find_elements_by_tag_name('td')
		temp = {}
		temp['period'] = r[0].text
		temp['returns'] = r[1].text
		temp['rank'] = r[2].text
		d['returns'].append(temp)

	#######################	
	#   Absolute Returns  #
	#######################

	#p = driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[3]/div[2]/table/tbody""")
	p = tbl[1]
	q = p.find_elements_by_tag_name('tr')
	d['absoluteReturns'] = []
	for elem in q[1:]:
		r = elem.find_elements_by_tag_name('td')
		temp = {}
		temp['year'] = r[0].text
		temp['qtr1'] = r[1].text
		temp['qtr2'] = r[2].text
		temp['qtr3'] = r[3].text
		temp['qtr4'] = r[4].text
		temp['annual'] = r[5].text
		d['absoluteReturns'].append(temp)

	#Expanding all options

	#driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[5]/a[1]""").click()
	driver.find_element_by_xpath('//a[@class="expandA"]').click()

	windowHandle()
	time.sleep(1)

	####################
	#  Scheme Details  #
	####################

	tables = driver.find_elements_by_xpath('//table[@class="invtbl"]')

	#p = driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[7]/div/div[1]/div/table/tbody""")
	p = tables[0]
	q = p.find_elements_by_tag_name('tr')

	for elem in q:
		key = elem.find_element_by_tag_name('th').text
		value = elem.find_element_by_tag_name('td').text
		d[key] = value

	##################	
	#  Load Details  #
	##################

	#p = driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[7]/div/div[2]/div[1]/table/tbody""")
	p = tables[1]
	q = p.find_elements_by_tag_name('tr')

	for elem in q:
		key = elem.find_element_by_tag_name('th').text
		value = elem.find_element_by_tag_name('td').text
		d[key] = value

	####################	
	#  Contact Details #
	####################

	#p = driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[7]/div/div[2]/div[2]/table/tbody""")
	p = tables[2]
	q = p.find_elements_by_tag_name('tr')

	for elem in q:
		key = elem.find_element_by_tag_name('th').text
		value = elem.find_element_by_tag_name('td').text
		d[key] = value

	##############	
	#  Holdings  #
	##############

	#p = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[9]/div[1]/div[1]/table/tbody')
	p = tbl[2]
	q = p.find_elements_by_tag_name('tr')
	d['holdings'] = []

	for elem in q[1:]:
		r = elem.find_elements_by_tag_name('td')
		temp = {}
		temp['equity'] = r[0].text
		temp['sector'] = r[1].text
		temp['value'] = r[2].text
		temp['assets'] = r[3].text
		d['holdings'].append(temp)

	######################	
	#  Sector Allocation #
	######################

	#p = driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[9]/div[1]/div[2]/table/tbody""")
	p = tbl[3] 
	q = p.find_elements_by_tag_name('tr')
	d['sectorAllocation'] = []

	for elem in q[1:]:
		r = elem.find_elements_by_tag_name('td')
		temp = {}
		temp['sector'] = r[0].text
		temp['value'] = r[1].text
		temp['high'] = r[2].text
		temp['low'] = r[3].text
		d['sectorAllocation'].append(temp)

	####################	
	# Asset Allocation #
	####################

	#p = driver.find_element_by_xpath("""//*[@id="mmcnt"]/div[2]/div[9]/div[2]/div[1]/table/tbody""")
	p = tbl[4]
	q = p.find_elements_by_tag_name('tr')
	d['assetAllocation'] = []

	for elem in q[1:]:
		r = elem.find_elements_by_tag_name('td')
		temp = {}
		temp['class'] = r[0].text
		temp['value'] = r[1].text
		d['assetAllocation'].append(temp)

	#################
	# Concentration #
	#################

	#p = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[9]/div[2]/div[2]/table[1]/tbody')
	p = tbl[5]
	q = p.find_elements_by_tag_name('tr')
	d['concentration'] = []

	for elem in q[1:]:
		temp = {}
		r = elem.find_elements_by_tag_name('td')
		temp['type'] = 'Holdings'
		temp['attribute'] = r[0].text
		temp['value'] = r[1].text
		d['concentration'].append(temp)

	#p = driver.find_element_by_xpath('//*[@id="mmcnt"]/div[2]/div[9]/div[2]/div[2]/table[2]/tbody')
	p = tbl[6]
	q = p.find_elements_by_tag_name('tr')

	for elem in q[1:]:
		r = elem.find_elements_by_tag_name('td')
		temp = {}
		temp['type'] = 'Sector'
		temp['attribute'] = r[0].text
		temp['value'] = r[1].text
		d['concentration'].append(temp)

	with open('money_new.json', 'a') as data:
		data.write(json.dumps(d, indent=2))
		data.write(",")

	print json.dumps(d, indent=2)
	#print holdings
	return True
  
  except:
  	return True

def main():
    
    i = 108
    chk = True
    while chk:
        chk = category(i)
        i += 1

def windowHandle():
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to_window(windows[1])
        driver.close()
        driver.switch_to_window(windows[0])
    return

main()
