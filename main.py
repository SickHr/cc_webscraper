from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

scraping_url = "https://de.clubcooee.com/market/itemListings/2"

login_username = "Oxygen-"
login_password = "D996b1c8f"

market_refresh = 30



class WebScraper:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(scraping_url)
        sleep(1)

        username_button = self.driver.find_element(By.ID, "id_username")
        password_button = self.driver.find_element(By.ID, "id_password")
        login_button = self.driver.find_element(By.ID, "id_submit")

        username_button.send_keys(login_username)
        sleep(0.5)
        password_button.send_keys(login_password)
        login_button.click()

        sleep(1)
        self.driver.get(scraping_url)
        sleep(2)

    def scrape(self, seconds):
        refresh = True

        while refresh:

            trade_list = self.driver.find_element(By.CSS_SELECTOR, "#main-content > div:nth-child(5) > div")

            items = trade_list.find_elements(By.XPATH, '//*[@id="trade-list"]/li/div')

            for item in items:
                category = item.find_element(By.CLASS_NAME, "font-m").text
                name = item.find_element(By.CLASS_NAME, "font-xl").text
                price = item.find_element(By.XPATH, ".//div[@class='col xs50 m20 l15']/div[@class='font-xl']").text


                buy_button = item.find_element(By.CSS_SELECTOR, "div[data-actionlink]")
                buy_link = buy_button.get_attribute("data-actionlink")


                print("category: " + category)
                print("name: " + name)
                print("price: " + price)
                print("buy link: " + buy_link)
                print("- - - -")

            sleep(seconds)
            self.driver.refresh()


if __name__ == "__main__":
    scraper = WebScraper()
    scraper.login()
    scraper.scrape(market_refresh)
