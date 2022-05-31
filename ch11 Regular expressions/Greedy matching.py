import re
x='From Using the : character'
y=re.findall('^F.+:',x)

#  ^    matches beginning of line
#  .    matches any character
#  +    repeats a char 1 - more times

print(y)