from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import json


class WebScraper:

    def __init__(self, username, password):
        self.logged_in_website = False
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def cc_login(self):
        scraping_url = json.load(open("config.json"))["scraping_url"]
        self.driver.get(scraping_url)
        sleep(1)

        username_field = self.driver.find_element(By.ID, "id_username")
        password_field = self.driver.find_element(By.ID, "id_password")
        login_button = self.driver.find_element(By.ID, "id_submit")

        username_field.send_keys(self.username)
        sleep(0.5)
        password_field.send_keys(self.password)
        login_button.click()

        sleep(1)
        self.driver.get(scraping_url)
        sleep(2)

        self.logged_in_website = True
