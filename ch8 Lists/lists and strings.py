abc='With three        words'
stuff=abc.split() #split breaks a string into parts and produce a list of strings
print(stuff)
print(len(stuff))

line = 'first;second;third'
num = line.split(';')
print(num)

#The Double split pattern
l1= 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = l1.split()
email=words[1]
# print(email)

pleces =email.split('@')
print(pleces)