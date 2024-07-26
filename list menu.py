l = []
while True:
  print("""
           1. Enter roll numbers of students as they enter the hall (one student at a time). While entry:
              a. Only valid roll numbers should be allowed
              b. No duplicate roll numbers should be allowed
           2. Delete the roll number of any student who leaves the hall
           3. Display the number of students present in the hall at any moment
           4. Display the smallest and the largest roll number present in the hall
           5. Display a list of absentees roll numbers
           6. Display a sorted list of roll numbers present
           7. Exit
        """)
  ch=int(input("Enter your choice: "))
  if ch == 1 :
    a = int(input("Enter the roll number : "))
    if a >= 91041 and a <= 91090 :
      if a in l :
        print("Duplicate roll number found")
      else :
        l.append(a)
    else : 
      print("Invalid roll number")
  elif ch == 2 :
    r_n =  int(input("Enter the roll number - "))
    if r_n in l :
      l.remove(r_n)
    else :
      print("The roll numbewr is absent ")
  elif ch == 3 :
    print(len(l)," Students are present in the hall at this moment")
  elif ch == 4 :
    print(max(l)," is the maximum roll number present in the hall ")
    print(min(l)," is the least roll number present in the hall ")
  elif ch == 5 :
    all_roll_numbers = []
    for i in range(91041,91091,1) :
      all_roll_numbers.append(i)
    for x in l :
      for y in all_roll_numbers :
        if x == y :
          all_roll_numbers.remove(y)
    print("Absentees = ",all_roll_numbers)
  elif ch == 6 :
    print(l.sort())
  elif ch == 7 :
    exit 
  else :
    print("Wrong choice ")
