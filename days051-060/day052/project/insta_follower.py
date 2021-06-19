import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstaFollower:
    def __init__(self, chromedriver_path):
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)

    def login(self, username, password):
        self.driver.get('https://www.instagram.com/accounts/login')
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(f'{password}{Keys.ENTER}')

        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')

    def find_follower(self, account):
        self.driver.get(f'https://www.instagram.com/{account}')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        buttons = self.driver.find_elements_by_css_selector('li button')
        for button in buttons:
            if button.text == 'Follow':
                button.click()
                time.sleep(1)

    def __del__(self):
        self.driver.quit()
