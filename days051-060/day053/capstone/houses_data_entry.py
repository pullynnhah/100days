import os
import time

import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

zillow_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22map' \
             'Bounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37' \
             '.681338202793995%2C%22north%22%3A37.8691254580163%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue' \
             '%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2' \
             'C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22ma' \
             'x%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr' \
             '%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22' \
             '%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22i' \
             'sListVisible%22%3Atrue%7D'
headers = {
    'USER-AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'ACCEPT-LANGUAGE': 'en-US,en;q=0.9,pt;q=0.8'
}
response = requests.get(zillow_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
links = [link['href'] if link['href'].startswith('https') else f'https://www.zillow.com{link["href"]}'
         for link in soup.select('.list-card-top a')]
addresses = [address.text.split('|')[-1] for address in soup.select('address')]
prices_per_month = [price.text.strip('/mo').split('+')[0] for price in soup.select('.list-card-price')]
houses = [
    {
        'link': link,
        'address': address,
        'price_per_month': price
    } for link, address, price in zip(links, addresses, prices_per_month)
    ]

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)

for house in houses:
    driver.get('https://forms.gle/dsWp1CkhmW5Na4XT8')
    time.sleep(2)
    address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(address_xpath).send_keys(house['address'])
    driver.find_element_by_xpath(price_xpath).send_keys(house['price_per_month'])
    driver.find_element_by_xpath(link_xpath).send_keys(house['link'])

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()

driver.quit()
