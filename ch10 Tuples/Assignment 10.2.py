name = input("Enter file:")
# file : mbox-short.txt
if len(name) < 1:
    name = "mbox-short.txt"
f = open(name)

counts=dict()
for l in f:
    l=l.rstrip()
    if not l.startswith('From '): continue
    words=l.split()
    word=words[5]
    h1=word.split(':')
    hr=h1[0]
    counts[hr]=counts.get(hr,0)+1

# lst=sorted( [ (k,v) for k,v in counts.items() ] )
# print(lst)

lst=list()
for k,v in counts.items():
    newtup = (k,v)
    lst.append(newtup)

lst = sorted(lst)

for k,v in lst:
    print(k,v)
