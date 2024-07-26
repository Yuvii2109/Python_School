#function to count the number of occurences of any character in an inputted string


def countChr(str1,ch) :
    count = 0
    for s in str1 :
        if s == ch :
            count += 1
    return count



msg = input("Enter the string - ").casefold()
ch = input("Enter the character to search - ")
C = countChr(msg,ch)
if C == 0 :
    print("Not found")
else :
    print("Found for ",C," number of times")
