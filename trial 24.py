s=input("Enter a String - ")
a=d=0
for j in range(len(s)):
    if s[j].isalpha():
        a+=1
    elif s[j].isdigit():
        d+=1
print("Total Number of letters in this String - ", a)
print("Total Number of Digits in this String - ", d)
