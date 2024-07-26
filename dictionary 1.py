#Employ dictionary
Emp = {'Ename':['Ritu','Vibhu','Vidoo','Pipu'],
       'Designation':['Mummy','Papa','Chacha','Chachi'],
       'Salary':[1000000,2000000,3000000,4000000]}
print(Emp)
for x,y in Emp.items() :
    print(x,":",y)
Emp['Pipu'] = 'Intern'
for E in Emp :
    print(E,":",Emp[E])
