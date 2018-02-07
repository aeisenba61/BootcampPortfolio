import pandas as pd

df = pd.read_csv("weather.csv")

df = df.drop(['Unnamed: 0','Date'], axis =1)
#print(df.head())
print(df.to_html(index=False))