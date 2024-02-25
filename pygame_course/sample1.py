class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender        
    def eat(self):
        if self.gender == "boy":
            print(f"{self.name} good boy, eatup!!!!")
        else:
            print(f"{self.name} good girl, eatup!!!!")
    def bark(self):
        print(f'{self.name} is barking!!!!')
        
class Beagle(Dog):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.gunshy = True
        
    
    def hunt(self):
        print(f"{self.name} is hunting so good")
        
b1 = Beagle("jessi", 11, "girl")
b1.eat()
b1.bark()
b1.hunt()