#OOP   Object Oriented Programming    برنامه نویسی شی گرا
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def walk(self):
        print(f"{self.name} is walking...")  
class Student(Person)    :
    def __init__(self, n, a, stu_code):
        super().__init__(n, a)
        self.code = stu_code
    def learn(self):
        print(f"{self.name} is learning...")
class Teacher(Person)    :
    def __init__(self, n, a, exp):
        super().__init__(n, a)
        self.experience = exp
    def teaching(self):
        print(f"{self.name} is teaching...")
s1 = Student("paniz",12, 12345)
s2 = Student("abtin", 12, 67843)
s1.walk()
s2.walk()
t1 = Teacher("msa", 37, 15)
t1.walk()
t1.teaching()
s1.learn()
