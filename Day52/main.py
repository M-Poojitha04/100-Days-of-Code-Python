from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
load_dotenv()
SIMILAR_ACCOUNT = os.environ.get("SIMILAR_ACCOUNT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(6)
        username = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        login_button = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[3]')

        username.click()
        username.send_keys(os.environ.get("USERNAME"))
        password.click()
        password.send_keys(os.environ.get("PASSWORD"))
        login_button.click()
        sleep(6)
    #     after login: pop-up asks for saving login information
        not_now = self.driver.find_element(By.XPATH,value='//*[@id="mount_0_0_PM"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div')
        not_now.click()


    def find_followers(self):
        sleep(10)
        self.driver.get(f"https://www.instagram.com/{os.environ.get("SIMILAR_ACCOUNT")}/followers")

        sleep(10)
        modal_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()