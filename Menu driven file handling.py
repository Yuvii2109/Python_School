#Write a menu driven program to read a file and perform the following 3 operations
#1. WAP to read a file line by line and display each word separated by hash
#2. Count the number of lowercase, uppercase, digits, vowels and consonants
#3. Count and display all the lines beginning with 'the' (and display total no of lines as well)
while True :
    print("""
    1. Read a file line by line and display each word separated by hash
    2. Count the number of lowercase, uppercase, digits, vowels and consonants
    3. Count and display all the lines beginning with 'the'
    """)
    ch=int(input('Enter your choice - '))
    f=open('final.txt','r')
    if ch==1:
        data=f.readlines()
        print('File contents - ')
        print(data)
        for i in data:
            print(i.replace(' ','#'))
    elif ch==2:
        l=0
        u=0
        d=0
        v=0
        c=0
        data=f.read()
        print('File contents - ')
        print(data)
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        
        for i in data :
            if i.islower() :
                l += 1
            elif i.isupper() :
                u += 1
            elif i.isdigit() :
                d += 1

        for a in data :
            if a in vowels :
                v += 1
            elif a in consonants :
                c += 1
            
        print('Number of lowercase letters is - ',l)
        print('Number of uppercase letters is - ',u)
        print('Number of digits is - ',d)
        print('Number of vowels - ',v)
        print('Number of consonants - ',c)
    elif ch==3:
           a=0
           data=f.readlines()
           print('File contents - ')
           print(data)
           for i in data:
               if i[0] == "the":
                  a=a+1
           print("Number of lines beginning with 'the' - " ,a)
    else:
           print('Sahi option bhar le nalayak')



 
