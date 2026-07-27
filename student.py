class Student:
    def __init__(self, roll, name, age, branch):
        self.roll = roll
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print(f"Roll No : {self.roll}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Branch  : {self.branch}")
