

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"my name is {self.name} and age is {self.age}")

    # name, age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print("Name must a string")


person1 = Person("Mounish", 28)
person2 = Person("Tarun", 25)
# person1.details()
# person2.details()
print(person1.get_name())
person1.set_name(765)
print(person1.get_name())
