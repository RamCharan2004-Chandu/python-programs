class Student:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hi, I am {self.name}")
s = Student("Charan")
s.greet()