##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

PLACEHOLDER = "[NAME]"
data = pandas.read_csv("birthdays.csv")
dictionary = {key:value for (key,value) in data.items()}

current = dt.datetime.now()
day = current.day
month = current.month

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

for bday in range(len(dictionary) - 1) :
    if month == dictionary["month"][bday] and day == dictionary["day"][bday]:
        my_email = "python100doc.smtp@gmail.com"
        password = "rykc xwir atvs glza"

        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            content = letter.read()
            birthday_wish = content.replace(PLACEHOLDER,dictionary["name"][bday])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs=dictionary["email"][bday],
            msg=f"Subject:Birthday Wishes\n\n{birthday_wish}"
            )





