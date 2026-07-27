#########################################################
import pandas as pd

data ={
    "Name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "Age": [25, 30, 28, 35, 22, 27],
    "City": ["Ankara", "Istanbul", "Ankara", "Izmir", "Bursa", "Istanbul"],
    "Salary": [5000, 7000, 6000, 8000, 4500, 6500]
}
df = pd.DataFrame(data)
print("Dataset")
print(df)

### Answer 1 ###
print("1. First three rows: ")
print(df.head(3))
print()

### Answer 2 ###
print("2. Column names of Dataset: ")
print(df.columns)
print()

### Answer 3 ###
print("3. Names of workers: ")
print(df["Name"])
print()

### Answer 4 ###
print("4. Names of workers and their Salaries: ")
print(df[["Name", "Salary"]])
print()

### Answer 5 ### 
print("5. Workers older then 28 years: ")
print(df[df["Age"] > 28])
print()

### Answer 6 ###
print("6. Names and salaries of workers earning more then 6000: ")
print(df[df["Salary"] > 6000][["Name", "Salary"]])
print()

### Answer 7 ###
print("7. ")
print(df.sort_values("Salary"))
print()

### Answer 8 ###
print("8. ")
print(df.sort_values("Salary", ascending=False))
print()

### Answer 9 ###
print("9. ")
print(df.groupby("City")["Salary"].mean())
print()

### Answer 10 ###
print("10. ")
df["Annual"] = df["Salary"] * 12
print(df)
print()