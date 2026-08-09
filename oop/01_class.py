# object oriented programing system
# class : a blueprint for creating objects

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

my_student = Student("John", 20)
print(my_student.name)  # Output: John
print(my_student.age)   # Output: 20
my_student.display()  # Output: Name: John, Age: 20

# Creating multiple objects of the same class
student2 = Student("Alice", 22)
student2.display()  # Output: Name: Alice, Age: 22

student3 = Student("Bob", 21)
student3.display()  # Output: Name: Bob, Age: 21