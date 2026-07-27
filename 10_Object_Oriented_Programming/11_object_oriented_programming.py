################################################################################

### 11.1 What is Class ### 

### 11.2 init ###
"""
class Student:

    def __init__(self, name, age):
        print(f"New students \nName:  {name} \nage: {age}")

student = Student("Ali", 21)
"""

### 11.3 Attributes and Method ###
"""class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
         


student1 = Student("Ali", 21)

print(student1.name)
print(student1.age)

# Method

class Ogrenci:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hello my name is {self.name}")

student1 = Ogrenci("Ali", 21)
student2 = Ogrenci("Kaan", 25)

student1.intro()
student2.intro()
"""

### 11.3 Object and Class ###
"""
class Book:

    def __init__(self, name, author, page):
        self.name =name
        self.author = author
        self.page = page

    def give_info(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Number of page: {self.page}")

book = Book("Python Programming", "Kaan", 500)

print(book.name)
print(book.author)
print(book.page)

book.give_info()

book1 = Book("Python Programming", "Kaan", 500)
book2 = Book("Introduction Python Programming", "Can", 150)
book3 = Book("Python ", "Kaan", 250)
"""
