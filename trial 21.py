Str='CBSE Digital India'
for i in range(len(Str)-1,0,-1):
    if Str[i].isupper():
        print(Str[i].lower(),end='')
    elif i%2==0:
        if Str[i].islower():
            print(Str[i].upper(),end='')
        else:
            print('@',end='')
