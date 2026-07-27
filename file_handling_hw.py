with open("notla.txt", "w", encoding = "utf-8") as file:
    file.write("90\n")
    file.write("98\n")
    file.write("87\n")
    file.write("76\n")
    file.write("65")

grades = []

file = open("notla.txt", "r")
for line in file:
    grades.append(int(line.strip()))
    
print(grades)
    
avarage = sum(grades) / len(grades)
max_grade = max(grades)
min_grades = min(grades)

print(f"avaeage grade: {avarage}")
print(f"highest grade: {max_grade}")
print(f"lowest grade: {min_grades}")

with open("sonuclar.txt", "w") as file:
    if avarage > 50: 
        file.write("pass")
    else:
        file.write("Failed")
