# Basics of OOP - Methods

# a car has model, color, size, fuel type
# fuel capacity

class Car:
    # define the init method
    #syn= def fun_name(parameter): ...
    
    def __init__(self):
        self.model = "Tesla"
        self.color = "black"
        self.size = 1000
        self.fuel_type = "electric"
        self.fuel_capacity = 10000

    def sayHello(self)  :
        print("Hello world")
 
    def sayColor(self)  :
        print("My color is",self.color)    


    def spendFuel(self,fuelAmount)    :
        self.fuel_capacity -= fuelAmount
# 	def spendFuel(self , fuelAmount) :
#         self.fuel_capacity -=fuelAmount  
  
new_car = Car()
#print(new_car.model)
#print(new_car.color)
#print(new_car.size)

new_car.sayHello()
new_car.spendFuel(1000)
print(new_car.fuel_capacity)



