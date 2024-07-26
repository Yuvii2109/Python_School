def evenodd(list) :
    for i in range (len(list)) :
        if list[i]%2 == 0 :
            list[i] //= 2
        else :
            list[i] *= 2



list = [2,24,5,6,7,11,55]
evenodd(list)
print("Final list is - ",list)
