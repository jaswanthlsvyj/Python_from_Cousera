# OOP :

''' 
1)Programming paradigm or school of thought that relies on idea of classes
  and objects
2)CLASSES : abstract blueprints that define behavior and properties of objects
3) Objects : the things that are created based on classes
'''
''' 
Class::Defines the attributes and methods
Attribute::Properties that a class will have
Methods:: code that you can execute for the object.i.e,behavior of the created object
'''
# In programing , every class is derived from "object" class

from turtle import color


class Bottle():
  # company name
  companyName = "Saypa"

  # constructor
  def __init__(self,color, capacity):
    self._color = color
    self.capacity = capacity

  # functions/behavior
  def wash(self):
    print('washing',self._color)

  def setCap(self):
    print('Setting capacity')

  def fillWater(self):
    print('fill water')

  # destructor
  # def __del__ (self):
  #   print('destructor')

# object creation
print(Bottle.companyName)
bottle1 = Bottle("green",5)
print(bottle1)
print(bottle1.capacity)
bottle1.wash()

bottle2 = Bottle('red', 2)
print(bottle2._color,bottle2.capacity)

print("\n====== Child class creation ======")

# ======By using inheritance======
# single ingeritance
class CopperBottle(Bottle): #Bottle is inherited to CopperBottle
  
  # we can create own constructor for the child class 
  # def __init__(self):
  #   print('child constructor')
  
  # we can pass the values to parent constructor too from child
  def __init__(self, color, capacity):
    # Bottle.__init__(self,color, capacity) or
    super().__init__(color, capacity)

  def morningWater(self):
    print("morning water")

# object creation for child class
print(CopperBottle.companyName)
Copper1= CopperBottle("blue",6)
Copper1.setCap()

Copper2 = CopperBottle("yello",1)
Copper2.fillWater()

print("\n======knowing the parent of class======")
# how to know the parent of any class?
# use : calass.__bases__
print(Bottle.__bases__)
print(CopperBottle.__bases__)

# how to know the parent of the class from an object?
print(CopperBottle.__class__.__bases__)


# ===== Types of inheritance =====

print("\n===== Multilevel inheritance =====")
class Class1:
  def join(self):
    print('joined')

class Class2(Class1):
  def subscribe(self):
    print('Subscribe')

class Class3(Class2):
  def comment(self):
    print('commented')

cl3 = Class3()
cl3.subscribe()
cl3.join()
cl3.comment()

"===== Hierarchical inheritance ====="
# Multiple classes derived from a single parent/base class


"===== Encapsulation ======"
# Process of wrapping code and data together into a single unit
#Access modifiers: 
# 1) Public     : dont give any undrscores for variables
# 2) Protected  : use one underscore i.e _varibles
# 3) Private    : use 2 underscores i.e __variables

" ===== Polymorphism ===== "
#  Same name but differnt forms/functionalities
# Types : 
# 1) Method overloading : python does not support it
# 2) Method overriding  : if sub class/child class has the same method as declared in the parent class
