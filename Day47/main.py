from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
header = {
"Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
}
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=header)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")
price_whole = soup.find(name="span", class_="aok-offscreen").getText()
price = float(price_whole.split("$")[1].split()[0])
target_price = 100.00
name_of_product = soup.find(id="productTitle").getText().split(",")[0].strip(" ")

if price < target_price:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], 587) as connection:
        connection.starttls()  # secure the connection
        connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{name_of_product} is now {price}"
        )
    print("Sent the mail!")

