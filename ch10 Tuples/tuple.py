# tuples
#immutable = cannot be changed

eg_tuple=("a","b","c","d","e")
#print(eg_tuple)
#print(len(eg_tuple))

print(eg_tuple+("f","g","h"))

print(eg_tuple[4])#sciling same as lists
print(eg_tuple[2:4])

#we can change an list to tuple
eg_list=[1,2,3,4,5]
print(tuple(eg_list))

#tuples comparable
print((0,1,234)<(0,56,3))
