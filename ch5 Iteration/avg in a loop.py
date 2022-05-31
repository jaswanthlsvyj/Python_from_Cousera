count = 0
sum = 0
print('Before', count, sum)
for i in [9, 41, 23, 45, 56, 7, 5, 34, 6, 56, 4]:
    count = count + 1
    sum = sum+i
    print(count, sum, i)
print('After', count, sum, sum/count)
