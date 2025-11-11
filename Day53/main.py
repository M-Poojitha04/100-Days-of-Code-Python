from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


google_form_link = "GOOGLE FORM LINK"
website_link = "https://appbrewery.github.io/Zillow-Clone/"
google_sheet_link = "https://docs.google.com/forms/"
response = requests.get(url=website_link)
zillow_webpage = response.text
soup = BeautifulSoup(zillow_webpage,"html.parser")

prices = soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
all_prices = [(price.getText()).split('/')[0].split(' ')[0].replace(',', '').replace('+', '') for price in prices]

links = soup.find_all(name="a", class_="property-card-link")
all_links = [link.get("href") for link in links]

addresses = soup.find_all(name="address")
all_addresses = [(address.getText()).replace('\n', '').replace('|', '').strip() for address in addresses]

class FillForm:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def filling_form(self):
        self.driver.get(google_form_link)

        for i in range(len(all_links)):
            sleep(1)
            address_fill = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_fill.send_keys(all_addresses[i])

            price_fill = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_fill.send_keys(all_prices[i])

            link_fill = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_fill.send_keys(all_links[i])

            submit = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()

            sleep(1)

            another_form = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_form.click()

    def get_sheet(self):
        self.driver.get(google_sheet_link)
        sleep(1)
        form = self.driver.find_element(By.XPATH, value='//*[@id=":3e"]/div[1]')
        form.click()
        sleep(1)
        responses = self.driver.find_element(By.XPATH, value='//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div')
        responses.click()
        sleep(1)
        link_to_sheet = self.driver.find_element(By.XPATH, value='//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]')
        link_to_sheet.click()
        sleep(1)
        create_sheet = self.driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/div[19]/div/div[2]/div[2]/div[3]/div[1]/span/span')
        create_sheet.click()

bot = FillForm()
bot.filling_form()
bot.get_sheet()