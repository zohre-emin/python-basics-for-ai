######################################################################

### 5.1 File openning and Reading ### 

"""
file = open("example.txt", "r", encoding = "utf-8")
content = file.read()
print(content)
file.close()

file = open("example.txt", "r", encoding = "utf-8")

for line in file:
    print(line.strip())
file.close()
"""

### 5.2 File Processing ###
"""
file = open("example.txt", "r", encoding = "utf-8")
content = file.read()
file.close()
print(content)

new_content = content.upper()
print(f"new content: \n{new_content}")

file = open("example.txt", "r", encoding = "utf-8")
lines = file.readlines()
file.close

print(f"Number of Lines: {len(lines)}")
print(lines)
"""

### 5.3 Writing ti Files ###
"""
file = open("example.txt", "w", encoding = "utf-8")
file.write("We are learning python\n")
file.write("Hello World")
file.close()

file = open("example.txt", "r", encoding = "utf-8")
content = file.read()
file.close()

new_content = content.upper()

file = open("new_example.txt", "w", encoding = "utf-8")
file.write(new_content)
file.close()
"""

### 5.4 with Statemant ###
"""file = open("example.txt", "r", encoding = "utf-8")
content = file.read()
file.close()

new_content = content.upper()

file = open("example.txt", "w", encoding = "utf-8")
file.write(new_content)
file.close()

with open("example.txt", "r", encoding = "utf-8") as file:
    content = file.read()
    print(content)

with open("with_write_file", "w", encoding="utf-8") as file:
    file.write(" ofjfhslfjjdhjbcgfulkbgy")
"""
