import pandas as pd
squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(squirrel_data.head())
# print(squirrel_data.columns)
squirrel_color = squirrel_data['Primary Fur Color']
# print(squirrel_color)
# print(squirrel_color.unique())
# print(squirrel_color.isnull().sum())
squirrel_color_list = squirrel_color.to_list()
# print(squirrel_color_list)

red_squirrels = 0
grey_squirrels = 0
black_squirrels = 0
no_color = 0

for color in squirrel_color_list:
    if color == 'Black':
        black_squirrels += 1
    if color == 'Cinnamon':
        red_squirrels += 1
    if color == 'Gray':
        grey_squirrels += 1
    else:
        no_color += 1

squrrels_fur_color = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count":[grey_squirrels, red_squirrels, black_squirrels]
}
df_fur_color = pd.DataFrame(squrrels_fur_color)
print(df_fur_color)

# ######## ALTERNATIVE APPROACH
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_ones = len(data[data["Primary Fur Color"] == 'Gray'])
black_ones = len(data[data["Primary Fur Color"] == 'Black'])
red_ones = len(data[data["Primary Fur Color"] == 'Cinnamon'])

print('Gray', gray_ones)
print('red', red_ones)
print('black', black_ones)

fur_colr = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count": [gray_ones, red_ones, black_ones]
}

fur_col_df = pd.DataFrame(fur_colr)
fur_col_df.to_csv('Squirrel by Color.csv')
