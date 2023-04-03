import pandas as pd

# read the csv file
df = pd.read_csv('discography.csv')

# creating a variable to define which columns to drop
columns_to_drop = ["Certifications(sales thresholds)", 
           "Peak chart positions", 
           "Peak chart positions.1", 
           "Peak chart positions.2"]
df.drop(columns_to_drop, inplace=True, axis=1) # drop the columns
df.drop(index=df.index[0], axis=0, inplace=True) # drop the first row, because it is duplicated

df.columns = ['year', 'album'] # rename columns to avoid labels with blank spaces
df[['album','details']] = df['album'].str.split(' Released',expand=True) # split album column to 2 columns (new column will receive the details content)
df.drop('details', inplace=True, axis=1) # delete the column 'details' because I will not use it

# saving as xlsx file
datatoexcel = pd.ExcelWriter('Hellacopters-discography.xlsx')
df.to_excel(datatoexcel)
datatoexcel.save()

print(df)
