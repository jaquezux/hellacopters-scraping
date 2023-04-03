# Scraping Hellacopters discography with Python ✨
In this project I used Python to scrape the discography of the band Hellacopters.

##
1) First of all, I searched for the Wikipedia page containing a table with a list of all albums relesed by the band.
These are the first 3 list items on Wikipedia:

![image](https://user-images.githubusercontent.com/97712990/229363434-aed20bb1-a640-466c-8a2e-69bbef0c8454.png)

2) I had to drop some columns that I wouldn't use. The columns are:
  - Peak chart positions (FIN, SWE, NOR)
  - Certifications

```python
import pandas as pd

df = pd.read_csv('discography.csv')

columns_to_drop = ["Certifications(sales thresholds)", 
           "Peak chart positions", 
           "Peak chart positions.1", 
           "Peak chart positions.2"]
df.drop(columns_to_drop, inplace=True, axis=1)
```
