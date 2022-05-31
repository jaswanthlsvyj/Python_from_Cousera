'''
get method : the pattern of checking to see if a key is already
in a dictionary and assuming a default value if the key is not
there is so common that there is a method called get() 
'''

#Default value if key does not exist(and no traceback)

counts = dict()
names=['csev','cewn','csev','zqian','cewn']

for name in names:
    counts[name]=counts.get(name,0)+1

print(counts)