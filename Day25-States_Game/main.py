# wheather_list = []

# with open("weather_data.csv") as data:
#     data_lines = data.readlines()
#     for line in data_lines:
#         wheather_list.append(line.replace("\n", "").split(","))
# print(wheather_list)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for temp in data:
#         if temp[1] != "temp":
#             temperatures.append(int(temp[1]))
#     print(temperatures)

# import pandas

# # data = pandas.read_csv("weather_data.csv")
# # # print(data['temp'])

# # data_dict = data.to_dict()
# # #print(data_dict)

# # temp_list = data["temp"].to_list()
# # #print(temp_list)

# # avg_temp = sum(temp_list)/len(temp_list)
# # print(avg_temp)
# # print(data["temp"].mean())
# # print(data["temp"].max())

# # print(data["condition"])

# # print(data[data["day"] == "Monday"])
# # print(data[data["temp"] == data["temp"].max()])

# # monday = data[data['day'] == "Monday"]
# # monday_temp = int(monday.temp)
# # print(monday_temp * 9/5 +32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")