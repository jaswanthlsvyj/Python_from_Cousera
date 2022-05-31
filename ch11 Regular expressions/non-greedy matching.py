import re

x='From: Using the : character'

y=re.findall('^F.+?:',x)
# +?   repeats a char 1 - more times(non-greedy)
# .    matches any character
# ^    matches beginning of line

print(y)