fruit = 'banana'
letter=fruit[1]
print(letter)
x=3
w=fruit[x-1]
print(w)

zot='abc'
# print(zot[5]) gives Traceback Error: index out of range

print(len(zot)) # len() is a function to count the lenght of the string

# Looping through string
fruit='banana'
index = 0
'''
while index<len(fruit) :
    letter = fruit[index]
    print(index,letter)
    index=index+1
        ( OR )
'''
for letter in fruit:
    print(letter)