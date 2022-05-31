import re
hand = open('D:\VS Code\Python(from Cousera)\ch11 Regular expressions\mbox-short.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)

print("max:",max(numlist))