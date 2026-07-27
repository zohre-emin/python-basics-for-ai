################################################################

### 4.1 Build in Functions ###
"""
print("Hello")

list = [1, 2, 3]

print(len(list))

x = 3.14
print(type(x))

num = "10"
print(int(num) + 5)

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

x = -8
print(abs(x))

x = 3.417435375878
print(round(x, 3))

numbers = [8, 3, 4, 56, 48,2, 6, 76,9]
print(sorted(numbers))

"""

### 4.2 User Defined Functions ###

""" Docstring """
"""

def greating():
    print("Hello")

greating()

def greating():
    print("Hello I am Ucanbles AI assistant.")

greating()

def greating(name):
    print(f"Hello I am {name}`s AI assistant.")

greating("TR AI Academy")


def greating(name, greating_santace):
    print(name + "`s  " + greating_santace)

greating("Kaan Hoca", "AI assitant greats you.")

def sum(a, b):
    result = a + b
    print(f"result: {result}")
    return result

sum(3, 8)
print(f"reult of the summation is ; {sum(3, 8)}")

def calculate(x, y):
    sum = x + y
    mul = x*y
    sub = abs(x - y)
    dev = round(x/y, 3)
    return sum, mul, sub, dev


calculate_mul = calculate(3, 9)
print(f"Multiplication is : {calculate_mul}")

calculate_sum, calculate_mul, calculate_sub, calculate_dev = calculate(3, 9)
print(f"Summation is: {calculate_sum}")
print(f"Multiplication is : {calculate_mul}")
print(f"Substraction is: {calculate_sub}")
print(f"Devision is: {calculate_dev}")
"""

### 4.3 User Defined Functions 2 ###
"""
def great(name, inf):
    print(f"{name} {inf}")
great("Kaan hocam", "Hello")
great("Arkadaslar", "HI")
great("Ucanble", " HI")

def great(name, inf = "Hello"):
    print(f"{name} {inf}")

great("Kaan hocam")
great("Arkadaslar")
great("Ucanble")

great("Students", "How are you? ")

def great(name, age, job, c, lr, epoch):
    print(name, age, job, c, lr, epoch)
great("Kaan", "35", "engineer", "0.4", "0.001", "1000")

great(name = "Kaan", age = "35", job = "engineer", c = "0.4", lr = "0.001", epoch = "1000")

def sum(a: int, b: int) -> int:
    return a + b
print(sum(3, 4))

# function in function

def square(x):
    s = x **2
    return s
def pr(x):
    print(square(x))
pr(5)

"""

### 4.3 Scope ###

## Local Veriable: defined in function
"""
def test():
    x = 10
    print(f"Inside the function: {x}")
test()

x = 15
def test():
    print(f"Inside the function: {x}")
test()

x = 11
def test():
    x = 5
    print(f"Inside the function: {x}")
test() # 5
# test(x) is not 11 
print(f"Outsideo of the function: {x}")

## Global veraible

x = 9
def test():
    global x
    x = 5 # local -> global

test() # 5
print(x) # 9

"""