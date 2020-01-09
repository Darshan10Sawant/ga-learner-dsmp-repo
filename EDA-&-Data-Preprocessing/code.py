# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data=pd.read_csv(path)
data['Rating'].hist()
data=data[data['Rating']<=5]
data['Rating'].hist()
#Code ends here


# --------------
# code starts here
import numpy as np
total_null=data.isnull().sum()
percent_null=(total_null*100/data.isnull().count())
missing_data=pd.concat([total_null, percent_null], axis=1,keys=['Total','Percent'])
print(missing_data)
data.dropna(inplace=True)

total_null_1=data.isnull().sum()
percent_null_1=(total_null*100/data.isnull().count())
missing_data_1=pd.concat([total_null_1, percent_null_1], axis=1,keys=['Total','Percent'])
print(missing_data_1)
# code ends here


# --------------

#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
plt.xticks(rotation=90)
plt.title("Rating vs Category [BoxPlot]")

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())

data['Installs']=data['Installs'].str.replace(',', '')
data['Installs']=data['Installs'].str.replace('+', '')
data['Installs']=data['Installs'].astype(np.int64)
print("data type of column : ",data['Installs'].dtype)
#Code ends here
le=LabelEncoder()
data['Installs']=le.fit_transform(data['Installs'])

sns.regplot(x="Installs",y="Rating",data=data)
plt.title("Rating vs Installs")


# --------------
#Code starts here
#print(data['Price'].value_counts())
data['Price']=data['Price'].str.replace('$','')
data['Price']=data['Price'].astype(np.float64)
sns.regplot(x="Price",y="Rating",data=data)
plt.title("Rating vs Price [RegPlot]")
#Code ends here


# --------------

#Code starts here
data['Genres'].unique()
data['Genres']=data['Genres'].str.split(';').str[0]


gr_mean=data[["Genres", "Rating"]].groupby(['Genres'], as_index=False).mean()

gr_mean.describe()
gr_mean.sort_values(by='Rating',inplace=True,ascending=True)
print(gr_mean.iloc[[0,-1]])
#Code ends here


# --------------

#Code starts here
data.plot('Last Updated')
#print(data['Last Updated'].dtype)
data['Last Updated']= pd.to_datetime(data['Last Updated']) 
max_date=max(data['Last Updated'])
data['Last Updated Days']=(max_date-data['Last Updated']).dt.days
print(data['Last Updated Days'].head())
sns.regplot(x="Last Updated Days",y="Rating",data=data)
plt.title("Rating vs Last Updated [RegPlot]")
#Code ends here


