#List manipulation
letters=["a","b","c","d","e"]

# len() to count no.of items in list
print(len(letters))

#use ,append() to add new item into list
#syn = yourlist.append(newitem)
letters.append("f")
print(letters)

#.pop(item_index) to remove item from list
letters.pop(3)
print(letters)

#you can store items popped out of list
popped_item=letters.pop()
print(popped_item)
print(letters)