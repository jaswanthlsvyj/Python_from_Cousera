l = list(range(1,101))
a=1
b=0
l = [l[i] for i in range(len(l)) if i % 2 == 0]
print(l)
while a!=7:
    a+=1
    if(b != 2):
        l = [l[i] for i in range(len(l)) if i % 2 == 0]
        b+=1
        print(l)
        continue

    elif (b==2):
        l = [l[i] for i in range(len(l)) if i % 2 != 0]
        b=0
        print(l)
        continue
    


