# with open('weather_data.csv', mode="r") as file:
#     content = file.readlines()
#     print(content)

# import csv
#
# with open('weather_data.csv') as file:
#     content = csv.reader(file)
#     print(content)
#     temperatures = []
#     for row in content:
#         temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# content = pandas.read_csv('weather_data.csv')
# # print(content[content.temp==content.temp.max()].day)
#
# monday= content[content.day == 'Monday']
# print((monday.temp*9/5)+32)


# Squirrel Project:
content = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260811.csv')
gray = content[content['Primary Fur Color'] == 'Gray']['Primary Fur Color'].count()
cinnamon = content[content['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].count()
black = content[content['Primary Fur Color'] == 'Black']['Primary Fur Color'].count()

# print(gray, cinnamon, black)

data = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, cinnamon, black]
}
dataframe = pandas.DataFrame(data)
print(dataframe)