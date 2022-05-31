'''
    *handle = open(filename, mode) 
    *filename is a basestring
    *mode is optional, 'r':read  and  'w':write
    *eg = open('mbox.txt','r')
    
    * special character : \n  as newline 
'''

xfile = open('mbox.txt')
# reading a file =>
for word in xfile:
    print(word)

#skipping with Continue 
for line in xfile:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
    
#using 'in' to select lines
for l in xfile:
    l=l.rstrip()
    if not '@uct.ac.za' in l:
        continue
    print(l)
    
#Prompt for file name 
count=0
for a in xfile:
    if a.startswith('Subject:'):
        count=count+1 

print('There were',count,'subject lines in',xfile)

