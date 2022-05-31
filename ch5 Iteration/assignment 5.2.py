largest = None
smallest = None
l = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        l.append(num)  # adding the element

    except:
        print('Invalid input')

n = len(l)
for i in l:
    if largest is None:
        largest = i
    elif largest < i:
        largest = i

    if smallest is None:
        smallest = i
    elif smallest > i:
        smallest = i

print("Maximum is", largest)
print("Minimum is", smallest)
