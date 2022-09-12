import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# df_excel = pd.read_excel('creds-usecase.xlsx', index_col=0)
# print("Column headings:")
# print(df)
# print(df.columns)

# df = pd.read_excel('creds-usecase.xlsx')
# print(df['IP Address'][0])
# print(df['IP Address'][1])
# print(df['IP Address'][2])
# print(df['IP Address'][3])

# print(df['Username'][0])
# print(df['Password'][0])

# print(df['Username'][1])
# print(df['Password'][1])

# print(df['Username'][2])
# print(df['Password'][2])

# print(df['Username'][3])
# print(df['Password'][3])

# def cleansing(x):
#     df = pd.read_excel('creds-usecase.xlsx')

#     for column in df.columns:
#         df['Password'] = df['Username'].str.replace(r'\W',"")
#         # df['Password'] = df[column].str.replace(r'\W',"")
#         # df[column] = df[column].str.replace(r'\W',"")
#         # df[column] = df[column].str.replace(r'\W',"")

#     print(df['Password'][x])

df = pd.read_excel('creds-usecase.xlsx')
for column in df.columns:
    df['Password'] = df['Username'].str.replace(r'\W',"")
    # df['Password'] = df[column].str.replace(r'\W',"")
    # df[column] = df[column].str.replace(r'\W',"")
    # df[column] = df[column].str.replace(r'\W',"")
    
print(df)
df.to_excel("creds-cleansing.xlsx", index=False)