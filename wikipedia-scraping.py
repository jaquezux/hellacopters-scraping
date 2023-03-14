import pandas as pd
import requests
from bs4 import BeautifulSoup

# make the request
wikiurl = 'https://en.wikipedia.org/wiki/The_Hellacopters_discography#Singles'
table_class="wikitable plainrowheaders"
response = requests.get(wikiurl)

# parse data
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table', {'class':"wikitable"})

# read html
df = pd.read_html(str(indiatable))

# convert list to dataframe
df = pd.DataFrame(df[0])

df.to_csv(r'C:\Users\jaque\Projects\hellacopters-scrap\discography.csv', index=False, header=True)

print(df.head())

