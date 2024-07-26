def freqcount(mylist,mydt):
    for i in mylist:
        if i not in mydt:
            mydt[i]=1
        else:
            mydt[i] += 1
    return mydt


mylist=[10,20,10,30,10,20,30,10,40,10,40]
mydt={}
freqcount(mylist,mydt)
print(mydt)
