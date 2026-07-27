#####################################################

### 10.1 Introduction to Matplotlib ###
import matplotlib.pyplot as plt

### 10.2 Line Plot ###

"""
days = [1, 2,3, 4, 5]
temp = [22, 24, 23, 25, 27]

plt.plot(days, temp, color = "red", linestyle = "--", marker = "o")
plt.title("Temperatures of Days")
plt.xlabel("Days")
plt.ylabel("Tamperature")
plt.grid(True)
plt.show()
"""
### 10.3 Bar Chart ###

"""
students = ["ali","ayse", "mehmet", "zeynep"]
grades = [70, 85, 60, 90]

colors = ["red", "blue", "green", "purple"]
plt.bar(students, grades, color = colors)
plt.title("Grades of Students")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.show()

# Horizontal bar chart
plt.barh(students, grades)
plt.show()
"""

### 10.4 Pie Chart ###
"""
a = [0.1, 0, 0, 0]
names = ["python", "java", "c++", "javascript"]
values = [40, 25, 20, 15]
c = ["red", "blue", "pink", "purple"]
plt.pie(values, labels = names,explode = a, autopct="%1.1f%%", colors = c)
plt.title("Programming Languages")
plt.show()
"""

### 10.5 Scatter Plot ### 
"""
working_hours = [1, 2, 3, 4, 5, 6]
grades = [50, 55, 60, 70, 80, 90]

plt.scatter(working_hours, grades, color = "red", s = 100)
plt.title("Working Hours and Grades")
plt.xlabel("Hours")
plt.ylabel("Grades")
plt.show()


x1 = [1, 2,3, 4]
y1 = [50, 60, 70, 80]

x2 = [1, 2, 3, 4]
y2 = [55,65, 75, 85]

plt.scatter(x1, y1, color = "blue",label = "science")
plt.scatter(x2, y2, color = "red", label = "Math")
plt.legend()
plt. show()
"""

### 10.6 Subplots ###
"""
x = [1, 2, 3,4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Graph")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Graph 2")

plt.show()

# Subplots by different charts

x = [1, 2, 3,4]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

plt.show()

# 2x2 Graphs 

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Graph 1")

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Graph 2")

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Graph 3")

plt.subplot(2, 2, 4)
plt.pie(y)
plt.title("Graph 4")

plt.show()
"""