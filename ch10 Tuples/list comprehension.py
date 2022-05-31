c={'a':10, 'b':1 ,'c':22}

# lst=list()
# for k,v in counts.items():
#     newtup = (v,k)
#     lst.append(newtup)
#line 3-6 is equal to line 9

lst=sorted( [ (v,k) for k,v in c.items() ] )
print(lst)