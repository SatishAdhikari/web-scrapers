from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time

driver = webdriver.Firefox()
driver.get("http://lipperleaders.com/index.aspx")

element = driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ctl06$cmbUniverse']")
all_options = element.find_elements_by_tag_name("option")

for option in all_options:
	if str(option.get_attribute("value")) == 'SGP':
	    option.click()

driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl06_btnDisplayFund").click()

def main():
	
	
	result = driver.find_elements_by_tag_name('span')
	
	del(result[0])
	del(result[len(result)-1])
	del(result[len(result)-1])

	stars = driver.find_elements_by_tag_name('img')
	img = []

	for star in stars:
		#print str(star)[len(str(star.get_attribute('src')))-5]
 	   	img.append(star.get_attribute('src'))

	ratings = []
	for i in img:
 	   	if i[len(i)-5] == '1' or i[len(i)-5] == '2' or i[len(i)-5] == '3' or i[len(i)-5] == '4' or i[len(i)-5] == '5' or i[len(i)-5] == 'a':
               	  if i[len(i)-5] == 'a':
		    	ratings.append('N/A')
        	  else:
	    		ratings.append(i[len(i)-5])
    	        else:
    		  pass

	#print ratings

	total_return = []
	consistent_return = []
	preservation = []
	expense = []

	chk = 0
	while chk < len(ratings):
		total_return.append(ratings[chk])
		chk += 4

	chk = 1
	while chk < len(ratings):
		consistent_return.append(ratings[chk])
		chk += 4

	chk = 2
	while chk < len(ratings):
		preservation.append(ratings[chk])
		chk += 4

	chk = 3
	while chk < len(ratings):
		expense.append(ratings[chk])
		chk += 4

	#for elem in result:
	#	print elem.text

	chk = 0
	fund_name = []
	fund_company = []
	fund_asset = []
	fund_class = []
	fund_returnper = []
	fund_currency = []

	while chk < len(result):
		fund_name.append(result[chk].text)
		chk += 6

	chk = 1
	while chk < len(result):
		fund_company.append(result[chk].text)
		chk += 6

	chk = 2
	while chk < len(result):
		fund_asset.append(result[chk].text) 
		chk += 6

	chk = 3
	while chk < len(result):
		fund_class.append(result[chk].text)
		chk += 6

	chk = 4
	while chk < len(result):
		fund_returnper.append(result[chk].text)
		chk += 6

	chk = 5
	while chk < len(result):
		fund_currency.append(result[chk].text)
		chk += 6

	pt = PrettyTable(field_names=['Fund Name', 'Fund Company', 'Asset Type', 'Classification', 'Return(3yr) %', 'Currency'])
	pt.align='l'
	[pt.add_row((fund_name[i], fund_company[i], fund_asset[i], fund_class[i], fund_returnper[i], fund_currency[i]))
	for i in range(len(fund_currency))]

	print pt

	pt1 = PrettyTable(field_names=['Fund Name', 'Total Return', 'Consistent Return', 'Preservation', 'Expense'])
	pt1.align='l'
	[pt1.add_row((fund_name[i], total_return[i], consistent_return[i], preservation[i], expense[i]))
	for i in range(len(fund_currency))]


	print pt1
        

main()

# number of pages

for i in range(20):

	driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucDataPager_btnNext").click()
	time.sleep(8)  #### stay away bitch :| let him sleep till the page loads :D :D  
	main()

	

