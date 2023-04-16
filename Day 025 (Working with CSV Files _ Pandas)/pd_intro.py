import pandas
# pandas is a software library written for the Python programming language for data manipulation and analysis.
# In particular, it offers data structures and operations for manipulating numerical tables and time series.
# It is free software released under the three-clause BSD license.
# This will make it easier to read data than the inbuilt csv or the readlines() function in files
import pandas as pd

data = pandas.read_csv('weather_data.csv')
print(type(data))
print(data)
print(data['temp'])
print(type(data['temp']))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)
print("The mean Temeperature is: " , data['temp'].mean())
print("The Maximum Temeperature is: " , data['temp'].max())
print("The Minimum Temeperature is: " , data['temp'].min())
print("The Most commom Temeperature value is: ", data['temp'].mode())

# Getting rows
print(data[data.day == 'Monday'])
print(data[data['day'] == 'Monday'])

# getting thr row with maximum value
print(data[data.temp == data.temp.max()])

# Challenge: Get temperature for Monday and convert it into F
monday = data[data.day == 'Monday']
monday_temp = monday.temp
monday_temp_F = monday_temp * 9/5 + 32
print('The temperature for Monday in F: ', monday_temp_F)

# How you create a DF from scratch
students = {
    "students":['Amy', 'James', 'Angela'],
    "Scores":[76, 56, 65]
}
students_df = pd.DataFrame(students)
print(students_df)
students_df.to_csv('Students.csv')