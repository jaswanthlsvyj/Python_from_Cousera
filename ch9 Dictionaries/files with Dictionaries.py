counts=dict()

file = input("enter file name:")
f=open(file)

for l in f:
    l=l.rstrip()
    words = l.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

print("Counts ",counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word

print(bigword,bigcount)