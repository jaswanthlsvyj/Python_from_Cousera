fnd = False
inp = int(input("Enter the number u want to search: "))
print("Before", fnd)
for i in [9, 41, 23, 45, 56, 7, 5, 34, 6, 56, 4]:
    if i == inp:
        fnd = True
    #print(fnd,i)
print('After', fnd)

print(None)  # None is a null form in python
