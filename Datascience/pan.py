import pandas as pd

# df = pd.read_csv("path")

#pandas series - it like a column in a table.it`s 1D holding any datatype`
#

# li = [2,3,4,5,6]

# s1 = pd.Series(li)

# print(s1)

# dict1 = {"one":1, "two":2}
# s2 = pd.Series(dict1)
# print(s2)


# Dataframe - 2d ds. uses loc attribute to return one or more specified row.

# data = {
#     "calories":[200,300,400],
#     "duration":[40,60,86]
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.loc[0])

df = pd.read_csv('countries.csv')

print(df.corr()) #.describe, info, std, min , 25%, max, corr,head - top 5