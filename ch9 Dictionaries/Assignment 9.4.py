name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

counts = dict()

for l in fh:
    l=l.rstrip()
    if not l.startswith('From ') : continue
        
    word = l.split()
    #print(word[1])
    #count=count+1
    words=word[1]
    #print(words)
    counts[words]=counts.get(words,0)+1
       
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word

print(bigword,bigcount)
