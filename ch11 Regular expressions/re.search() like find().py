import re

hand = open("D:\VS Code\Python(from Cousera)\ch11 Regular expressions\mbox-short.txt")

for l in hand:
    l=l.rstrip()
    if re.search('From:',l):
        print(l)