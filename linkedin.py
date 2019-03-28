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

for page in range(2, 3):
    search_url = 'https://www.linkedin.com/search/results/companies/?keywords=Marketing%20and%20Advertising&origin=GLOBAL_SEARCH_HEADER&page={}'.format(page)
    # search_url = str(search_url)
    browser.get(search_url)
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,'lxml')
    search_items = soup.find_all('li', class_='search-result__occluded-item')

    for item in search_items:
        try:
            company_url = item.find('a', class_='search-result__result-link')
            company_url = company_url['href']
            full_url = 'https://www.linkedin.com'+ company_url + 'about'
            browser.get(full_url)
            time.sleep(5)
            single_page_soup = BeautifulSoup(browser.page_source, 'lxml')
            location  = single_page_soup.find('div', class_="org-top-card-summary__info-item org-top-card-summary__headquarter").text
            company_name= single_page_soup.find('a', class_='company-name-link').text 

            company_website = single_page_soup.find('a', class_="link-without-visited-state")['href']

            print(location, company_name, company_website)
            break
        except TypeError:
            pass
    print('-'*100)
    break



    data.append(search_items)





