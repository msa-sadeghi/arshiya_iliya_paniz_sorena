class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")         

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
  
    def exam(self):
        print(f"{self.name}'s quiz was so good")

s1 = Student("roze", 17, "A")
s2 = Student("artin", 15, "B")
print(s1.name)
print(s2.name)
s1.exam()
s2.exam()
s1.eat()
s2.eat()