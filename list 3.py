Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,3]
>>> list2 = list1
>>> list1.append(10)
>>> list1
[1, 2, 3, 10]
>>> list2
[1, 2, 3, 10]
>>> list1 = [1,2,3,4,5]
>>> list2 = list1[:]
>>> list2
[1, 2, 3, 4, 5]
>>> list1 = [1,2,3,4]
>>> list2 = list(list1)
>>> list2
[1, 2, 3, 4]
>>> import copy
>>> list1 = [1,2,3,4,5]
>>> list2 = copy.copy(list1)
>>> list2
[1, 2, 3, 4, 5]
>>> 
=================================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/append function.py ==================================
[1, 2, 3, 4, 55]
>>> l1 = [1,2,3,4]
>>> l1.append([5,6])
>>> l1
[1, 2, 3, 4, [5, 6]]
>>> 
>>> 
>>> color = ['red','green','blue']
>>> color.append('white')
>>> print(color)
['red', 'green', 'blue', 'white']
>>> 
=================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py ===================
Enter the number of elements in a list - 
Enter the number of elements in a list -5
Traceback (most recent call last):
  File "C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py", line 3, in <module>
    N = int(input())
ValueError: invalid literal for int() with base 10: 'Enter the number of elements in a list -5'
>>> 
=================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py ===================
Enter the number of elements in a list - 
Enter the number of elements in a list -5
Traceback (most recent call last):
  File "C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py", line 3, in <module>
    N = int(input())
ValueError: invalid literal for int() with base 10: 'Enter the number of elements in a list -5'
>>> 
=================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py ===================
Enter the number of elements in a list - 

Traceback (most recent call last):
  File "C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py", line 3, in <module>
    N = int(input())
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py ===================
Enter the number of elements in a list - 
5
Enter list value - 
3
Enter list value - 
4
Enter list value - 
5
Enter list value - 
6
Enter list value - 
7
The original list is -  3 4 5 6 7 
The second largest element in the list is -  6
>>> 
=================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py ===================
Enter the number of elements in a list - 
10
Enter list value - 
3
Enter list value - 
4
Enter list value - 
5
Enter list value - 
6
Enter list value - 
7
Enter list value - 
9
Enter list value - 
5
Enter list value - 
2
Enter list value - 
4
Enter list value - 
5
The original list is -  3 4 5 6 7 9 5 2 4 5 
The second largest element in the list is -  7
>>> 
=================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/to find the second largest element in the list.py ===================
Enter the number of elements in a list - 
40
Enter list value - 
234
Enter list value - 
3
Enter list value - 
54
Enter list value - 
54
Enter list value - 
43
Enter list value - 
32
Enter list value - 
32
Enter list value - 
4
Enter list value - 
6567
Enter list value - 
6
Enter list value - 
876
Enter list value - 
65
Enter list value - 
45
Enter list value - 
33
Enter list value - 
23
Enter list value - 
2
Enter list value - 
545
Enter list value - 
756
Enter list value - 
74
Enter list value - 
34
Enter list value - 
23
Enter list value - 
43
Enter list value - 
66
Enter list value - 
73
Enter list value - 
523
Enter list value - 
5
Enter list value - 
456
Enter list value - 
566
Enter list value - 
35
Enter list value - 
34
Enter list value - 
66
Enter list value - 
74
Enter list value - 
55
Enter list value - 
34
Enter list value - 
32
Enter list value - 
5646
Enter list value - 
756
Enter list value - 
643
Enter list value - 
42
Enter list value - 
43
The original list is -  234 3 54 54 43 32 32 4 6567 6 876 65 45 33 236 2 545 756 74 47 23 43 66 573 523 5 56 566 
35 34 66 746 55 34 32 5646 56 643 42 43 
The second largest element in the list is -  5646
7
>>> 
>>> 435
5
5
>>> 