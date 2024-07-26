nums=[1,2,7,9,5,7,2,4,5,1,1,2]
for i in range(1,10):
    if i in nums:
        index=nums.index(i)
        c=nums.count(i)
    print(i,'appears in nums',c,'times.',end=' ')
    print('Its first occurence is at index',index)
 
