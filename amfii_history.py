# this code will end with an exception so don't panic !! i.e. when ( i > total number of funds )
# Not used try catch (Too Lazy :P)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json
import re
driver = webdriver.Firefox()


def selectFund(i):
	
	#try:
		driver.get("https://www.amfiindia.com/nav-history-download")

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
		time.sleep(6)
		driver.switch_to_window(driver.window_handles[1])
		time.sleep(1)
		soup = BeautifulSoup(driver.page_source)
		
		str_content = driver.find_element_by_tag_name('pre').text
		list_content = str_content.split('\n')
		
		ans = []
		#print list_content[6:10]
		for elem in list_content[6:]:
			temp = elem.split(';')
			d = dict()

			if len(temp) != 6:
				continue
			d['Scheme Code']		=	temp[0]
			d['Scheme Name']		=	temp[1]
			d['Net Asset Value']	=	temp[2]
			d['Repurchase Price']	=	temp[3]
			d['Sale Price']			=	temp[4]
			d['Date']				=	temp[5]	
			ans.append(d)

		t = open((list_content[5]+'.json'), 'w')
		t.write(json.dumps(ans, indent=2))
		t.close()

		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		return True



	#except:
	#	return False

	#return True

def main():

	i = 15
	chk = True
	while chk:
		chk = selectFund(i)
		i += 1
		print i 
	print "========That's it=========="

main()	



    