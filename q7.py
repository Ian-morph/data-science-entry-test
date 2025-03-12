class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, Make, Model, Year):
        self.make = Make
        self.model = Model
        self.year = Year
    def describe_car(self):
        print("Year: ", self.year)
        print("Make: ",  self.make)
        print("Model: ", self.model)
        print(f"{self.year}, {self.make}, {self.model}")

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

car1 = Car( "Toyota", "Corolla", 2020)
car1.describe_car()