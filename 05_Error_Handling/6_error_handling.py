#######################################################################

### 6.1 Error types ###

"""
if 5 > 3:  # if ':' is missing, Syntax error
    print("ok") #  if 'ok would not be defined, Name error

# Nmae error (Undefined veraible)
# Type error (Mismatching veraible types) : print("10" + 5)
# Value erro (Value is not matching): int("Kaan")
# zero division error: print(10/0)
#index error: list = [1, 2, 3, 4] print(list[10])
# Key error: in dictionaries
# file not found: when file name is not correct
# Attribute Eror: sayi = 10  sayi.append(20)
            
"""            

### 6.2 Try Except Else Finally ###
"""

# method to run the program without error massage
try:
    number = int(input("enter a number: "))
    print(10/number)
except:
    print("There is an error")

print("Program continues to run without giving any error")

# method to catch an error 
try:
    number = int(input("Enter a number: "))
    print(10/number)
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Cannot be divided by zero")

# else: works when there is no error

try:
    number = int(input("Enter a number: "))
    result = 10/number
except (ValueError, ZeroDivisionError):
    print("Wrong value entered.")
else:
    print(f"Result: {result}")

# finally: program runs in any case


try:
    file = open("data.txt", "r", encoding = "utf-8")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File cannot be found")
finally:
    try: 
        file.close()
    except:
        pass

# 
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Aage cannot be nagative.")

try:
    number = int(input("Enter a unmber: "))
    print(10/number)
except Exception as e:
    print(f"Error: {str(e)}")
    
"""
