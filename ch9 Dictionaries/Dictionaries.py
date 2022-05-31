#dictionaries
# {key: value}
#dictionaries can store diff datatypes at a time

john = {"name":"John Smith",
        "age":18}
print(john)

john["country"]="Singapore" # adding a key/value to dictionary
print(john)

#we can retrieve the value using the key
print(john['name']) #prints John Smith

#we can see keys in the dictionaries
print(john.keys())

#we can see values in the dictionaries
print(john.values())

john['haskids']=True
john['favcolors']=['black','white','red']
print(john)


