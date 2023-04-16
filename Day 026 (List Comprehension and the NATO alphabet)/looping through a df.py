import pandas as pd
# How to iterate over a pd df

student_dict = {
    "student": ['Chris', 'Adams', 'Mercy', 'Lydia'],
    "scores":[99, 88, 77, 66]
}

# for (key, value) in student_dict.items():
#     print(value)
#
student_df = pd.DataFrame(student_dict)
# print(student_df)

# loop through a DF
# for (key, value) in student_df.items():
#     print(key, value)

# Loop through rows of a DF
# for (index, row) in student_df.iterrows():
#     print(row)
#
# for (index, row) in student_df.iterrows():
#     print(row.scores)

for (index, row) in student_df.iterrows():
    if row.student == 'Chris':
        print(row.scores)
        print(row.student)