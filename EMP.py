#write a menu driven program to read a file and perform the following 3 operations
#1.wap to read a file line by line and display each word separated by hash
#2.count the number of lowercase, uppercase, digits, vowels and consonants
#3. count and display all the lines beginning with 'the' (and display total no of lines as well)
while True :
    print("""
    1. read a file line by line and display each word separated by hash
    2. count the number of lowercase, uppercase, digits, vowels and consonants
    3. count and display all the lines beginning with 'the'
    """)
    ch=int(input('Enter your choice - '))
    f=open('final.txt','r')
    data=f.readlines()
    print('file contents')
    print(data)
    if ch==1:
        for i in data:
            print(i.replace(' ','#'))
    elif ch==2:
        l=0
        u=0
        d=0
        v=0
        c=0
        for i in data:
            if i.islower():
                l=l+1
            elif i.isupper():
                u=u+1
            elif i.isdigit():
                d=d+1
            elif i in 'aeiou':
                v=v+1
            else :
                c=c+1
        print('Number of lowercase letters is - ',l)
        print('Number of uppercase letters is - ',u)
        print('Number of digits is - ',d)
        print('Number of vowels - ',v)
        print('Number of consonants - ',c)
    elif ch==3:
           a=0
           for i in data:
               if i[0] == "the":
                  a=a+1
           print("Number of lines beginning with 'the' - " ,a)
    else:
           print('wrong choice')



 
