# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))   # DataFrame
# print(type(data["temp"]))   # Series (equivalent to column in a table)
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# avg = sum(temp_list)/ len(temp_list)
# print(avg)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition) # is same as print(data["condition"])
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# fahrenheit = monday_temp * (9/5) + 32
# print(fahrenheit)

# creating DataFrame from scratch
# data_dict = {
#     "students" : ["A","B","C"],
#     "scores" : [76,54,86]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250821.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_count)
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_count)
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_count)
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_count, cinnamon_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")