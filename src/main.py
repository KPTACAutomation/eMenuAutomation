import pandas as pd

df = pd.read_excel('menu/menu.xlsx',engine='openpyxl')

#to csv
df.to_csv('menu/menu.csv',index=False)