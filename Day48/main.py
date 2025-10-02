from selenium import webdriver
from selenium.webdriver.common.by import By

# To keep the chrome browser open after program finishes we use ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

# Day 47 with Selenium:
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")


driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="success-story-1301"]/table/tbody/tr/td/p/a')
# print(bug_link.text)

# Challenge 1
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
time_of_events = []
for time in event_times:
   time_of_events.append(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")
name_of_events = []
for event in event_names:
   name_of_events.append(event.text)

events = { }

for n in range(len(time_of_events)):
    events[n] = {
        "time": time_of_events[n],
        "name": name_of_events[n]
    }

print(events)

# driver.close()  # Closes the active tab
driver.quit()  # Closes all tabs


