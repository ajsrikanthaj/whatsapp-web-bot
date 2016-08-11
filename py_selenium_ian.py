#https://www.github.com/iamnosa
#Let's import the Selenium package
from selenium import webdriver

#Let's use Firefox as our browser
web = webdriver.Firefox()
web.get('http://web.whatsapp.com')
input()

#Replace Mr Kelvin with the name of your friend to spam
elem = web.find_element_by_xpath('//span[contains(text(),"Mr Kelvin")]')
elem.click()
elem1 = web.find_elements_by_class_name('input')
while True:
	elem1[1].send_keys('hahahahahahaha')
	web.find_element_by_class_name('send-container').click()
