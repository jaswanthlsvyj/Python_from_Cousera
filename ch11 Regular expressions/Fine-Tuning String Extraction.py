import re

x='From stephen.marquard@uct.ac.za sat jan 5 09:14:16 2008'

y=re.findall('\S+@\S+',x)
# \S   matches non-whitespaces
# +    repeats a char 1 - more times
print('1st',y)

y=re.findall('\S+@\S+?',x)
#+?   repeats a char 1 - more times(non-greedy)
print('2nd',y)

y=re.findall('^From (\S+?@\S+)',x)
print('3rd',y)

y=re.findall('@([^ ]*)',x)
print('4th',y)