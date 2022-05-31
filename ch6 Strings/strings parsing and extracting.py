#parsing and extracting

data = 'Form stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#want to slice "uct.ac.za" from the data

atpos = data.find('@')
print("atpos:",atpos)

sppos = data.find(' ',atpos)
print("sppos:",sppos)

host = data[atpos+1 :sppos]
print("host:",host)
