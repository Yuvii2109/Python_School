Data=['P',20,'R',10,'S',30]
Times =0
Alpha=''
Add=0
for C in range(1,6,2):
    Times=Times+C
    Alpha=Alpha+Data[C-1]+'@'
    Add=Add+Data[C]
print(Times, Add, Alpha)
