d = {'Student1' : 90 , 'Student2' : 67 , 'Student3' : 88}
L1 = sorted(d , reverse = True)
print(L1)
L2 = dict(sorted(d.items()) , reverse = True)
print(L2)
L3 = sorted(d.values() , reverse = True)
print(L3)
