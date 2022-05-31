#Basics of OOP - Instance Variables
# a car has model, color, size, fuel type
# fuel capacity

class Car:
    # define the init method
    def __init__(self,x,y,z):
        self.model = x
        self.color = y
        self.fuel_capacity = z
    
    def sayHello(self):
        print("Hello world")
        
    def sayColor(self):
        print("My color is", self.color)
    
    def spendFuel(self, fuelAmount):
        self.fuel_capacity -= fuelAmount
    
new_car = Car("BMW","blue",2000) # (model,color,fuel_capacity)
print(new_car.model)
print(new_car.color)
print(new_car.fuel_capacity)
new_car.spendFuel(1000)
print(new_car.fuel_capacity)
