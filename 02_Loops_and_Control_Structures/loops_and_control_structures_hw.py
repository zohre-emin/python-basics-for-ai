##################################################

### Answer 1 ###
"""
number = int(input("Enter a number: "))
if number == 0:
    print("You entered zero.")
elif number > 0:
    print(f"The {number} you entered is a positive number.")
else:
    print(f"The {number} you entered id a negative number.")

"""

### Anawer 2 ###
"""
sum = 0 

for i in range(11):
    print(i)
    sum+=i
print(sum)           

"""

### Answer 3 ###
"""
answer = ""
while answer != 'q':
    answer = input("Enter q to quit from the program: ")
    if answer != 'q':
        print(f"Your answer: {answer}.")

print("Quit succesfully.")

"""
    
### Answer 4 ###
"""
for i in range(1, 21):
    if i < 10:
        if i % 2 ==0:
            print(f"{i} is an even number. Smaller then ten.")
        else: 
            print(f"{i} is an odd number. Smaller then ten.")
    else:
        if i % 2 ==0:
            print(f"{i} is an even number. Greater then ten.")
        else: 
            print(f"{i} is an odd number. Greater then ten.")
            
"""

