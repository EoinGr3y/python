from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.rte.ie/')
sportElem = browser.find_element_by_css_selector('.sport-nav-item')
sportElem.click()

searchElem = browser.find_element_by_css_selector('#searchterm')
searchElem.send_keys('rugby')
searchElem.submit()