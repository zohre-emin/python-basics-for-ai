####################

### Answer1 ###
"""name = "Kaan"
print(type(name)) # str

age = 35
print(type(age)) # int

avarage = 3.45
print(type(avarage)) # float
"""

### Answer 2 ### 
"""age = int(input("Enter your age: "))
print(type(age))

print(f"You will be {age + 5} years old after 5 years later.")
"""

### Answer3 ###
"""price = float(input("Enter the price of the product without tax rate: "))

price_with_tax_rate = price + price *18/100
print(f"pprice of the product with a 18% of tax rate is {round(price_with_tax_rate,2)}.")
print("price of the product with 18% of tax rate is ", round(price_with_tax_rate,2), ".")
print(f"Price of the product with 18% tax rate is {price_with_tax_rate:.2f}")
"""
### Answer4 ###
"""numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[4])
print(numbers[2:])

numbers.append(60)
print(numbers)

#numbers.pop(1)
numbers.remove(20)
print(numbers)

print(numbers[3:])
"""

### ANswer5 ###
"""coordinate = (12, 34)

x, y = (12, 34)

print(x)
print(y)

print(type(x))

## coordinate[0] = 99 : ERROR
# """

### Answer6 ### 
"""student = {"Name": "Ayse", "Age": 22, "Department": "Software"}

print(student["Name"])

student["Grade"] = 90
print(student)

student["Age"] = 23
print(student)

print(student.keys())
print(student.values())
print(student.items())
"""

### Answer7 ###
"""list = ["Ali", "Ayse", "Ali", "Mehmet", "Ayse"]

print(list.count("Ayse"))
print(list.count("Ali"))

new_list = set(list)

print(set(list))
print(len(new_list))"""