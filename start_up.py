from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass

def openGmail(browser):
	browser.get('https://gmail.com')
	usernameElem = browser.find_element_by_name('identifier')
	usernameElem.send_keys('eoin.g08@gmail.com')

	nextButton = browser.find_element_by_css_selector('#identifierNext > content:nth-child(3) > span:nth-child(1)')
	nextButton.click()
	time.sleep(1)
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

	passwordElem = browser.find_element_by_name('password')
	password = getpass.getpass('Gmail password:')
	passwordElem.send_keys(password)

	passwordNextButton = browser.find_element_by_css_selector('#passwordNext > content:nth-child(3) > span:nth-child(1)')
	passwordNextButton.click()

def openUdemy(browser):
	browser.execute_script("window.open('about:blank', 'tab2');")
	browser.switch_to.window("tab2")
	browser.get('https://www.udemy.com/')

	logInButton = browser.find_element_by_css_selector('div.dropdown:nth-child(4) > require-auth:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
	logInButton.click()
	time.sleep(1)

	emailElem = browser.find_element_by_name('email')
	emailElem.send_keys('eoin.g08@gmail.com')

	passwordElem = browser.find_element_by_name('password')
	password = getpass.getpass('Udemy password:')
	passwordElem.send_keys(password)

	submitElem = browser.find_element_by_name('submit')
	submitElem.click()


browser = webdriver.Firefox()
openGmail(browser)
openUdemy(browser)