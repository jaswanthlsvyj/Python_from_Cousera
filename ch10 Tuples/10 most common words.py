fhand= input('Enter the file name:')
f = open(fhand)

counts=dict()
for line in f:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val,key in lst[:10]:
    print(key,val)
