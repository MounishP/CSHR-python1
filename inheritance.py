# Parent class
class Parent:
    def __init__(self, address, bedrooms, bathrooms):
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def describe_house(self):
        print(f"The house consists of {self.bedrooms} bedrooms and {self.bathrooms} bathroom"
              f"in {self.address}")

    def car_parking(self, hasParking):
        if hasParking:
            print("The house has a garage for parking")
        else:
            print("There is no dedicated parking place")


# Child class inheriting from Parent class
class Child(Parent):
    def __init__(self, address, bedrooms, bathrooms, bikeParking):
        # Calling the constructor of the parent class
        super().__init__(address, bedrooms, bathrooms)
        self.bikeParking = bikeParking

    def bike_parking(self):
        if self.bikeParking:
            print("Bike parking is available")
        else:
            print("Bike parking is not available")


p = Parent("hyderabad", 3, 3)

# create an instance of the child class
c = Child("address", 3, 3, True)

c.describe_house()
