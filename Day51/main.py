from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep,time

PROMISED_DOWN = 150
PROMISED_UP = 10
# CHROME_DRIVER_PATH = "C:\Users\pooji\.cache\selenium\chromedriver\win64\141.0.7390.78\chromedriver.exe"
X_EMAIL = ""
X_PASSWORD = ""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")


        sleep(5)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        sleep(50)
        self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')


    def tweet_at_provider(self):
        self.driver.get("https://www.x.com")
        sleep(7)

        sign_in = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div/span/span')
        sign_in.click()
        sleep(3)
        x_mail = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        x_mail.click()
        x_mail.send_keys(X_EMAIL)
        sleep(3)
        next_btn = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_btn.click()
        sleep(3)
        userid = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        userid.send_keys("")

        next = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        next.click()
        enter_password = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_password.click()
        enter_password.send_keys(X_PASSWORD)
        sleep(3)
        enter_btn = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        enter_btn.click()
        sleep(3)
        post_btn = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
        post_btn.click()
        sleep(3)
        post = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
        post.click()
        my_post = f"Hey Internet provider!, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? "
        post.send_keys(my_post)
        sleep(3)
        send_post = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button/div/span/span')
        send_post.click()
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
