# import smtplib
#
# my_email = "python100doc.smtp@gmail.com"
# password = "rykc xwir atvs glza"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="python.practicemail@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )

# import datetime as dt
#
# current_datetime = dt.datetime.now()
# year = current_datetime.year
# month = current_datetime.month
# day_of_week = current_datetime.weekday()
# print(current_datetime)
# print(year)
# print(month)
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2004, month=7, day=30, hour=5)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

current_datetime = dt.datetime.now()
week = current_datetime.weekday()

if week == 0:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()

    my_email = "python100doc.smtp@gmail.com"
    password = "rykc xwir atvs glza"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="python.practicemail@yahoo.com",
            msg=f"Subject:Monday Motivation!!\n\n{random.choice(quotes)}"
        )