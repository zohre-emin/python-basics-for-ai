########################################

# Program Overflow 

"""
1. Ask user to enter midterm and final grade
2. Calculate avarage grade
3. Calculate letter grade
4. Print the results to the screen 

"""

### Answer1: self tried answer ###
"""
def grade():
    midterm = int(input("Enter your midterm grade: "))
    final = int(input("ENter your final grade: "))
    avarage = round((midterm + final)/2, 2)
    print(f"Your avarage grade is {avarage}")
    l =""
    if avarage >= 85:
        l = 'A'
    elif avarage >=70:
        l = "B"
    elif avarage >= 60:
        l = "C"
    elif avarage >=50:
        l = "D"
    else:
        l ="F"
    print(f"Your letter grade is {l}")
    
grade()

"""

### Improved code from AI for my answer ###
"""
def grade():
    midterm = float(input("Enter your midterm grade: "))
    final = float(input("Enter your final grade: "))

    average = midterm * 0.4 + final * 0.6

    if average >= 85:
        letter = "A"
    elif average >= 70:
        letter = "B"
    elif average >= 50:
        letter = "C"
    elif average >= 40:
        letter = "D"
    else:
        letter = "F"

    print(f"Your average grade is {average:.2f}")
    print(f"Your letter grade is {letter}")


grade()
"""

### Answer2:  instructions answer ###
"""
def calculate_avarage(midterm: float, final: float) -> float:
    # %40 of midterm, %60 of final 
    midterm = midterm * 0.4
    final = final * 0.6
    avarage = midterm + final 
    return avarage
    pass

def calculate_letter_grade(avarage: float) -> str:
    if avarage>= 85:
        return "A"
    elif avarage >= 70:
        return "B"
    elif avarage >= 50:
        return "C"
    elif avarage >= 40:
        return "D"
    else:
        return "F"
    pass

# program overflow
name = input("Students name: ")
midterm = float(input("Midterm grade: "))
final = float(input("Final grade: "))

avarage = calculate_avarage(midterm = midterm, final = final)
letter = calculate_letter_grade(avarage = avarage)

def print_output(name = name, avarage = avarage, letter = letter):
    print("Result: ")
    print(f"Student: {name}")
    print(f"Avarge: {avarage}")
    print(f"Letter grade: {letter}")
    pass


print_output(name = name, avarage = avarage, letter = letter)

"""

### Improved code from AI for instructions answer ###
"""
def calculate_average(midterm: float, final: float) -> float:
    return midterm * 0.4 + final * 0.6


def calculate_letter_grade(average: float) -> str:
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def print_output(name: str, average: float, letter: str) -> None:
    print("Result:")
    print(f"Student: {name}")
    print(f"Average: {average:.2f}")
    print(f"Letter grade: {letter}")


name = input("Student's name: ")
midterm = float(input("Midterm grade: "))
final = float(input("Final grade: "))

average = calculate_average(midterm, final)
letter = calculate_letter_grade(average)

print_output(name, average, letter)
"""


