# from cleansing import *

# cleansing(0)

import pandas as pd

df = pd.read_excel('creds-cleansing.xlsx')
print(df['IP Address'][0])
print(df['IP Address'][1])
print(df['IP Address'][2])
print(df['IP Address'][3])

print("----------------------------------------")

print(df['Username'][0])
print(df['Password'][0])

print("----------------------------------------")

print(df['Username'][1])
print(df['Password'][1])

print("----------------------------------------")

print(df['Username'][2])
print(df['Password'][2])

print("----------------------------------------")

print(df['Username'][3])
print(df['Password'][3])