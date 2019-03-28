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

email.send_keys('mithun.tutorial.one@gmail.com')
password.send_keys('mithun.tutorial.one')
submit.click()
time.sleep(2)

# search_url = 'https://www.linkedin.com/search/results/companies/?keywords=Marketing%20and%20Advertising&origin=GLOBAL_SEARCH_HEADER&page={}'.format(i)

for page in range(1, 3):
    print('Page Number {} processing.....'.format(page))
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
            time.sleep(2)
            single_page_soup = BeautifulSoup(browser.page_source, 'lxml')
            try:
                location  = single_page_soup.find('div', class_="org-top-card-summary__info-item org-top-card-summary__headquarter").text.strip()
                company_name= single_page_soup.find('h1', class_='org-top-card-summary__title')['title'].strip()
                company_website = single_page_soup.find('span', class_="link-without-visited-state").text.strip()
                category = single_page_soup.find('div', class_="org-top-card-summary__industry").text.strip()
                company={'name':company_name, 'category':category, 'website': company_website, 'location': location}
                data.append(company)
            except AttributeError:
                pass
        except TypeError:
            pass
    print('Page Number {} Completed'.format(page))


def write_csv(data, filename="file2.csv"):
    with open(filename, 'w', newline='') as csvfile:
        f = csv.writer(csvfile)
        for line in data:
            f.writerow([line['name'], line['category'], line['location'], line['website']])
write_csv(data)





