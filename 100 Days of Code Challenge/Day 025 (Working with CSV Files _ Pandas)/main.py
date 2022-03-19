import csv
# with open('weather_data.csv', 'r') as data:
#     data = data.readlines()
#
# print(data)

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    # for row in data:
    #     print(row)

    temperature = []
    for row in data:
        if row[1] != 'temp':
            temp = int(row[1])
            temperature.append(temp)
    print(temperature)

