#########################################################################

### 9.1 Introduction to Pandas ###

### 9.2 Series ###
"""
import pandas as pd

data = pd.Series([10, 20, 30, 40])
print(data)

data = pd.Series([10, 20, 30, 40])
print(data[0])
print(data[1])

data = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(data)
print(data["b"])

# creating series with dictionary

data = {
    "ali": 80,
    "ayse:": 90,
    "mehmet": 75
}

s = pd.Series(data)
print(s)

print(s.index)
print(s.values)
print(s.dtype)

data = pd.Series([10, 20, 30, 40])
result = data * 2
print(data)

# Series Filtering

age = pd.Series([10, 20, 30, 40, 50])
filtre = age > 25
print(filtre)

result = age[filtre]
print(result)
"""

### 9.3 Data Frame ###
"""
import pandas as pd

data = {
    "name": ["ali", "ayse","mehmet"],
    "age": [25, 30, 28],
    "city": ["Ankara", "Istanbul", "Izmir"]
}
df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df.shape)

print(df["name"])
print(df[["name", "age"]])

# new column
df["salary"] = [5000, 7000, 6000]
print(df)

# Deleting columns
df = df.drop("city", axis = 1)

# First 5 rows
print(df.head())

# last 5 rows
print(df.tail())

# Information about dataFrame
print(df.info())
"""
 
### 9.4 Reading an Writing Data (I/O) ###
"""
import pandas as pd

# Reading CSV (commo saparated Values)

df= pd.read_csv("new.csv")
print(df)

# Reading excel 

df = pd.read_excel("data.xlsx")
print(df)

# Writing csv 

data = {
    "name": ["ali", "ayse", "mehmet"],
    "age": [25, 30, 35]
}
df =pd.DataFrame(data)
df.to_csv("data_output.csv", index = False)

# Writing excel
df.to_excel("data_output.xlsx", index = False)
"""

### 9.5 Selecting and Filtering data ###
"""
import pandas as pd

data = {
    "name": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "age": [25, 30, 28, 35, 22],
    "city": ["Ankara", "Istanbul", "Izmir", "Ankara", "Bursa"],
    "salary": [5000, 7000, 6000, 8000, 4500]
}
df = pd.DataFrame(data)
print(df)
print(df["name"])
print(df[["name", "salary"]])

# selelcting rows: iloc
print(df.iloc[0])
print(df.iloc[0: 3])
print(df.loc[2])

print(df.loc[:, ["name", "salary"]])
print(df.loc[2, ["name","salary"]])

filtre = df["age"] > 25
print(filtre)

filtre = df["age"] > 30
print(filtre)

result = df[filtre]
print(result)

print(df[df["age"] > 30])

result = df[(df["city"] == "Ankara") & (df["salary"] > 6000)]
print(result)

print(df[df["city"] == "Ankara"])

print(df[df["age"] > 25][["name", "salary"]])
"""

### 9.6 Row and Column Operations ###
"""
import pandas as pd

data = {
    "name": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "age": [25,  30, 28, 35, 22],
    "salary": [5000, 70000, 6000, 8000, 4500]
}
df = pd.DataFrame(data)
print(df)

# Adding new column to the data frame
df["city"] = ["Ankara", "Istanbul", "Izmir", "Ankara", "Bursa"]
print(df)

df["annual salary"] = df["salary"] * 12
print(df)

# Deleting column
df = df.drop("salary", axis = 1)
print(df)

# Cahnging a columns name
df = df.rename(columns={"annual salary":"annual"})
print(df)

# New row
df.loc[3] = ["zeynep", 32, "Ankara", 8000]
print(df)

# Deleting a row
df = df.drop(0)
print(df)

# Reordering index values 
df = df.reset_index(drop = True)
print(df)
"""

### 9.7 GrpoupBy Operaitons ###
"""
import pandas as pd

data = {
    "name": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "age": [25, 30, 28, 35, 22],
    "city": ["Ankara", "Istanbul", "Ankara", "Izmir", "Istanbul"],
    "salary": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(data)
print(df)

# Sorting

df_sorted = df.sort_values("salary")
print("Sorted: \n", df_sorted)

df_sorted = df.sort_values("salary", ascending= False)
print("Sorted: \n", df_sorted)

df_sorted = df.sort_values(["city", "salary"])
print(df_sorted)

# GroupBy
groups = df.groupby("city")
print(groups)

result = df.groupby("city")["salary"].mean()
print(result)

result = df.groupby("city")["salary"].sum()
print(result)

result = df.groupby("city")["name"].count()
print(result)

result = df.groupby("city")["salary"].agg(["mean", "max", "min"])
print(result)
"""

### 9.8 Common Pandas Functions

# This is copied from gitHub since I lost all my code by mistake
"""
import pandas as pd
veri = {
    "isim": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "yas": [25, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)

# head fonksiyonu ile ilk 5 satırı görelim
print(df.head())

# tail ile son satırları görme
print(df.tail(3))

# info()
print(df.info())


# sayısal sütunların temel istatistiklerini görmek için describe()
print(df.describe())


# bir sütunda ki değerlerin kaç kez tekrar ettiğini görmek için value_counts()
print(df["sehir"].value_counts())

# bir sütunda ki benzersiz değerleri görmek için unique fonksiyonunu kullanırız
print(df["sehir"].unique()) # ['Ankara', 'İstanbul', 'İzmir']

# bir sütunda kaç farklı değer olduğunu görmek için nunique
print(df["sehir"].nunique()) # 3

"""

