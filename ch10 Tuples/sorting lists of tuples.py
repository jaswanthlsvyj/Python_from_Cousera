d={'a':10, 'c':1 , 'b':22}
print(d.items())
print (sorted(d.items())) #sorts the list of tuples

#1) sort by Keys
d={'a':10, 'c':1 , 'b':22}
t=sorted(d.items())
for k,v in t:
    print(k,v)

#2) sort by Values
d={'a':10, 'c':1 , 'b':22}
tmp=list()
for k,v in d.items():
    tmp.append((v,k))

print(tmp)
tmp=sorted(tmp, reverse=True) #high to low
print(tmp)
