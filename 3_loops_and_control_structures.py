
### 3.1 If else ###
"""
number = 10 
if number > 0:
    print("Number is positive")

number = -3

if number >0:
    print("positive")
else:
    print("Negative")

grade = 72

if grade > 85:
    print("A")
elif grade > 70:
    print("B")
elif grade > 50:
    print("C")
else:
    print("F")

age = 20 

student = True

if age < 25 and student == True:
    print("Student discount applied")

if age < 25 or student == True:
    print("Student discount applied")

fruits = ['elma', "armut", "muz"]

a = "elma"
if a in fruits:
    print(f"{a} is in the list")
else:
    print(f"{a} is out of list")

product = input("Enter a fruit name: ")

if product in fruits:
    print(f"{product} is in the stock.")
else: 
    print(f"{product} is out of stock.")
"""

### 3.2 For Loop ###
"""
numbers = [10, 20, 30, 40]

for num in numbers:
     print(num + 5)

for i in range(5):
    print(i)
    #print()

print()

for i in range(1, 7):
    print(i)
    #print()

sum = 0
for a in numbers:
    print(a)
    sum = sum + a
print(sum)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numbers:
    if n % 2 == 0:
        print(f"{n} is even number.")
    else:
        print(f"{n} is odd number.")

word = "ucanble"

for L in word: 
    print(L)
"""

### 3.3 while Loop ###
"""
i = 0 
while i < 5:
    print(i)
    i = i + 1
print(f"i: {i}")

count = 0 
while count <=5:
    print("Hello")
    count+=1

i = 0 
while i <= 10:
    if i % 2 ==0:
        print(f"{i} is even number")
    else:
            print(f"{i} is odd number")
    i += 1
print(f"i: {i}")

answer = ""
while answer != "q":
    answer = input("Enter q to quit from the program: ")
    print(f"Your Answer: {answer}")
"""

### 3.4 break, continue, Pass and Nested Loops ###
"""
for i in range(10):    
    print(i)

for i in range(10):
    if i == 9:
        break
    print(i)
print(f"i: {i}")   

for i in range(10):
    if i ==5:
        continue
    print(i)

if True:
    pass

print("dhckjehfjh")

for i in range(10):
    if i ==1:
        pass
    print(i)

for i in range(5):
    if i % 2 == 0:
        print(i)

age = 20
student = True

if age < 25:
    if student:
        print("Student discount")

for i in range(3):
    for j in range(2):
        print(f"i: {i}", f"j: {j}")

"""