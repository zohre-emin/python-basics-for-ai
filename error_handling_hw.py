#######################################################################################

### my answer ###

"""

file = open("veri.txt", "w", encoding = "utf-8")
file.write("70\n")
file.write("85\n")
file.write("abc\n")
file.write("90\n")
file.write("50\n")
file.write("hata\n")
file.write("60")

data = []
file = open("veri.txt", "r", encoding = "utf-8")
for line in file:
    try:       
        data.append(int(line.strip()))
    except ValueError:
        print(f"wrong value: {line.strip()}")
   
print(data)
"""
    
### instructions answer ### 
"""

grades = []

number_of_error = 0

with open("veri.txt", "r") as file:
    for line in file:
        try:
            value = int(line.strip())
            grades.append(value)
        except ValueError:
            print(f"Error found: {line.strip()}")
            number_of_error += 1

print(f"grades: {grades}")
print(f"number of error: {number_of_error}")

avarage = sum(grades)/len(grades)

print(f"Avarage grade: {avarage}")
"""