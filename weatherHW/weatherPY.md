
# Weather Homework - Aaron Eisenbarth

## Analysis
Observable Trend 1: The Max temperature versus Latitude graph displays the overall trend of getting warmer the closer you are to the equator. That being said on the negative latitudes (i.e. south of the equator) I had less matches and  no data beyond -50, which would have helped make this conclusion. I think subsequent analysis would benefit from normalizing these max temperatures with data elements like elevation.  Observable Trend 2: The Humidity and Cloudiness graphs appeared nearly random suggesting that no significant relationship with respect to Latitude exists. Whereas the Wind Speed versus Latitude graph displays a slight relationship with latitude as there is a faint bell curve represented in the scatterplotObservable Trend 3: The analysis would benefit from looking at average annual temperatures rather than a point in time. It would give more validity to trend analysis.  

```python
import pandas as pd 
import requests as req
import numpy as np 
import json 
from citipy import citipy
import random
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import time
```


```python
lat = []
lon = []
for x in range(500):
    lat.append(random.uniform(-90,0))
    lon.append(random.uniform(-180,0))
for x in range(500):
    lat.append(random.uniform(0,90))
    lon.append(random.uniform(0,180))
```


```python
df = pd.DataFrame(
    {'lat': lat,
     'lon': lon,
    })
```


```python
cities = []
countries = []
city_names = []
for index, row in df.iterrows():
    cities.append(citipy.nearest_city(row['lat'], row['lon']))
for city in cities:
    countries.append(city.country_code)
    city_names.append(city.city_name)
city_country = pd.DataFrame({
    'city_name': city_names,
    'country':countries})
city_country.head(1)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city_name</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>georgetown</td>
      <td>sh</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_counter = city_country.drop_duplicates(subset = city_country[['city_name', 'country']])
len(city_counter)
```




    409




```python
lat2 = []
lon2 = []
if len(city_counter) < 500:
    for x in range(500):
        lat2.append(random.uniform(-90,0))
        lon2.append(random.uniform(-180,0))
    for x in range(500):
        lat2.append(random.uniform(0,90))
        lon2.append(random.uniform(0,180))
display(len(lat2))
display(len(lon2))
```


    1000



    1000



```python
df2 = pd.DataFrame(
    {'lat': lat2,
     'lon': lon2,
    })
display(len(df2))
```


    1000



```python
cities2 = []
countries2 = []
city_names2 = []
for index, row in df2.iterrows():
    cities2.append(citipy.nearest_city(row['lat'], row['lon']))
for city in cities2:
    countries2.append(city.country_code)
    city_names2.append(city.city_name)
city_country2 = pd.DataFrame({
    'city_name': city_names2,
    'country':countries2})
len(city_country2['city_name'])
```




    1000




```python
city_counter2 = city_country2.drop_duplicates(subset = city_country2[['city_name', 'country']])
len(city_counter2)
```




    424




```python
frames = [city_country,city_country2]
combined = pd.concat(frames)
readydf = combined.drop_duplicates(subset = combined[['city_name', 'country']])
display(len(readydf))
readydf.head()
```


    709





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city_name</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>georgetown</td>
      <td>sh</td>
    </tr>
    <tr>
      <th>1</th>
      <td>rikitea</td>
      <td>pf</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rio gallegos</td>
      <td>ar</td>
    </tr>
    <tr>
      <th>3</th>
      <td>mataura</td>
      <td>pf</td>
    </tr>
    <tr>
      <th>4</th>
      <td>jamestown</td>
      <td>sh</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Save config information.
api_key = "6842f8457dd8a6b32eaaad7d97b25fed"
endpoint = "http://api.openweathermap.org/data/2.5/weather"
units = "Imperial"

# Build partial query URL
params = {
    'appid': api_key,
    'units': units
}
```

## Perform Waves of API Calls


```python
record = 0 
set = 1
x=0
for record in range(len(readydf['city_name'])):
    for index, row in readydf.iloc[x:x+60,:].iterrows():
        target_url = "http://api.openweathermap.org/data/2.5/weather?appid=%s&q=%s,%s" % (api_key, row['city_name'],row['country'])
        response = req.get(target_url, params=params).json()
        if response.get('cod') != '404':
            readydf.set_value(index,'Latitude',response.get("coord").get("lat"))
            readydf.set_value(index,'Max Temperature', response.get("main").get("temp_max"))
            readydf.set_value(index,'Humidity', response.get("main").get("humidity"))
            readydf.set_value(index,'Wind Speed (mph)',response.get("wind").get("speed"))
            readydf.set_value(index,'Cloudiness %', response.get("clouds").get("all"))
            readydf.set_value(index,'Date', datetime.datetime.now().strftime("%Y-%m-%d"))
            record += 1
            x += 1
            print("Processing Record " + str(record) + " of Set " + str(set) +" | " + row['city_name'] + ' ' + str(x)) 
            print(target_url)
    time.sleep(60)
    record = 0
    set = set + 1
```

    C:\Users\aeise\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\indexing.py:337: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      self.obj[key] = _infer_fill_value(value)
    C:\Users\aeise\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\indexing.py:517: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      self.obj[item] = s
    

    Processing Record 1 of Set 1 | georgetown 1
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=georgetown,sh
    Processing Record 2 of Set 1 | rikitea 2
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rikitea,pf
    Processing Record 3 of Set 1 | rio gallegos 3
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rio gallegos,ar
    Processing Record 4 of Set 1 | jamestown 4
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jamestown,sh
    Processing Record 5 of Set 1 | ushuaia 5
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ushuaia,ar
    Processing Record 6 of Set 1 | hermanus 6
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hermanus,za
    Processing Record 7 of Set 1 | inhapim 7
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=inhapim,br
    Processing Record 8 of Set 1 | cape town 8
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cape town,za
    Processing Record 9 of Set 1 | treinta y tres 9
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=treinta y tres,uy
    Processing Record 10 of Set 1 | cidreira 10
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cidreira,br
    Processing Record 11 of Set 1 | avarua 11
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=avarua,ck
    Processing Record 12 of Set 1 | chuy 12
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=chuy,uy
    Processing Record 13 of Set 1 | contamana 13
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=contamana,pe
    Processing Record 14 of Set 1 | atuona 14
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=atuona,pf
    Processing Record 15 of Set 1 | chapeco 15
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=chapeco,br
    Processing Record 16 of Set 1 | ancud 16
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ancud,cl
    Processing Record 17 of Set 1 | cordoba 17
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cordoba,ar
    Processing Record 18 of Set 1 | punta arenas 18
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=punta arenas,cl
    Processing Record 19 of Set 1 | constitucion 19
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=constitucion,cl
    Processing Record 20 of Set 1 | lebu 20
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lebu,cl
    Processing Record 21 of Set 1 | sao joao da barra 21
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sao joao da barra,br
    Processing Record 22 of Set 1 | mar del plata 22
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mar del plata,ar
    Processing Record 23 of Set 1 | vaini 23
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vaini,to
    Processing Record 24 of Set 1 | urucara 24
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=urucara,br
    Processing Record 25 of Set 1 | puerto narino 25
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=puerto narino,co
    Processing Record 26 of Set 1 | castro 26
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=castro,cl
    Processing Record 27 of Set 1 | laguna 27
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=laguna,br
    Processing Record 28 of Set 1 | caravelas 28
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=caravelas,br
    Processing Record 29 of Set 1 | belmonte 29
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=belmonte,br
    Processing Record 30 of Set 1 | san luis 30
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san luis,ar
    Processing Record 31 of Set 1 | ariquemes 31
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ariquemes,br
    Processing Record 32 of Set 1 | manaus 32
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=manaus,br
    Processing Record 33 of Set 1 | faanui 33
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=faanui,pf
    Processing Record 34 of Set 1 | arraial do cabo 34
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=arraial do cabo,br
    Processing Record 35 of Set 1 | santiago de cao 35
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=santiago de cao,pe
    Processing Record 36 of Set 1 | coihaique 36
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=coihaique,cl
    Processing Record 37 of Set 1 | harper 37
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=harper,lr
    Processing Record 38 of Set 1 | punta alta 38
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=punta alta,ar
    Processing Record 39 of Set 1 | puerto ayora 39
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=puerto ayora,ec
    Processing Record 40 of Set 1 | saldanha 40
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=saldanha,za
    Processing Record 41 of Set 1 | puerto maldonado 41
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=puerto maldonado,pe
    Processing Record 42 of Set 1 | itaituba 42
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=itaituba,br
    Processing Record 43 of Set 1 | maragogi 43
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=maragogi,br
    Processing Record 44 of Set 1 | huarmey 44
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=huarmey,pe
    Processing Record 45 of Set 1 | uberlandia 45
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=uberlandia,br
    Processing Record 46 of Set 1 | maraa 46
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=maraa,br
    Processing Record 47 of Set 1 | pucara 47
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pucara,pe
    Processing Record 48 of Set 1 | pauini 48
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pauini,br
    Processing Record 49 of Set 1 | montes claros 49
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=montes claros,br
    Processing Record 50 of Set 1 | viedma 50
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=viedma,ar
    Processing Record 51 of Set 1 | neuquen 51
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=neuquen,ar
    Processing Record 52 of Set 1 | leticia 52
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=leticia,co
    Processing Record 53 of Set 1 | filadelfia 53
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=filadelfia,py
    Processing Record 2 of Set 2 | pucara 54
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pucara,pe
    Processing Record 3 of Set 2 | pauini 55
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pauini,br
    Processing Record 4 of Set 2 | montes claros 56
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=montes claros,br
    Processing Record 5 of Set 2 | viedma 57
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=viedma,ar
    Processing Record 6 of Set 2 | neuquen 58
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=neuquen,ar
    Processing Record 7 of Set 2 | leticia 59
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=leticia,co
    Processing Record 8 of Set 2 | filadelfia 60
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=filadelfia,py
    Processing Record 9 of Set 2 | san ramon 61
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san ramon,bo
    Processing Record 10 of Set 2 | canutama 62
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=canutama,br
    Processing Record 11 of Set 2 | taltal 63
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=taltal,cl
    Processing Record 12 of Set 2 | abaete 64
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=abaete,br
    Processing Record 13 of Set 2 | tarauaca 65
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tarauaca,br
    Processing Record 14 of Set 2 | porto da folha 66
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=porto da folha,br
    Processing Record 15 of Set 2 | cassilandia 67
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cassilandia,br
    Processing Record 16 of Set 2 | guapimirim 68
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=guapimirim,br
    Processing Record 17 of Set 2 | paranaiba 69
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=paranaiba,br
    Processing Record 18 of Set 2 | tocopilla 70
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tocopilla,cl
    Processing Record 19 of Set 2 | rafaela 71
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rafaela,ar
    Processing Record 20 of Set 2 | san juan 72
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san juan,ar
    Processing Record 21 of Set 2 | paramonga 73
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=paramonga,pe
    Processing Record 22 of Set 2 | minas novas 74
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=minas novas,br
    Processing Record 23 of Set 2 | rawson 75
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rawson,ar
    Processing Record 24 of Set 2 | tiarei 76
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tiarei,pf
    Processing Record 25 of Set 2 | bujaru 77
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bujaru,br
    Processing Record 26 of Set 2 | uaua 78
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=uaua,br
    Processing Record 27 of Set 2 | calbuco 79
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=calbuco,cl
    Processing Record 28 of Set 2 | san cristobal 80
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san cristobal,ec
    Processing Record 29 of Set 2 | alofi 81
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=alofi,nu
    Processing Record 30 of Set 2 | pisco 82
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pisco,pe
    Processing Record 31 of Set 2 | manicore 83
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=manicore,br
    Processing Record 32 of Set 2 | iberia 84
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=iberia,pe
    Processing Record 33 of Set 2 | cuiaba 85
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cuiaba,br
    Processing Record 34 of Set 2 | rio grande 86
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rio grande,br
    Processing Record 35 of Set 2 | tautira 87
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tautira,pf
    Processing Record 36 of Set 2 | barcelos 88
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=barcelos,br
    Processing Record 37 of Set 2 | pontes e lacerda 89
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pontes e lacerda,br
    Processing Record 38 of Set 2 | hualmay 90
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hualmay,pe
    Processing Record 39 of Set 2 | santarem 91
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=santarem,br
    Processing Record 40 of Set 2 | coquimbo 92
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=coquimbo,cl
    Processing Record 41 of Set 2 | general roca 93
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=general roca,ar
    Processing Record 42 of Set 2 | ixtapa 94
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ixtapa,mx
    Processing Record 43 of Set 2 | necochea 95
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=necochea,ar
    Processing Record 44 of Set 2 | alta floresta 96
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=alta floresta,br
    Processing Record 45 of Set 2 | villa maria 97
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=villa maria,ar
    Processing Record 46 of Set 2 | coracao de jesus 98
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=coracao de jesus,br
    Processing Record 47 of Set 2 | urubicha 99
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=urubicha,bo
    Processing Record 48 of Set 2 | pimentel 100
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pimentel,pe
    Processing Record 49 of Set 2 | aripuana 101
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aripuana,br
    Processing Record 50 of Set 2 | doka 102
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=doka,sd
    Processing Record 51 of Set 2 | bilma 103
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bilma,ne
    Processing Record 52 of Set 2 | mecca 104
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mecca,sa
    Processing Record 53 of Set 2 | evensk 105
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=evensk,ru
    Processing Record 54 of Set 2 | almaznyy 106
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=almaznyy,ru
    Processing Record 3 of Set 3 | doka 107
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=doka,sd
    Processing Record 4 of Set 3 | bilma 108
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bilma,ne
    Processing Record 5 of Set 3 | mecca 109
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mecca,sa
    Processing Record 6 of Set 3 | evensk 110
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=evensk,ru
    Processing Record 7 of Set 3 | almaznyy 111
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=almaznyy,ru
    Processing Record 8 of Set 3 | orlik 112
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=orlik,ru
    Processing Record 9 of Set 3 | dikson 113
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dikson,ru
    Processing Record 10 of Set 3 | butaritari 114
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=butaritari,ki
    Processing Record 11 of Set 3 | pastavy 115
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pastavy,by
    Processing Record 12 of Set 3 | sarangani 116
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sarangani,ph
    Processing Record 13 of Set 3 | kysyl-syr 117
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kysyl-syr,ru
    Processing Record 14 of Set 3 | fiche 118
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=fiche,et
    Processing Record 15 of Set 3 | ouesso 119
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ouesso,cg
    Processing Record 16 of Set 3 | islamkot 120
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=islamkot,pk
    Processing Record 17 of Set 3 | pevek 121
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pevek,ru
    Processing Record 18 of Set 3 | severo-kurilsk 122
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=severo-kurilsk,ru
    Processing Record 19 of Set 3 | hithadhoo 123
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hithadhoo,mv
    Processing Record 20 of Set 3 | cherskiy 124
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cherskiy,ru
    Processing Record 21 of Set 3 | guilin 125
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=guilin,cn
    Processing Record 22 of Set 3 | saskylakh 126
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=saskylakh,ru
    Processing Record 23 of Set 3 | oksfjord 127
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=oksfjord,no
    Processing Record 24 of Set 3 | banda aceh 128
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=banda aceh,id
    Processing Record 25 of Set 3 | vardo 129
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vardo,no
    Processing Record 26 of Set 3 | sinop 130
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sinop,tr
    Processing Record 27 of Set 3 | yeniseysk 131
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=yeniseysk,ru
    Processing Record 28 of Set 3 | katsuura 132
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=katsuura,jp
    Processing Record 29 of Set 3 | druzhba 133
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=druzhba,ua
    Processing Record 30 of Set 3 | melito di porto salvo 134
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=melito di porto salvo,it
    Processing Record 31 of Set 3 | arman 135
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=arman,ru
    Processing Record 32 of Set 3 | hirara 136
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hirara,jp
    Processing Record 33 of Set 3 | carlagan 137
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=carlagan,ph
    Processing Record 34 of Set 3 | zavodoukovsk 138
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zavodoukovsk,ru
    Processing Record 35 of Set 3 | adrar 139
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=adrar,dz
    Processing Record 36 of Set 3 | tazovskiy 140
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tazovskiy,ru
    Processing Record 37 of Set 3 | zilupe 141
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zilupe,lv
    Processing Record 38 of Set 3 | baruun-urt 142
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=baruun-urt,mn
    Processing Record 39 of Set 3 | sur 143
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sur,om
    Processing Record 40 of Set 3 | khatanga 144
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=khatanga,ru
    Processing Record 41 of Set 3 | dicabisagan 145
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dicabisagan,ph
    Processing Record 42 of Set 3 | barentu 146
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=barentu,er
    Processing Record 43 of Set 3 | port blair 147
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=port blair,in
    Processing Record 44 of Set 3 | veraval 148
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=veraval,in
    Processing Record 45 of Set 3 | san isidro 149
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san isidro,ph
    Processing Record 46 of Set 3 | sfantu gheorghe 150
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sfantu gheorghe,ro
    Processing Record 47 of Set 3 | hohhot 151
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hohhot,cn
    Processing Record 4 of Set 4 | adrar 152
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=adrar,dz
    Processing Record 5 of Set 4 | tazovskiy 153
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tazovskiy,ru
    Processing Record 6 of Set 4 | zilupe 154
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zilupe,lv
    Processing Record 7 of Set 4 | baruun-urt 155
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=baruun-urt,mn
    Processing Record 8 of Set 4 | sur 156
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sur,om
    Processing Record 9 of Set 4 | khatanga 157
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=khatanga,ru
    Processing Record 10 of Set 4 | dicabisagan 158
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dicabisagan,ph
    Processing Record 11 of Set 4 | barentu 159
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=barentu,er
    Processing Record 12 of Set 4 | port blair 160
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=port blair,in
    Processing Record 13 of Set 4 | veraval 161
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=veraval,in
    Processing Record 14 of Set 4 | san isidro 162
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san isidro,ph
    Processing Record 15 of Set 4 | sfantu gheorghe 163
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sfantu gheorghe,ro
    Processing Record 16 of Set 4 | hohhot 164
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hohhot,cn
    Processing Record 17 of Set 4 | piploda 165
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=piploda,in
    Processing Record 18 of Set 4 | moussoro 166
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=moussoro,td
    Processing Record 19 of Set 4 | ulaanbaatar 167
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ulaanbaatar,mn
    Processing Record 20 of Set 4 | mehamn 168
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mehamn,no
    Processing Record 21 of Set 4 | yar-sale 169
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=yar-sale,ru
    Processing Record 22 of Set 4 | tessalit 170
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tessalit,ml
    Processing Record 23 of Set 4 | jumla 171
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jumla,np
    Processing Record 24 of Set 4 | chokurdakh 172
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=chokurdakh,ru
    Processing Record 25 of Set 4 | sakaiminato 173
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sakaiminato,jp
    Processing Record 26 of Set 4 | nikologory 174
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nikologory,ru
    Processing Record 27 of Set 4 | bandarbeyla 175
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bandarbeyla,so
    Processing Record 28 of Set 4 | tiksi 176
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tiksi,ru
    Processing Record 29 of Set 4 | suluq 177
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=suluq,ly
    Processing Record 30 of Set 4 | livny 178
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=livny,ru
    Processing Record 31 of Set 4 | wanning 179
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=wanning,cn
    Processing Record 32 of Set 4 | aykhal 180
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aykhal,ru
    Processing Record 33 of Set 4 | okha 181
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=okha,ru
    Processing Record 34 of Set 4 | bannu 182
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bannu,pk
    Processing Record 35 of Set 4 | naze 183
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=naze,jp
    Processing Record 36 of Set 4 | fershampenuaz 184
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=fershampenuaz,ru
    Processing Record 37 of Set 4 | lesnoye 185
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lesnoye,ru
    Processing Record 38 of Set 4 | gambela 186
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gambela,et
    Processing Record 39 of Set 4 | urkarakh 187
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=urkarakh,ru
    Processing Record 40 of Set 4 | sabang 188
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sabang,id
    Processing Record 41 of Set 4 | dahuk 189
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dahuk,iq
    Processing Record 42 of Set 4 | pokaran 190
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pokaran,in
    Processing Record 43 of Set 4 | kashi 191
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kashi,cn
    Processing Record 44 of Set 4 | klimovsk 192
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=klimovsk,ru
    Processing Record 45 of Set 4 | bestobe 193
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bestobe,kz
    Processing Record 46 of Set 4 | kavaratti 194
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kavaratti,in
    Processing Record 47 of Set 4 | tignere 195
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tignere,cm
    Processing Record 48 of Set 4 | talnakh 196
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=talnakh,ru
    Processing Record 49 of Set 4 | kavieng 197
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kavieng,pg
    Processing Record 50 of Set 4 | bontang 198
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bontang,id
    Processing Record 51 of Set 4 | salalah 199
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=salalah,om
    Processing Record 52 of Set 4 | coulommiers 200
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=coulommiers,fr
    Processing Record 53 of Set 4 | marsa matruh 201
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=marsa matruh,eg
    Processing Record 54 of Set 4 | arlit 202
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=arlit,ne
    Processing Record 55 of Set 4 | aksarka 203
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aksarka,ru
    Processing Record 5 of Set 5 | talnakh 204
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=talnakh,ru
    Processing Record 6 of Set 5 | kavieng 205
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kavieng,pg
    Processing Record 7 of Set 5 | bontang 206
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bontang,id
    Processing Record 8 of Set 5 | salalah 207
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=salalah,om
    Processing Record 9 of Set 5 | coulommiers 208
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=coulommiers,fr
    Processing Record 10 of Set 5 | marsa matruh 209
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=marsa matruh,eg
    Processing Record 11 of Set 5 | arlit 210
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=arlit,ne
    Processing Record 12 of Set 5 | aksarka 211
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aksarka,ru
    Processing Record 13 of Set 5 | zalesovo 212
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zalesovo,ru
    Processing Record 14 of Set 5 | gorontalo 213
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gorontalo,id
    Processing Record 15 of Set 5 | muli 214
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=muli,mv
    Processing Record 16 of Set 5 | asnaes 215
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=asnaes,dk
    Processing Record 17 of Set 5 | dongsheng 216
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dongsheng,cn
    Processing Record 18 of Set 5 | pyapon 217
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pyapon,mm
    Processing Record 19 of Set 5 | chingirlau 218
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=chingirlau,kz
    Processing Record 20 of Set 5 | nyurba 219
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nyurba,ru
    Processing Record 21 of Set 5 | riyadh 220
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=riyadh,sa
    Processing Record 22 of Set 5 | belozerskoye 221
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=belozerskoye,ru
    Processing Record 23 of Set 5 | berlevag 222
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=berlevag,no
    Processing Record 24 of Set 5 | bahir dar 223
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bahir dar,et
    Processing Record 25 of Set 5 | taloqan 224
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=taloqan,af
    Processing Record 26 of Set 5 | hasaki 225
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hasaki,jp
    Processing Record 27 of Set 5 | hami 226
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hami,cn
    Processing Record 28 of Set 5 | asyut 227
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=asyut,eg
    Processing Record 29 of Set 5 | belaya gora 228
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=belaya gora,ru
    Processing Record 30 of Set 5 | haimen 229
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=haimen,cn
    Processing Record 31 of Set 5 | dawei 230
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dawei,mm
    Processing Record 32 of Set 5 | lyubytino 231
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lyubytino,ru
    Processing Record 33 of Set 5 | zhangye 232
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhangye,cn
    Processing Record 34 of Set 5 | lorengau 233
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lorengau,pg
    Processing Record 35 of Set 5 | vostok 234
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vostok,ru
    Processing Record 36 of Set 5 | alanya 235
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=alanya,tr
    Processing Record 37 of Set 5 | ust-nera 236
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ust-nera,ru
    Processing Record 38 of Set 5 | znamenskoye 237
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=znamenskoye,ru
    Processing Record 39 of Set 5 | tanout 238
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tanout,ne
    Processing Record 40 of Set 5 | mogzon 239
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mogzon,ru
    Processing Record 41 of Set 5 | koslan 240
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=koslan,ru
    Processing Record 42 of Set 5 | jonkoping 241
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jonkoping,se
    Processing Record 43 of Set 5 | baykit 242
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=baykit,ru
    Processing Record 44 of Set 5 | altay 243
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=altay,cn
    Processing Record 45 of Set 5 | lisakovsk 244
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lisakovsk,kz
    Processing Record 46 of Set 5 | roald 245
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=roald,no
    Processing Record 47 of Set 5 | berdigestyakh 246
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=berdigestyakh,ru
    Processing Record 48 of Set 5 | sebinkarahisar 247
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sebinkarahisar,tr
    Processing Record 49 of Set 5 | umm lajj 248
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=umm lajj,sa
    Processing Record 50 of Set 5 | sainte-maxime 249
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sainte-maxime,fr
    Processing Record 51 of Set 5 | tura 250
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tura,ru
    Processing Record 52 of Set 5 | songkhla 251
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=songkhla,th
    Processing Record 53 of Set 5 | ostrovnoy 252
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ostrovnoy,ru
    Processing Record 6 of Set 6 | lisakovsk 253
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lisakovsk,kz
    Processing Record 7 of Set 6 | roald 254
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=roald,no
    Processing Record 8 of Set 6 | berdigestyakh 255
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=berdigestyakh,ru
    Processing Record 9 of Set 6 | sebinkarahisar 256
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sebinkarahisar,tr
    Processing Record 10 of Set 6 | umm lajj 257
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=umm lajj,sa
    Processing Record 11 of Set 6 | sainte-maxime 258
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sainte-maxime,fr
    Processing Record 12 of Set 6 | tura 259
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tura,ru
    Processing Record 13 of Set 6 | songkhla 260
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=songkhla,th
    Processing Record 14 of Set 6 | ostrovnoy 261
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ostrovnoy,ru
    Processing Record 15 of Set 6 | aden 262
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aden,ye
    Processing Record 16 of Set 6 | shiraz 263
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=shiraz,ir
    Processing Record 17 of Set 6 | marawi 264
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=marawi,sd
    Processing Record 18 of Set 6 | olga 265
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=olga,ru
    Processing Record 19 of Set 6 | zavallya 266
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zavallya,ua
    Processing Record 20 of Set 6 | erdenet 267
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=erdenet,mn
    Processing Record 21 of Set 6 | pathein 268
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pathein,mm
    Processing Record 22 of Set 6 | de-kastri 269
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=de-kastri,ru
    Processing Record 23 of Set 6 | votkinsk 270
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=votkinsk,ru
    Processing Record 24 of Set 6 | beringovskiy 271
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=beringovskiy,ru
    Processing Record 25 of Set 6 | darhan 272
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=darhan,mn
    Processing Record 26 of Set 6 | tura 273
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tura,in
    Processing Record 27 of Set 6 | dusti 274
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dusti,tj
    Processing Record 28 of Set 6 | qeshm 275
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=qeshm,ir
    Processing Record 29 of Set 6 | petropavlovsk-kamchatskiy 276
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=petropavlovsk-kamchatskiy,ru
    Processing Record 30 of Set 6 | pokhara 277
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pokhara,np
    Processing Record 31 of Set 6 | kautokeino 278
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kautokeino,no
    Processing Record 32 of Set 6 | voloshka 279
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=voloshka,ru
    Processing Record 33 of Set 6 | srednekolymsk 280
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=srednekolymsk,ru
    Processing Record 34 of Set 6 | sungairaya 281
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sungairaya,id
    Processing Record 35 of Set 6 | semey 282
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=semey,kz
    Processing Record 36 of Set 6 | buta 283
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=buta,cd
    Processing Record 37 of Set 6 | kovdor 284
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kovdor,ru
    Processing Record 38 of Set 6 | den helder 285
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=den helder,nl
    Processing Record 39 of Set 6 | tezu 286
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tezu,in
    Processing Record 40 of Set 6 | zheleznodorozhnyy 287
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zheleznodorozhnyy,ru
    Processing Record 41 of Set 6 | kiruna 288
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kiruna,se
    Processing Record 42 of Set 6 | kapit 289
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kapit,my
    Processing Record 43 of Set 6 | sundsvall 290
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sundsvall,se
    Processing Record 44 of Set 6 | saryozek 291
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=saryozek,kz
    Processing Record 45 of Set 6 | nishihara 292
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nishihara,jp
    Processing Record 46 of Set 6 | bikaner 293
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bikaner,in
    Processing Record 47 of Set 6 | shimoda 294
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=shimoda,jp
    Processing Record 48 of Set 6 | kathu 295
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kathu,th
    Processing Record 49 of Set 6 | kolkwitz 296
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kolkwitz,de
    Processing Record 50 of Set 6 | buraydah 297
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=buraydah,sa
    Processing Record 51 of Set 6 | dudinka 298
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dudinka,ru
    Processing Record 7 of Set 7 | den helder 299
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=den helder,nl
    Processing Record 8 of Set 7 | tezu 300
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tezu,in
    Processing Record 9 of Set 7 | zheleznodorozhnyy 301
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zheleznodorozhnyy,ru
    Processing Record 10 of Set 7 | kiruna 302
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kiruna,se
    Processing Record 11 of Set 7 | kapit 303
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kapit,my
    Processing Record 12 of Set 7 | sundsvall 304
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sundsvall,se
    Processing Record 13 of Set 7 | saryozek 305
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=saryozek,kz
    Processing Record 14 of Set 7 | nishihara 306
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nishihara,jp
    Processing Record 15 of Set 7 | bikaner 307
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bikaner,in
    Processing Record 16 of Set 7 | shimoda 308
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=shimoda,jp
    Processing Record 17 of Set 7 | kathu 309
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kathu,th
    Processing Record 18 of Set 7 | kolkwitz 310
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kolkwitz,de
    Processing Record 19 of Set 7 | buraydah 311
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=buraydah,sa
    Processing Record 20 of Set 7 | dudinka 312
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dudinka,ru
    Processing Record 21 of Set 7 | waddan 313
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=waddan,ly
    Processing Record 22 of Set 7 | bayan 314
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bayan,cn
    Processing Record 23 of Set 7 | eisenerz 315
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=eisenerz,at
    Processing Record 24 of Set 7 | abnub 316
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=abnub,eg
    Processing Record 25 of Set 7 | misratah 317
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=misratah,ly
    Processing Record 26 of Set 7 | vrangel 318
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vrangel,ru
    Processing Record 27 of Set 7 | visnes 319
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=visnes,no
    Processing Record 28 of Set 7 | jiexiu 320
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jiexiu,cn
    Processing Record 29 of Set 7 | kanth 321
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kanth,in
    Processing Record 30 of Set 7 | kathmandu 322
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kathmandu,np
    Processing Record 31 of Set 7 | kulhudhuffushi 323
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kulhudhuffushi,mv
    Processing Record 32 of Set 7 | ivdel 324
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ivdel,ru
    Processing Record 33 of Set 7 | lulea 325
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lulea,se
    Processing Record 34 of Set 7 | verkhoyansk 326
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=verkhoyansk,ru
    Processing Record 35 of Set 7 | imeni stepana razina 327
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=imeni stepana razina,ru
    Processing Record 36 of Set 7 | kuybysheve 328
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kuybysheve,ua
    Processing Record 37 of Set 7 | aksu 329
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aksu,cn
    Processing Record 38 of Set 7 | abakaliki 330
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=abakaliki,ng
    Processing Record 39 of Set 7 | khandbari 331
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=khandbari,np
    Processing Record 40 of Set 7 | longyearbyen 332
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=longyearbyen,sj
    Processing Record 41 of Set 7 | iranshahr 333
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=iranshahr,ir
    Processing Record 42 of Set 7 | mao 334
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mao,td
    Processing Record 43 of Set 7 | uspenka 335
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=uspenka,ru
    Processing Record 44 of Set 7 | nogent-le-rotrou 336
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nogent-le-rotrou,fr
    Processing Record 45 of Set 7 | kargat 337
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kargat,ru
    Processing Record 46 of Set 7 | duldurga 338
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=duldurga,ru
    Processing Record 47 of Set 7 | novyy urgal 339
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=novyy urgal,ru
    Processing Record 48 of Set 7 | komsomolskiy 340
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=komsomolskiy,ru
    Processing Record 49 of Set 7 | linxia 341
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=linxia,cn
    Processing Record 50 of Set 7 | vanimo 342
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vanimo,pg
    Processing Record 51 of Set 7 | bhadrapur 343
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bhadrapur,np
    Processing Record 52 of Set 7 | awjilah 344
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=awjilah,ly
    Processing Record 53 of Set 7 | verkh-suetka 345
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=verkh-suetka,ru
    Processing Record 54 of Set 7 | medvedka 346
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=medvedka,ru
    Processing Record 55 of Set 7 | panzhihua 347
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=panzhihua,cn
    Processing Record 56 of Set 7 | maralal 348
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=maralal,ke
    Processing Record 57 of Set 7 | batangafo 349
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=batangafo,cf
    Processing Record 58 of Set 7 | dakoro 350
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dakoro,ne
    Processing Record 59 of Set 7 | rafsanjan 351
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rafsanjan,ir
    Processing Record 60 of Set 7 | abalak 352
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=abalak,ne
    Processing Record 8 of Set 8 | panzhihua 353
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=panzhihua,cn
    Processing Record 9 of Set 8 | maralal 354
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=maralal,ke
    Processing Record 10 of Set 8 | batangafo 355
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=batangafo,cf
    Processing Record 11 of Set 8 | dakoro 356
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dakoro,ne
    Processing Record 12 of Set 8 | rafsanjan 357
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rafsanjan,ir
    Processing Record 13 of Set 8 | abalak 358
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=abalak,ne
    Processing Record 14 of Set 8 | sibolga 359
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sibolga,id
    Processing Record 15 of Set 8 | norrtalje 360
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=norrtalje,se
    Processing Record 16 of Set 8 | sorland 361
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sorland,no
    Processing Record 17 of Set 8 | imeni poliny osipenko 362
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=imeni poliny osipenko,ru
    Processing Record 18 of Set 8 | zhigansk 363
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhigansk,ru
    Processing Record 19 of Set 8 | nizwa 364
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nizwa,om
    Processing Record 20 of Set 8 | ngaoundere 365
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ngaoundere,cm
    Processing Record 21 of Set 8 | toktogul 366
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=toktogul,kg
    Processing Record 22 of Set 8 | suez 367
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=suez,eg
    Processing Record 23 of Set 8 | gigmoto 368
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gigmoto,ph
    Processing Record 24 of Set 8 | mbandaka 369
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mbandaka,cd
    Processing Record 25 of Set 8 | yangjiang 370
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=yangjiang,cn
    Processing Record 26 of Set 8 | daltenganj 371
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=daltenganj,in
    Processing Record 27 of Set 8 | leningradskiy 372
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=leningradskiy,ru
    Processing Record 28 of Set 8 | sistranda 373
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sistranda,no
    Processing Record 29 of Set 8 | bellary 374
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bellary,in
    Processing Record 30 of Set 8 | filingue 375
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=filingue,ne
    Processing Record 31 of Set 8 | zhuhai 376
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhuhai,cn
    Processing Record 32 of Set 8 | nadvoitsy 377
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nadvoitsy,ru
    Processing Record 33 of Set 8 | hof 378
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hof,no
    Processing Record 34 of Set 8 | jian 379
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jian,cn
    Processing Record 35 of Set 8 | gilgit 380
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gilgit,pk
    Processing Record 36 of Set 8 | paldiski 381
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=paldiski,ee
    Processing Record 37 of Set 8 | aktau 382
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aktau,kz
    Processing Record 38 of Set 8 | ko samui 383
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ko samui,th
    Processing Record 39 of Set 8 | baoding 384
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=baoding,cn
    Processing Record 40 of Set 8 | singapore 385
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=singapore,sg
    Processing Record 41 of Set 8 | sawakin 386
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sawakin,sd
    Processing Record 42 of Set 8 | shahr-e babak 387
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=shahr-e babak,ir
    Processing Record 43 of Set 8 | makarov 388
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=makarov,ru
    Processing Record 44 of Set 8 | poltavka 389
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=poltavka,ru
    Processing Record 45 of Set 8 | mnogovershinnyy 390
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mnogovershinnyy,ru
    Processing Record 46 of Set 8 | venosa 391
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=venosa,it
    Processing Record 47 of Set 8 | kvarkeno 392
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kvarkeno,ru
    Processing Record 48 of Set 8 | cabra 393
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cabra,ph
    Processing Record 49 of Set 8 | gorno-altaysk 394
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gorno-altaysk,ru
    Processing Record 50 of Set 8 | roros 395
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=roros,no
    Processing Record 51 of Set 8 | labytnangi 396
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=labytnangi,ru
    Processing Record 52 of Set 8 | dumka 397
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dumka,in
    Processing Record 53 of Set 8 | manavalakurichi 398
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=manavalakurichi,in
    Processing Record 54 of Set 8 | bolu 399
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bolu,tr
    Processing Record 55 of Set 8 | tahta 400
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tahta,eg
    Processing Record 56 of Set 8 | ust-tsilma 401
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ust-tsilma,ru
    Processing Record 57 of Set 8 | verkhniy lomov 402
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=verkhniy lomov,ru
    Processing Record 58 of Set 8 | iquique 403
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=iquique,cl
    Processing Record 59 of Set 8 | mazagao 404
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mazagao,br
    Processing Record 60 of Set 8 | conde 405
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=conde,br
    Processing Record 9 of Set 9 | tahta 406
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tahta,eg
    Processing Record 10 of Set 9 | ust-tsilma 407
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ust-tsilma,ru
    Processing Record 11 of Set 9 | verkhniy lomov 408
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=verkhniy lomov,ru
    Processing Record 12 of Set 9 | iquique 409
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=iquique,cl
    Processing Record 13 of Set 9 | mazagao 410
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mazagao,br
    Processing Record 14 of Set 9 | conde 411
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=conde,br
    Processing Record 15 of Set 9 | calama 412
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=calama,cl
    Processing Record 16 of Set 9 | riachao das neves 413
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=riachao das neves,br
    Processing Record 17 of Set 9 | illapel 414
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=illapel,cl
    Processing Record 18 of Set 9 | fare 415
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=fare,pf
    Processing Record 19 of Set 9 | casa nova 416
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=casa nova,br
    Processing Record 20 of Set 9 | aquiraz 417
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aquiraz,br
    Processing Record 21 of Set 9 | rio pomba 418
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rio pomba,br
    Processing Record 22 of Set 9 | olavarria 419
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=olavarria,ar
    Processing Record 23 of Set 9 | lima 420
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lima,pe
    Processing Record 24 of Set 9 | mercedes 421
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mercedes,ar
    Processing Record 25 of Set 9 | medina 422
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=medina,br
    Processing Record 26 of Set 9 | santa rosa 423
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=santa rosa,bo
    Processing Record 27 of Set 9 | rurrenabaque 424
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rurrenabaque,bo
    Processing Record 28 of Set 9 | san carlos de bariloche 425
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san carlos de bariloche,ar
    Processing Record 29 of Set 9 | rocha 426
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rocha,uy
    Processing Record 30 of Set 9 | camana 427
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=camana,pe
    Processing Record 31 of Set 9 | ilhabela 428
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ilhabela,br
    Processing Record 32 of Set 9 | santa ines 429
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=santa ines,br
    Processing Record 33 of Set 9 | linhares 430
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=linhares,br
    Processing Record 34 of Set 9 | cabedelo 431
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cabedelo,br
    Processing Record 35 of Set 9 | el alto 432
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=el alto,pe
    Processing Record 36 of Set 9 | natal 433
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=natal,br
    Processing Record 37 of Set 9 | touros 434
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=touros,br
    Processing Record 38 of Set 9 | talara 435
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=talara,pe
    Processing Record 39 of Set 9 | arica 436
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=arica,cl
    Processing Record 40 of Set 9 | vila velha 437
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vila velha,br
    Processing Record 41 of Set 9 | porto belo 438
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=porto belo,br
    Processing Record 42 of Set 9 | santa branca 439
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=santa branca,br
    Processing Record 43 of Set 9 | tevaitoa 440
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tevaitoa,pf
    Processing Record 44 of Set 9 | carutapera 441
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=carutapera,br
    Processing Record 45 of Set 9 | barra 442
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=barra,br
    Processing Record 46 of Set 9 | pitimbu 443
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pitimbu,br
    Processing Record 47 of Set 9 | olinda 444
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=olinda,br
    Processing Record 48 of Set 9 | lincoln 445
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lincoln,ar
    Processing Record 49 of Set 9 | maceio 446
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=maceio,br
    Processing Record 50 of Set 9 | riberalta 447
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=riberalta,bo
    Processing Record 51 of Set 9 | diego de almagro 448
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=diego de almagro,cl
    Processing Record 52 of Set 9 | inhumas 449
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=inhumas,br
    Processing Record 53 of Set 9 | eirunepe 450
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=eirunepe,br
    Processing Record 54 of Set 9 | tefe 451
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tefe,br
    Processing Record 55 of Set 9 | axim 452
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=axim,gh
    Processing Record 56 of Set 9 | vallenar 453
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vallenar,cl
    Processing Record 57 of Set 9 | rio tercero 454
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rio tercero,ar
    Processing Record 58 of Set 9 | joao pinheiro 455
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=joao pinheiro,br
    Processing Record 59 of Set 9 | tupiza 456
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tupiza,bo
    Processing Record 60 of Set 9 | pacasmayo 457
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pacasmayo,pe
    Processing Record 10 of Set 10 | tefe 458
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tefe,br
    Processing Record 11 of Set 10 | axim 459
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=axim,gh
    Processing Record 12 of Set 10 | vallenar 460
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vallenar,cl
    Processing Record 13 of Set 10 | rio tercero 461
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rio tercero,ar
    Processing Record 14 of Set 10 | joao pinheiro 462
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=joao pinheiro,br
    Processing Record 15 of Set 10 | tupiza 463
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tupiza,bo
    Processing Record 16 of Set 10 | pacasmayo 464
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pacasmayo,pe
    Processing Record 17 of Set 10 | gari 465
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gari,ru
    Processing Record 18 of Set 10 | brae 466
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=brae,gb
    Processing Record 19 of Set 10 | teguldet 467
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=teguldet,ru
    Processing Record 20 of Set 10 | idah 468
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=idah,ng
    Processing Record 21 of Set 10 | bardoli 469
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bardoli,in
    Processing Record 22 of Set 10 | fukuma 470
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=fukuma,jp
    Processing Record 23 of Set 10 | namatanai 471
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=namatanai,pg
    Processing Record 24 of Set 10 | suhbaatar 472
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=suhbaatar,mn
    Processing Record 25 of Set 10 | mogadishu 473
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mogadishu,so
    Processing Record 26 of Set 10 | bandar-e lengeh 474
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bandar-e lengeh,ir
    Processing Record 27 of Set 10 | nichinan 475
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nichinan,jp
    Processing Record 28 of Set 10 | vinh 476
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vinh,vn
    Processing Record 29 of Set 10 | zhigalovo 477
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhigalovo,ru
    Processing Record 30 of Set 10 | puksoozero 478
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=puksoozero,ru
    Processing Record 31 of Set 10 | bedele 479
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bedele,et
    Processing Record 32 of Set 10 | karpogory 480
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=karpogory,ru
    Processing Record 33 of Set 10 | tilichiki 481
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tilichiki,ru
    Processing Record 34 of Set 10 | cotonou 482
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cotonou,bj
    Processing Record 35 of Set 10 | gravdal 483
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gravdal,no
    Processing Record 36 of Set 10 | kousseri 484
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kousseri,cm
    Processing Record 37 of Set 10 | porbandar 485
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=porbandar,in
    Processing Record 38 of Set 10 | hambantota 486
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hambantota,lk
    Processing Record 39 of Set 10 | tessaoua 487
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tessaoua,ne
    Processing Record 40 of Set 10 | thonon-les-bains 488
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=thonon-les-bains,fr
    Processing Record 41 of Set 10 | pyaozerskiy 489
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pyaozerskiy,ru
    Processing Record 42 of Set 10 | nagato 490
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nagato,jp
    Processing Record 43 of Set 10 | dandong 491
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dandong,cn
    Processing Record 44 of Set 10 | uglovskoye 492
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=uglovskoye,ru
    Processing Record 45 of Set 10 | shadegan 493
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=shadegan,ir
    Processing Record 46 of Set 10 | ola 494
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ola,ru
    Processing Record 47 of Set 10 | ust-maya 495
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ust-maya,ru
    Processing Record 48 of Set 10 | bassila 496
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bassila,bj
    Processing Record 49 of Set 10 | ibra 497
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ibra,om
    Processing Record 50 of Set 10 | ileza 498
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ileza,ru
    Processing Record 51 of Set 10 | irbit 499
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=irbit,ru
    Processing Record 52 of Set 10 | harnosand 500
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=harnosand,se
    Processing Record 53 of Set 10 | andenes 501
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=andenes,no
    Processing Record 54 of Set 10 | szczecin 502
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=szczecin,pl
    Processing Record 55 of Set 10 | keti bandar 503
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=keti bandar,pk
    Processing Record 56 of Set 10 | baghdad 504
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=baghdad,iq
    Processing Record 57 of Set 10 | ugoofaaru 505
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ugoofaaru,mv
    Processing Record 58 of Set 10 | jiblah 506
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jiblah,ye
    Processing Record 59 of Set 10 | gangapur 507
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gangapur,in
    Processing Record 60 of Set 10 | kushalgarh 508
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kushalgarh,in
    Processing Record 61 of Set 10 | jinji 509
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jinji,cn
    Processing Record 11 of Set 11 | baghdad 510
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=baghdad,iq
    Processing Record 12 of Set 11 | ugoofaaru 511
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ugoofaaru,mv
    Processing Record 13 of Set 11 | jiblah 512
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jiblah,ye
    Processing Record 14 of Set 11 | gangapur 513
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gangapur,in
    Processing Record 15 of Set 11 | kushalgarh 514
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kushalgarh,in
    Processing Record 16 of Set 11 | jinji 515
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jinji,cn
    Processing Record 17 of Set 11 | hamina 516
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hamina,fi
    Processing Record 18 of Set 11 | zhangzhou 517
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhangzhou,cn
    Processing Record 19 of Set 11 | pak phanang 518
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pak phanang,th
    Processing Record 20 of Set 11 | calabar 519
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=calabar,ng
    Processing Record 21 of Set 11 | neyshabur 520
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=neyshabur,ir
    Processing Record 22 of Set 11 | sinegorye 521
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sinegorye,ru
    Processing Record 23 of Set 11 | bilibino 522
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bilibino,ru
    Processing Record 24 of Set 11 | lapua 523
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lapua,fi
    Processing Record 25 of Set 11 | yerbogachen 524
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=yerbogachen,ru
    Processing Record 26 of Set 11 | ivankiv 525
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ivankiv,ua
    Processing Record 27 of Set 11 | alghero 526
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=alghero,it
    Processing Record 28 of Set 11 | syumsi 527
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=syumsi,ru
    Processing Record 29 of Set 11 | fukue 528
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=fukue,jp
    Processing Record 30 of Set 11 | ayan 529
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ayan,ru
    Processing Record 31 of Set 11 | krasnovka 530
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=krasnovka,ru
    Processing Record 32 of Set 11 | pokrovsk 531
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pokrovsk,ru
    Processing Record 33 of Set 11 | nenjiang 532
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nenjiang,cn
    Processing Record 34 of Set 11 | caruray 533
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=caruray,ph
    Processing Record 35 of Set 11 | koscian 534
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=koscian,pl
    Processing Record 36 of Set 11 | simbahan 535
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=simbahan,ph
    Processing Record 37 of Set 11 | kloulklubed 536
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kloulklubed,pw
    Processing Record 38 of Set 11 | hovd 537
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hovd,mn
    Processing Record 39 of Set 11 | ishim 538
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ishim,ru
    Processing Record 40 of Set 11 | itoman 539
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=itoman,jp
    Processing Record 41 of Set 11 | vilnius 540
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vilnius,lt
    Processing Record 42 of Set 11 | abatskoye 541
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=abatskoye,ru
    Processing Record 43 of Set 11 | cam ranh 542
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cam ranh,vn
    Processing Record 44 of Set 11 | kayan 543
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kayan,mm
    Processing Record 45 of Set 11 | nemuro 544
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nemuro,jp
    Processing Record 46 of Set 11 | luorong 545
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=luorong,cn
    Processing Record 47 of Set 11 | hun 546
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=hun,ly
    Processing Record 48 of Set 11 | batsfjord 547
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=batsfjord,no
    Processing Record 49 of Set 11 | korla 548
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=korla,cn
    Processing Record 50 of Set 11 | rapar 549
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rapar,in
    Processing Record 51 of Set 11 | kozhva 550
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kozhva,ru
    Processing Record 52 of Set 11 | gushikawa 551
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gushikawa,jp
    Processing Record 53 of Set 11 | kashary 552
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kashary,ru
    Processing Record 54 of Set 11 | khanpur 553
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=khanpur,pk
    Processing Record 55 of Set 11 | jiaozuo 554
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jiaozuo,cn
    Processing Record 56 of Set 11 | ha giang 555
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ha giang,vn
    Processing Record 57 of Set 11 | dubai 556
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dubai,ae
    Processing Record 58 of Set 11 | wum 557
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=wum,cm
    Processing Record 12 of Set 12 | batsfjord 558
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=batsfjord,no
    Processing Record 13 of Set 12 | korla 559
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=korla,cn
    Processing Record 14 of Set 12 | rapar 560
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rapar,in
    Processing Record 15 of Set 12 | kozhva 561
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kozhva,ru
    Processing Record 16 of Set 12 | gushikawa 562
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gushikawa,jp
    Processing Record 17 of Set 12 | kashary 563
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kashary,ru
    Processing Record 18 of Set 12 | khanpur 564
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=khanpur,pk
    Processing Record 19 of Set 12 | jiaozuo 565
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jiaozuo,cn
    Processing Record 20 of Set 12 | ha giang 566
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ha giang,vn
    Processing Record 21 of Set 12 | dubai 567
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dubai,ae
    Processing Record 22 of Set 12 | wum 568
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=wum,cm
    Processing Record 23 of Set 12 | altea 569
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=altea,es
    Processing Record 24 of Set 12 | klembivka 570
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=klembivka,ua
    Processing Record 25 of Set 12 | kedrovyy 571
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kedrovyy,ru
    Processing Record 26 of Set 12 | bogorodsk 572
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bogorodsk,ru
    Processing Record 27 of Set 12 | sembe 573
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sembe,cg
    Processing Record 28 of Set 12 | nadym 574
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=nadym,ru
    Processing Record 29 of Set 12 | proletarskiy 575
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=proletarskiy,ru
    Processing Record 30 of Set 12 | teya 576
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=teya,ru
    Processing Record 31 of Set 12 | sigli 577
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sigli,id
    Processing Record 32 of Set 12 | aswan 578
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aswan,eg
    Processing Record 33 of Set 12 | mangan 579
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mangan,in
    Processing Record 34 of Set 12 | sarkand 580
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sarkand,kz
    Processing Record 35 of Set 12 | leshukonskoye 581
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=leshukonskoye,ru
    Processing Record 36 of Set 12 | mut 582
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mut,tr
    Processing Record 37 of Set 12 | ust-kut 583
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ust-kut,ru
    Processing Record 38 of Set 12 | podgornoye 584
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=podgornoye,ru
    Processing Record 39 of Set 12 | xinan 585
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=xinan,cn
    Processing Record 40 of Set 12 | rybnaya sloboda 586
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rybnaya sloboda,ru
    Processing Record 41 of Set 12 | sauda 587
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sauda,no
    Processing Record 42 of Set 12 | bhadasar 588
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bhadasar,in
    Processing Record 43 of Set 12 | kushiro 589
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kushiro,jp
    Processing Record 44 of Set 12 | erzin 590
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=erzin,ru
    Processing Record 45 of Set 12 | changping 591
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=changping,cn
    Processing Record 46 of Set 12 | deputatskiy 592
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=deputatskiy,ru
    Processing Record 47 of Set 12 | puri 593
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=puri,in
    Processing Record 48 of Set 12 | toyoshina 594
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=toyoshina,jp
    Processing Record 49 of Set 12 | novobirilyussy 595
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=novobirilyussy,ru
    Processing Record 50 of Set 12 | sparti 596
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sparti,gr
    Processing Record 51 of Set 12 | folldal 597
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=folldal,no
    Processing Record 52 of Set 12 | taman 598
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=taman,ru
    Processing Record 53 of Set 12 | mangrol 599
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mangrol,in
    Processing Record 54 of Set 12 | buluang 600
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=buluang,ph
    Processing Record 55 of Set 12 | pischia 601
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pischia,ro
    Processing Record 56 of Set 12 | huilong 602
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=huilong,cn
    Processing Record 57 of Set 12 | sai buri 603
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sai buri,th
    Processing Record 58 of Set 12 | debre tabor 604
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=debre tabor,et
    Processing Record 59 of Set 12 | jabinyanah 605
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jabinyanah,tn
    Processing Record 60 of Set 12 | great yarmouth 606
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=great yarmouth,gb
    Processing Record 61 of Set 12 | sabha 607
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sabha,ly
    Processing Record 13 of Set 13 | buluang 608
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=buluang,ph
    Processing Record 14 of Set 13 | pischia 609
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pischia,ro
    Processing Record 15 of Set 13 | huilong 610
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=huilong,cn
    Processing Record 16 of Set 13 | sai buri 611
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sai buri,th
    Processing Record 17 of Set 13 | debre tabor 612
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=debre tabor,et
    Processing Record 18 of Set 13 | jabinyanah 613
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=jabinyanah,tn
    Processing Record 19 of Set 13 | great yarmouth 614
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=great yarmouth,gb
    Processing Record 20 of Set 13 | sabha 615
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sabha,ly
    Processing Record 21 of Set 13 | karacabey 616
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=karacabey,tr
    Processing Record 22 of Set 13 | gelgaudiskis 617
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gelgaudiskis,lt
    Processing Record 23 of Set 13 | pingliang 618
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pingliang,cn
    Processing Record 24 of Set 13 | katghora 619
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=katghora,in
    Processing Record 25 of Set 13 | adilcevaz 620
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=adilcevaz,tr
    Processing Record 26 of Set 13 | talant 621
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=talant,fr
    Processing Record 27 of Set 13 | batticaloa 622
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=batticaloa,lk
    Processing Record 28 of Set 13 | malaryta 623
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=malaryta,by
    Processing Record 29 of Set 13 | chegdomyn 624
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=chegdomyn,ru
    Processing Record 30 of Set 13 | furstenfeld 625
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=furstenfeld,at
    Processing Record 31 of Set 13 | alugan 626
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=alugan,ph
    Processing Record 32 of Set 13 | aleksandrov 627
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aleksandrov,ru
    Processing Record 33 of Set 13 | bintulu 628
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bintulu,my
    Processing Record 34 of Set 13 | huaicheng 629
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=huaicheng,cn
    Processing Record 35 of Set 13 | sorong 630
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sorong,id
    Processing Record 36 of Set 13 | sangar 631
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sangar,ru
    Processing Record 37 of Set 13 | xinxiang 632
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=xinxiang,cn
    Processing Record 38 of Set 13 | san roque 633
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=san roque,ph
    Processing Record 39 of Set 13 | chumikan 634
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=chumikan,ru
    Processing Record 40 of Set 13 | genhe 635
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=genhe,cn
    Processing Record 41 of Set 13 | svetlogorsk 636
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=svetlogorsk,ru
    Processing Record 42 of Set 13 | pandavapura 637
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=pandavapura,in
    Processing Record 43 of Set 13 | sheregesh 638
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sheregesh,ru
    Processing Record 44 of Set 13 | umm kaddadah 639
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=umm kaddadah,sd
    Processing Record 45 of Set 13 | wasserbillig 640
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=wasserbillig,lu
    Processing Record 46 of Set 13 | porto torres 641
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=porto torres,it
    Processing Record 47 of Set 13 | glowno 642
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=glowno,pl
    Processing Record 48 of Set 13 | najran 643
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=najran,sa
    Processing Record 49 of Set 13 | cuddapah 644
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cuddapah,in
    Processing Record 50 of Set 13 | porkhov 645
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=porkhov,ru
    Processing Record 51 of Set 13 | klyuchi 646
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=klyuchi,ru
    Processing Record 52 of Set 13 | dehloran 647
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dehloran,ir
    Processing Record 53 of Set 13 | sarakhs 648
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sarakhs,ir
    Processing Record 54 of Set 13 | miri 649
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=miri,my
    Processing Record 55 of Set 13 | tupik 650
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tupik,ru
    Processing Record 56 of Set 13 | avallon 651
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=avallon,fr
    Processing Record 57 of Set 13 | arkadak 652
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=arkadak,ru
    Processing Record 58 of Set 13 | moron 653
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=moron,mn
    Processing Record 59 of Set 13 | vanavara 654
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vanavara,ru
    Processing Record 60 of Set 13 | vilyuysk 655
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vilyuysk,ru
    Processing Record 61 of Set 13 | okhotsk 656
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=okhotsk,ru
    Processing Record 14 of Set 14 | miri 657
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=miri,my
    Processing Record 15 of Set 14 | tupik 658
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tupik,ru
    Processing Record 16 of Set 14 | avallon 659
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=avallon,fr
    Processing Record 17 of Set 14 | arkadak 660
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=arkadak,ru
    Processing Record 18 of Set 14 | moron 661
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=moron,mn
    Processing Record 19 of Set 14 | vanavara 662
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vanavara,ru
    Processing Record 20 of Set 14 | vilyuysk 663
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=vilyuysk,ru
    Processing Record 21 of Set 14 | okhotsk 664
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=okhotsk,ru
    Processing Record 22 of Set 14 | kamaishi 665
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kamaishi,jp
    Processing Record 23 of Set 14 | suruc 666
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=suruc,tr
    Processing Record 24 of Set 14 | ulaangom 667
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ulaangom,mn
    Processing Record 25 of Set 14 | damara 668
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=damara,cf
    Processing Record 26 of Set 14 | niamey 669
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=niamey,ne
    Processing Record 27 of Set 14 | shimanovsk 670
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=shimanovsk,ru
    Processing Record 28 of Set 14 | caska 671
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=caska,mk
    Processing Record 29 of Set 14 | bukachacha 672
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=bukachacha,ru
    Processing Record 30 of Set 14 | verkhnevilyuysk 673
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=verkhnevilyuysk,ru
    Processing Record 31 of Set 14 | gurun 674
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=gurun,my
    Processing Record 32 of Set 14 | along 675
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=along,in
    Processing Record 33 of Set 14 | cortes 676
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=cortes,ph
    Processing Record 34 of Set 14 | ouallam 677
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ouallam,ne
    Processing Record 35 of Set 14 | kamenka 678
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kamenka,ru
    Processing Record 36 of Set 14 | tokur 679
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=tokur,ru
    Processing Record 37 of Set 14 | zakamensk 680
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zakamensk,ru
    Processing Record 38 of Set 14 | yunhe 681
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=yunhe,cn
    Processing Record 39 of Set 14 | aksu 682
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=aksu,kz
    Processing Record 40 of Set 14 | mashhad 683
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=mashhad,ir
    Processing Record 41 of Set 14 | sergeyevka 684
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sergeyevka,kz
    Processing Record 42 of Set 14 | quzhou 685
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=quzhou,cn
    Processing Record 43 of Set 14 | itzehoe 686
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=itzehoe,de
    Processing Record 44 of Set 14 | kshenskiy 687
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kshenskiy,ru
    Processing Record 45 of Set 14 | ayorou 688
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ayorou,ne
    Processing Record 46 of Set 14 | atasu 689
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=atasu,kz
    Processing Record 47 of Set 14 | dera ghazi khan 690
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=dera ghazi khan,pk
    Processing Record 48 of Set 14 | yumen 691
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=yumen,cn
    Processing Record 49 of Set 14 | ahmadpur east 692
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=ahmadpur east,pk
    Processing Record 50 of Set 14 | sommerda 693
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sommerda,de
    Processing Record 51 of Set 14 | lhokseumawe 694
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lhokseumawe,id
    Processing Record 52 of Set 14 | oschersleben 695
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=oschersleben,de
    Processing Record 53 of Set 14 | kalat 696
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kalat,pk
    Processing Record 54 of Set 14 | rovinj 697
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rovinj,hr
    Processing Record 55 of Set 14 | serov 698
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=serov,ru
    Processing Record 56 of Set 14 | zhanaozen 699
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhanaozen,kz
    Processing Record 57 of Set 14 | zhoukou 700
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhoukou,cn
    Processing Record 15 of Set 15 | sommerda 701
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=sommerda,de
    Processing Record 16 of Set 15 | lhokseumawe 702
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=lhokseumawe,id
    Processing Record 17 of Set 15 | oschersleben 703
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=oschersleben,de
    Processing Record 18 of Set 15 | kalat 704
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=kalat,pk
    Processing Record 19 of Set 15 | rovinj 705
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=rovinj,hr
    Processing Record 20 of Set 15 | serov 706
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=serov,ru
    Processing Record 21 of Set 15 | zhanaozen 707
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhanaozen,kz
    Processing Record 22 of Set 15 | zhoukou 708
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhoukou,cn
    Processing Record 16 of Set 16 | zhoukou 709
    http://api.openweathermap.org/data/2.5/weather?appid=6842f8457dd8a6b32eaaad7d97b25fed&q=zhoukou,cn
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-43-107915ba6bbf> in <module>()
         17             print("Processing Record " + str(record) + " of Set " + str(set) +" | " + row['city_name'] + ' ' + str(x))
         18             print(target_url)
    ---> 19     time.sleep(60)
         20     record = 0
         21     set = set + 1
    

    KeyboardInterrupt: 



```python
newdf = readydf.dropna(axis=0, how='any')
display(len(newdf))
display(newdf.head())
```


    644



<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city_name</th>
      <th>country</th>
      <th>Latitude</th>
      <th>Max Temperature</th>
      <th>Humidity</th>
      <th>Wind Speed (mph)</th>
      <th>Cloudiness %</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>georgetown</td>
      <td>sh</td>
      <td>-7.93</td>
      <td>77.0</td>
      <td>65.0</td>
      <td>18.34</td>
      <td>75.0</td>
      <td>2017-12-11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>rikitea</td>
      <td>pf</td>
      <td>-23.12</td>
      <td>72.2</td>
      <td>100.0</td>
      <td>13.22</td>
      <td>92.0</td>
      <td>2017-12-11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rio gallegos</td>
      <td>ar</td>
      <td>-51.62</td>
      <td>55.4</td>
      <td>71.0</td>
      <td>8.05</td>
      <td>75.0</td>
      <td>2017-12-11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>jamestown</td>
      <td>sh</td>
      <td>-20.22</td>
      <td>69.8</td>
      <td>56.0</td>
      <td>11.41</td>
      <td>20.0</td>
      <td>2017-12-11</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ushuaia</td>
      <td>ar</td>
      <td>-0.12</td>
      <td>93.2</td>
      <td>52.0</td>
      <td>11.41</td>
      <td>20.0</td>
      <td>2017-12-11</td>
    </tr>
  </tbody>
</table>
</div>



```python
plt.clf()

# # Incorporate the other graph properties
ax = sns.jointplot(x='Latitude', y='Max Temperature',data=newdf, color="r",size=10)
plt.title("Temperature (F) vs. Latitude" ,size=20).set_position([-3, 1.2])

# # Save the figure
plt.savefig("Temperature (F) vs. Latitude.png")

# # Show plot
plt.show()
```


    <matplotlib.figure.Figure at 0x1a3d89cca90>



![png](output_19_1.png)



```python
plt.clf()

# # Incorporate the other graph properties
ax = sns.jointplot(x='Latitude', y='Humidity',data=newdf, color="b",size=10)
plt.title("Humidity (%) vs. Latitude",size=20).set_position([-3, 1.2])

# # Save the figure
plt.savefig("Humidity (%) vs. Latitude.png")

# # Show plot
plt.show()
```


    <matplotlib.figure.Figure at 0x1a3d6607860>



![png](output_20_1.png)



```python
plt.clf()

# # Incorporate the other graph properties
ax = sns.jointplot(x='Latitude', y='Cloudiness %',data=newdf, color="g",size=10)
plt.title("Cloudiness (%) vs. Latitude",size=20).set_position([-3, 1.2])

# # Save the figure
plt.savefig("Cloudiness (%) vs. Latitude.png")

# # Show plot
plt.show()
```


    <matplotlib.figure.Figure at 0x1a3d750e780>



![png](output_21_1.png)



```python
plt.clf()

# # Incorporate the other graph properties
ax = sns.jointplot(x='Latitude', y='Wind Speed (mph)',data=newdf, color="gray",size=10)
plt.title("Wind Speed (mph) vs. Latitude",size=20).set_position([-3, 1.2])

# # Save the figure
plt.savefig("Wind Speed (mph) vs. Latitude.png")

# # Show plot
plt.show()
```


    <matplotlib.figure.Figure at 0x1a3d76a4358>



![png](output_22_1.png)



```python
newdf.to_csv('weather.csv')
```
