from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
driver = webdriver.Firefox()
driver.get("http://sg.morningstar.com/ap/fundselect/results.aspx?onshore=All")

def main():

    

    result = driver.find_elements_by_class_name('msDataText')                  # fund name, fund category and fund rating
    b = driver.find_elements_by_class_name('msDataNumeric')                    # expense ratio and current rate
    content = []

    for elem in result:
	if elem.text == u'':
	    a = elem.find_element_by_tag_name('img').get_attribute('src')
            content.append(a[len(a)-5])
   	else:
    	    content.append(elem.text)

    fund_name = []
    morning_category = []
    morning_rating = []
    price = []
    expense = []

    chk = 0
    while chk < len(content):
    	fund_name.append(content[chk])
    	chk += 3
    chk = 1
    while chk< len(content):
    	morning_category.append(content[chk])
    	chk += 3
    chk = 2
    while chk<len(content):
    	morning_rating.append(content[chk])
    	chk += 3

    chk = 0
    while chk < len(b):
    	expense.append(b[chk].text)
    	chk += 2

    chk = 1
    while chk < len(b):
    	price.append(b[chk].text)
    	chk += 2

    print len(fund_name)
    print len(morning_category)
    print len(morning_rating)
    print len(price)
    print len(expense)

    pt = PrettyTable(field_names=['Fund Name', 'Morning Star Category', 'Morning Star rating', 'Latest price', 'Expense Ratio'])
    pt.align='l'
    [pt.add_row((fund_name[i], morning_category[i], morning_rating[i], price[i], expense[i]))
    for i in range(len(fund_name))]

    print pt

    c = driver.find_elements_by_class_name('ms_page_label')
    c[len(c)-2].click()
    time.sleep(8)
    main()

main()
