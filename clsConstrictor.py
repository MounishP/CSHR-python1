class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"my name is {self.name} and age is {self.age}")
    # name, age


person1 = Person("Mounish", 28)
person2 = Person("Tarun", 25)
person1.details()
person2.details()
