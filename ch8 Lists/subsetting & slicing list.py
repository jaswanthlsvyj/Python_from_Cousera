# Subsetting & Slicing Lists

letters = ["a", "b", "c", "d", "e"]
#print(letters)

#["a","b","c","d","e"]
#  0   1   2   3   4
#  -5  -4  -3  -2  -1

# subset[start:end+1:steps]
print(letters[0:3:1])

print(letters[::-1])  # prints in reverse order

print(letters[1:])  # prints every thing from b to end
print(letters[-4:])
