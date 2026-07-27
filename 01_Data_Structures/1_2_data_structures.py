### 1.3 Hello World ###
"""
print("Heloo World")
"""

### 2.2 Intiger(int) ###
"""
age = 35 
number_of_students = 55000
temperature = -15

print(age)
print(35)

a = 10
b = 5 
sum = a+b
print(sum)

sub = a - b
print(sub)

dev = a/b
print(dev)

number_of_product = 8
price_per_product = 10

total = number_of_product*price_per_product

print(total)

rate = int(input("Enter the rate: "))
print(rate)
zamli_fiyat = price_per_product + price_per_product * rate/100

print(zamli_fiyat)

"""
### 2.3 Float ###

"""
pi = 3.14

temperature = 35.5

price = 99.9

print(temperature)

a = 35. 
b = 2.0

print(a + b)
print(a/b)

print(0.1 + 0.2)

result = 0.1 + 0.2
print(result)

rounded_result = round(result,3)
print(rounded_result)

price = float(input("Enter the price: "))
print(price)
price_with_kdv = price + 20*price/100

print(price_with_kdv)

"""
### 2.4 String ###

"""
name = "kaan"
company = "Ucanble"
information = "Ucanble is the name of Sir Kaan`s company"
print(information)

information2 = company + " is the name of Sir " + name + "`s company"
print(information2)

age = 35
int_to_str = str(age)
name  = "Kaan"
result = "Sir " + name + "`s age is " + int_to_str + "."

print(result)

"""
### 2.5 String2 ###

"""
print("Ucanble Technology was estableshid in 2023.")
estableshed_date = 2023
print("Ucanble Technology was estableshed in " + str(estableshed_date) + ".")

# f string
print(f"Ucanble Technology was established in {estableshed_date}.")

accuracy = 95
print(f"Decision Trees accuricy: {accuracy}%")

# string indexing

word = "python"
print(word[0])
print(word[3])

#string methods 

text = "Python"
lower_case_text = text.lower()
print(lower_case_text)
print(len(text))
print(text.replace("o", "O"))

"""
### 2.6 Veri Tipi Kontrolü ve Tip Dönüşümleri ###

""""
x = 10 
print(type(x))

x = "10"
print(type(x))

# Castin: veri tipi donusumu

x = "25"
print(type(int(x)))
print(type(float(x)))

x = 35
print(type(str(x)))

number = input("Enter a number: ")
print(number)

print(type(number))

## ERROR: print(int("abc")) 

"""
### 2.7 Listeler ###
"""
numbers = [1, 2, 3, 4, 5, 6]
names = ["Kaan", "Can", "Ucanble", "Yilmaz"]
mixed = ["Kaan", 1, "Can", "ucanble", 55, 65.5]

print(mixed)

fruits = ["elma", "muz", "kivi"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(len(fruits))

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
print(numbers[0:3])
print(numbers[:3])
print(numbers[2:])

numbers = [1, 2,3,4 ]
numbers.append(4)
print(numbers)
numbers.insert(4,100)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.pop(3))
print(numbers)

"""

### 2.8 Tuple ###
"""coordinate = (10, 20)
colors = ("red", "blue", "green")

list = [1,2,3]
list[0] = 99
print(list)

tup = (1, 2, 3)
t = (10, 20, 30)
print(t[1])
print(t[-1])

t = (10, 20, 30, 40)
print(t[1:3])

x = (5)
print(type(x))

x = (5,)
print(type(x))

coordinate = (10, 20)
x, y  = 10, 20
print(x)
print(y)

t = (20, 20, 30, 40)
print(t.count(20))
print(t.index(30))
print(t[-1])

"""

### 2.9 Dictionary ###

"""
student = {
    "isim": "ali",
    "age": 25,
    "department": "Computer"
}
print(student)
print(student["isim"])
print(student["age"])
print(student["department"])

student["grade"] = 85

print(student)

student["age"] = 26
print(student)
del student["department"]
print(student)

print(student.keys())
print(student.values())
print(student.items())

"""

### 2.10 Set ###

"""
maalesef ki yanlislikla kodlarin hepsini sildim ve aklimda kaldigi kadariyla yazdim am atest etmedim. :(

I removed all the code in this part by mistake. But  :(

numbers = {1, 2, 3, 4, 4, 5}
print(numbers)

list = {1, 2, 3, 3}
numbers = set(list)
print(numbers)

numbers.add(5)
print(numbers)
numbers.remove(3)
print(numbers)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
 
"""