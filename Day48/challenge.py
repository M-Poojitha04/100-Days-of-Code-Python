from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value="fName")
fname.click()
fname.send_keys("asdf")

lname = driver.find_element(By.NAME, value="lName")
lname.click()
lname.send_keys("lkjh")

mail = driver.find_element(By.NAME, value="email")
mail.click()
mail.send_keys("abc@123.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

driver.quit()