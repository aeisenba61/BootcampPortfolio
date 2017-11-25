
# Heroes Of Pymoli Data Analysis

## Observed Trends
1. Men make up 80.4% of the Heroes of Pymoli players.
2. The 20-24 age group spent the most money overall in the game with $1087.66, although the highest spending on average came from the 40+ group
3. Whereas the Arcane Gem was the highest selling item in the game it was only 5th on the most profitable list. The Retribution Axe earned the top spot for being the most profitable item sold garnering $37 from 9 sales to the Arcane Gem's $29 from 12 sales.  
## Initial import


```python
import pandas as pd
import json
import glob
import os
```


```python
os.remove('finalFile.json')
glob_data = []
for file in glob.glob('*.json'):
    with open(file) as json_file:
        data = json.load(json_file)

        i = 0
        while i < len(data):
            glob_data.append(data[i])
            i += 1

with open('finalFile.json', 'w') as f:
    json.dump(glob_data, f, indent=4)
```


```python
df = pd.read_json('finalFile.json')
#df.head(3)
```

## Player Count


```python
#Total Number of Players
df['Unique_ID'] = df['SN'] + df['Gender']
total_players = len(df['Unique_ID'].unique())
tp_df = pd.DataFrame()
tp_df.set_value(0,'Total Players',total_players)
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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619.0</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)


```python
#Number of Unique Items
unique_items = len(df['Item Name'].unique())
#Average Purchase Price
avg_price = df['Price'].mean()
#Total Number of Purchases
total_purchases = len(df)
#Total Revenue
total_revenue = df['Price'].sum()
#Create Summary dataframe
summary_df = pd.DataFrame()
summary_df.set_value(0,'Number of Unique Items',unique_items)
summary_df.set_value(0,'Average Price',avg_price)
summary_df.set_value(0,'Number of Purchases',total_purchases)
summary_df.set_value(0,'Total Revenue',total_revenue)
summary_df["Number of Unique Items"] = summary_df["Number of Unique Items"].map( '{:.0f}'.format)
summary_df["Number of Purchases"] = summary_df["Number of Purchases"].map( '{:.0f}'.format)
summary_df["Average Price"] = summary_df["Average Price"].map( '${:.2f}'.format)
summary_df["Total Revenue"] = summary_df["Total Revenue"].map( '${:.2f}'.format)
summary_df

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
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>180</td>
      <td>$2.93</td>
      <td>858</td>
      <td>$2514.43</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics


```python
df_SN_Gender_wdups = df[['SN','Gender']]
df_SN_Gender = df_SN_Gender_wdups.drop_duplicates()
#df_SN_Gender.head()
#Count of Player Demographics
gender_breakdown = df_SN_Gender["Gender"].value_counts()#.to_frame().reset_index()
#Percentage of Player Demographics and convert to DataFrame
gender_breakdown_percent = (gender_breakdown / total_players * 100).to_frame().reset_index()
#Convert to DataFrame
gender_breakdown_df = gender_breakdown.to_frame().reset_index()
#Rename columns
gender_breakdown_percent.columns = ['Gender', 'Percentage of Players']
gender_breakdown_df.columns = ['Gender', 'Total Count']
```


```python
#Merge tables create summary Demographics table and format
merge_table = pd.merge(gender_breakdown_percent, gender_breakdown_df, on='Gender')
merge_table["Percentage of Players"] = merge_table["Percentage of Players"].map( '{:.2f}%'.format)

```

## Purchasing Analysis (Gender)


```python
#* The below each broken by gender
#  * Purchase Count
#  * Average Purchase Price
#  * Total Purchase Value
#  * Normalized Totals

df2 = df.groupby('Gender')
gender_count = df2['Age'].count().to_frame().reset_index()
gender_count.columns = ['Gender','Purchase Count']
gender_avg = df2['Price'].mean().to_frame().reset_index()
gender_avg.columns = ['Gender','Average Purchase Price']
gender_total_value = df2['Price'].sum().to_frame().reset_index()
gender_total_value.columns = ['Gender','Total Purchase Value']
gender_normalize = (df2['Price'].sum() / df_SN_Gender['Gender'].value_counts()).to_frame().reset_index()
gender_normalize.columns = ['Gender', 'Normalized Totals']
tmp1 = pd.merge(gender_count,gender_avg, on='Gender')
tmp2 = pd.merge(tmp1,gender_total_value, on='Gender')
purchase_analysis = pd.merge(tmp2,gender_normalize, on='Gender')
df_SN_Gender['Gender'].value_counts()
```




    Male                     498
    Female                   112
    Other / Non-Disclosed      9
    Name: Gender, dtype: int64




```python
#Formatting
purchase_analysis["Average Purchase Price"] = purchase_analysis["Average Purchase Price"].map("${:.2f}".format)
purchase_analysis["Total Purchase Value"] = purchase_analysis["Total Purchase Value"].map("${:.2f}".format)
purchase_analysis["Normalized Totals"] = purchase_analysis["Normalized Totals"].map("${:.2f}".format)
purchase_analysis

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
      <th>Gender</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Female</td>
      <td>149</td>
      <td>$2.85</td>
      <td>$424.29</td>
      <td>$3.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Male</td>
      <td>697</td>
      <td>$2.94</td>
      <td>$2052.28</td>
      <td>$4.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>12</td>
      <td>$3.15</td>
      <td>$37.86</td>
      <td>$4.21</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics 


```python
#* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.) 
#  * Purchase Count
#  * Average Purchase Price
#  * Total Purchase Value
#  * Normalized Totals
dfAge = df
bins = [0,9,14,19,24,29,34,39,100]
group_names = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']
```


```python
dfAge['AgeGroup'] = pd.cut(df["Age"], bins, labels=group_names)
dfAge.head()
# with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
#     display(dfAge.sort_values('Age'))
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Unique_ID</th>
      <th>AgeGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>Aelalis34Male</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>Eolo46Male</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>Assastnya25Male</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>Pheusrical25Male</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>Aela59Male</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = df.groupby('AgeGroup')
age_count = df3['Age'].count().to_frame().reset_index()
age_count.columns = ['Age Group','Purchase Count']
age_avg = df3['Price'].mean().to_frame().reset_index()
age_avg.columns = ['Age Group','Average Purchase Price']
age_total_value = df3['Price'].sum().to_frame().reset_index()
age_total_value.columns = ['Age Group','Total Purchase Value']
age_normalize = (age_total_value['Total Purchase Value']/age_count['Purchase Count']).to_frame().reset_index(drop=True)
age_normalize['Age Group'] = group_names
cols = ['Normalized Totals','Age Group']
age_normalize.columns = cols
age_normalize = age_normalize[['Age Group','Normalized Totals']]
tmp_age1 = pd.merge(age_count,age_avg, on='Age Group')
tmp_age2 = pd.merge(tmp_age1,age_total_value, on='Age Group')
age_purchase_analysis = pd.merge(tmp_age2,age_normalize, on='Age Group')
```


```python
age_purchase_analysis["Average Purchase Price"] = age_purchase_analysis["Average Purchase Price"].map("${:.2f}".format)
age_purchase_analysis["Total Purchase Value"] = age_purchase_analysis["Total Purchase Value"].map("${:.2f}".format)
age_purchase_analysis["Normalized Totals"] = age_purchase_analysis["Normalized Totals"].map("${:.2f}".format)
age_purchase_analysis
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
      <th>Age Group</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>&lt;10</td>
      <td>33</td>
      <td>$2.95</td>
      <td>$97.28</td>
      <td>$2.95</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10-14</td>
      <td>38</td>
      <td>$2.79</td>
      <td>$105.91</td>
      <td>$2.79</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15-19</td>
      <td>144</td>
      <td>$2.89</td>
      <td>$416.83</td>
      <td>$2.89</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20-24</td>
      <td>372</td>
      <td>$2.92</td>
      <td>$1087.66</td>
      <td>$2.92</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25-29</td>
      <td>134</td>
      <td>$2.96</td>
      <td>$396.44</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>5</th>
      <td>30-34</td>
      <td>71</td>
      <td>$2.97</td>
      <td>$211.14</td>
      <td>$2.97</td>
    </tr>
    <tr>
      <th>6</th>
      <td>35-39</td>
      <td>48</td>
      <td>$2.93</td>
      <td>$140.77</td>
      <td>$2.93</td>
    </tr>
    <tr>
      <th>7</th>
      <td>40+</td>
      <td>18</td>
      <td>$3.24</td>
      <td>$58.40</td>
      <td>$3.24</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders


```python
# * Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
top_spenders_group = df.groupby(['Unique_ID'])
tpv = top_spenders_group['Price'].sum().sort_values(ascending=False).head(5).to_frame().reset_index()
tpv.columns = ('Unique_ID','Total Purchase Value')
df_filtered = df[df['Unique_ID'].isin(tpv['Unique_ID'])]
df_filtered_group= df_filtered.groupby(['Unique_ID'])
pc = df_filtered_group['Age'].count().to_frame().reset_index()
pc.columns = ('Unique_ID', 'Purchase Count')
ts_merger = pd.merge(tpv,pc,on='Unique_ID')
ts_merger['Average Purchase Price'] = ts_merger["Total Purchase Value"] / ts_merger['Purchase Count'] 
ts_merger['Average Purchase Price'] = ts_merger['Average Purchase Price'].map("${:.2f}".format)
ts_merger["Purchase Count"] = ts_merger["Purchase Count"].map("{:.0f}".format)
ts_merger["Total Purchase Value"] = ts_merger["Total Purchase Value"].map("${:.2f}".format)
ts_merger = ts_merger[['Unique_ID',"Purchase Count",'Average Purchase Price',"Total Purchase Value"]]
ts_merger
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
      <th>Unique_ID</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Undirrala66Male</td>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aerithllora36Male</td>
      <td>4</td>
      <td>$3.77</td>
      <td>$15.10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Saedue76Male</td>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sondim43Male</td>
      <td>4</td>
      <td>$3.25</td>
      <td>$13.02</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mindimnya67Female</td>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
  </tbody>
</table>
</div>



# Most Popular Items


```python
top_items_group = df.groupby(['Item ID'])
ti_df = top_items_group['Price'].count().sort_values(ascending=False).head(5).to_frame().reset_index()
ti_df.columns = ('Item ID', 'Purchase Count')
ti_df_filtered = df[df['Item ID'].isin(ti_df['Item ID'])]
ti_df_group = ti_df_filtered.groupby(['Item ID'])
tip = ti_df_group['Price'].sum().to_frame().reset_index()
tip.columns = ('Item ID', 'Total Purchase Value')
itemname = ti_df_filtered[['Item ID','Item Name']].drop_duplicates()
item_merger = pd.merge(ti_df, tip, on= 'Item ID')
item_merger2 = pd.merge(item_merger,itemname, on='Item ID') 
item_merger2['Average Item Price'] = item_merger2["Total Purchase Value"] / item_merger2['Purchase Count'] 
pop_items = item_merger2[['Item ID','Item Name','Purchase Count','Average Item Price','Total Purchase Value']]
pop_items['Average Item Price'] = pop_items['Average Item Price'].map("${:.2f}".format)
pop_items['Purchase Count'] = pop_items['Purchase Count'].map("{:.0f}".format)
pop_items['Total Purchase Value'] = pop_items['Total Purchase Value'].map("${:.2f}".format)
pop_items
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Average Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>12</td>
      <td>$2.45</td>
      <td>$29.34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31</td>
      <td>Trickster</td>
      <td>10</td>
      <td>$2.32</td>
      <td>$23.22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>9</td>
      <td>$2.67</td>
      <td>$24.04</td>
    </tr>
  </tbody>
</table>
</div>



# Most Profitable Items


```python
top_items_group = df.groupby(['Item ID'])
ti_df = top_items_group['Price'].sum().sort_values(ascending=False).head(5).to_frame().reset_index()
ti_df.columns = ('Item ID', 'Total Purchase Value')
ti_df_filtered = df[df['Item ID'].isin(ti_df['Item ID'])]
ti_df_group = ti_df_filtered.groupby(['Item ID'])
ti_count = ti_df_group['Price'].count().to_frame().reset_index()
ti_count.columns = ('Item ID', 'Purchase Count')
itemname = ti_df_filtered[['Item ID','Item Name']].drop_duplicates()
item_merger = pd.merge(ti_df, ti_count, on= 'Item ID')
item_merger2 = pd.merge(item_merger,itemname, on='Item ID') 
item_merger2['Average Item Price'] = item_merger2["Total Purchase Value"] / item_merger2['Purchase Count'] 
prof_items = item_merger2[['Item ID','Item Name','Purchase Count','Average Item Price','Total Purchase Value']]
prof_items['Average Item Price'] = prof_items['Average Item Price'].map("${:.2f}".format)
prof_items['Purchase Count'] = prof_items['Purchase Count'].map("{:.0f}".format)
prof_items['Total Purchase Value'] = prof_items['Total Purchase Value'].map("${:.2f}".format)
prof_items
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Average Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>9</td>
      <td>$3.67</td>
      <td>$33.03</td>
    </tr>
    <tr>
      <th>2</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>12</td>
      <td>$2.45</td>
      <td>$29.34</td>
    </tr>
  </tbody>
</table>
</div>


