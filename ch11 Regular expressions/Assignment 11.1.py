import re

file = open('D:\VS Code\Python(from Cousera)\ch11 Regular expressions\RegexSum1.txt')

lst=list()
for f in file:
    f=f.rstrip()
    y=re.findall("[0-9]+",f)
    for i in y:
        lst.append(int(i))
    

print(sum(lst))
