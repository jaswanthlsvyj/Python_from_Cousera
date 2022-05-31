import re
x='My 2 favorite numbers are 19 and 42'

y=re.findall('[0-9]+',x)
#[a-z0-9]    The set of chae can include a range
# +    repeats a char 1 - more times

print(y)