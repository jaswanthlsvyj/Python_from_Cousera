fname = input("Enter file name: ")
# use file : mbox-short.txt
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for l in fh:
    l=l.rstrip()
    if not l.startswith('From ') : continue
    word = l.split()
    print(word[1])
    count=count+1

print("There were", count, "lines in the file with From as the first word")
