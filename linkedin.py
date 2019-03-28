from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
import time
import csv
from bs4 import BeautifulSoup
data = []


chrome_options = Options()
# chrome_options.add_argument("--headless")

browser = webdriver.Chrome(chrome_options= chrome_options)

browser.get('https://www.linkedin.com/')
time.sleep(2)


email = browser.find_element_by_xpath('//*[@id="login-email"]')
password = browser.find_element_by_xpath('//*[@id="login-password"]')
submit = browser.find_element_by_xpath('//*[@id="login-submit"]')

email.send_keys('ratan01828@gmail.com')
password.send_keys('(P@ssFast123^!)_')
submit.click()
time.sleep(2)

# search_url = 'https://www.linkedin.com/search/results/companies/?keywords=Marketing%20and%20Advertising&origin=GLOBAL_SEARCH_HEADER&page={}'.format(i)

for page in range(1, 10):
    search_url = 'https://www.linkedin.com/search/results/companies/?keywords=Marketing%20and%20Advertising&origin=GLOBAL_SEARCH_HEADER&page={}'.format(page)
    # search_url = str(search_url)
    browser.get(search_url)
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,'lxml')
    search_items = soup.find_all('li', class_='search-result__occluded-item')
    
    data.append(search_items)





