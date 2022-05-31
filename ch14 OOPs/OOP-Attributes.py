# Basics of OOP - Attributes

# a car has model,color,size,fuel,fuel capacity
class Car:
    # define the init method
    def __init__(self):
        self.model="Tesla"
        self.color="black"
        self.size=1000
        self.fuel="Electric"
        self.fuel_capacity=1000
        
        
new_car = Car()
print(type(new_car))

print(new_car.model)
print(new_car.color)
print(new_car.size)
