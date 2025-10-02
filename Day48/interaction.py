from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# Click the link
num = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# num.click()

# Click the link using LINK_TEXT
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Search the webpage
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)


driver.quit()