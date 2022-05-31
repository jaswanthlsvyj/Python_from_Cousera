#sets 
#removes dulicate items 
eg_set = {"a","b","c","d","a","b"}
print(eg_set)

eg_list=[1,2,3,7,3,4,5,2,6,7]
print(set(eg_list)) #conver list to set

print(len(eg_set))

#adding item into set
# set_name.add(item)
eg_set.add("g")
print(eg_set)

#set_name.remove(item) is used to remove item from set
eg_set.remove("b")
print(eg_set)

eg_set2={"c","s","a"}
print(eg_set & eg_set2) #gives common elements of 2 sets

print(eg_set - eg_set2) #gives differ elements of 2 sets
