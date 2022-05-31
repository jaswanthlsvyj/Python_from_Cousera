import math
a=[1, 2, 3, 4, 5, 6, 7, 5, 90, 5, 43, 65, 23, 65, 76, 8, 74, 245, 234, 67, 687, 974, 3456, 735, 47, 543, 566]

max = 0
for i in a:
    if (i > max):
        max = i
print('The largest num in array :', max)

#or

a.sort()
print('The largest num by using sort fun :',a[len(a)-1])
