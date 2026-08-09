class Student:
    school = "ABC School"       # Class variable

    def __init__(self, name, age):
        self.name = name        # Instance variable
        self.age = age          # Instance variable

    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def greet():
        return "Hello, welcome to the school!"

    
student1 = Student("John", 20)
# print(Student.name)     
print(Student.school)  
print(Student.add(5, 3)) 
print(Student.greet())  