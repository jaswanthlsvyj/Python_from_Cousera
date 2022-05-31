# Basics of OOP - Defining a Class

class car:
    #define the init method
    def __init__(self):
        print("A car is created!")
        #pass to not to print
        
newcar = car()
print(type(newcar))
