str = input("Enter the string - ")
vowel = 0
count = 0
for i in str :
    if i in "AEIOUaeiou" :
        vowel += 1
    else :
        count += 1
print("Number of Vowels - ",vowel)
print("Number of consonants - ",count)
