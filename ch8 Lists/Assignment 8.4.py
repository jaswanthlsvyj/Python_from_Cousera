fname = input("Enter file name: ")
# use file : romeo.txt
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    word=line.split()
    for i in word:
        lst.append(i)
    
lst=list(set(lst))
lst.sort()
print(lst)
