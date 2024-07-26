Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/concatenation lists.py
['Red', 'green', 'Blue']
>>> 
= RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/concatenation lists.py
['Red', 'green', 'Blue']
['Learn', 'python', 'Programming']
>>> list1 = ['Red','Green']
>>> list1 = [1,2,3,4]
>>> list2 = [5,6,7,8]
>>> list3 = list1 + list2
>>> print(list3)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 
= RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/Repitition operator.py
[1, 2, 3, 1, 2, 3, 1, 2, 3]
python python python 
>>> DOB = "2004-09-21"
>>> list(DOB)
['2', '0', '0', '4', '-', '0', '9', '-', '2', '1']
>>> x = 'Python'
>>> print('o' in x)
True
>>> print('p' in x)
False
>>> list1 = [1,2,5,10]
>>> print(4 in list1)
False
>>> print(5 in list1)
True
>>> x = ['Apple','Banana','Orange','Grapes']
>>> print('Lichi' not in x)
True
>>> print('Apple' not in x)
False
>>> l1 = [2,5,10,20]
>>> print(4 not in l1)
True
>>> print(5 not in l1)
False
>>> 
========================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/'in' operator used with for loop.py ==========================
Ritu
Saksham
Abha
Varun
>>> 
================================= RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/Indexing operation.py =================================
Blue
Blue
3
3
>>> x = 'Computer'
>>> x[1:4]
'omp'
>>> x[1:6:2]
'opt'
>>> x[3:]
'puter'
>>> x[:5]
'Compu'
>>> x[-1]
'r'
>>> x[-3:]
'ter'
>>> x[:-2]
'Comput'
>>> 
================================== RESTART: C:/Users/YUVRAJ/AppData/Local/Programs/Python/Python38-32/slicing operation.py =================================
[100, 50.75, 'Radhika', 'Shaurya', 900, 897.6]
>>> 
>>> list1 = [100, 50.75, 'Radhika', 'Shaurya', 900, 897.6]
>>> print(list1[2:5])
['Radhika', 'Shaurya', 900]
>>> print(list1[:5])
[100, 50.75, 'Radhika', 'Shaurya', 900]
>>> print(list1[3:])
['Shaurya', 900, 897.6]
>>> print(list1[::2])
[100, 'Radhika', 900]
>>> print(list1[::-2])
[897.6, 'Shaurya', 50.75]
>>> print(list1[-5:-2])
[50.75, 'Radhika', 'Shaurya']
>>> print(list1[5:2:-1])
[897.6, 900, 'Shaurya']
>>> print(list1[-2:-5:-1])
[900, 'Shaurya', 'Radhika']
>>> print(list1[-2:-5:-2])
[900, 'Radhika']
>>> 
>>> list = [24,56,10,99,28,90,20,22,34]
>>> slice = list[3:-3]
>>> slice
[99, 28, 90]
>>> slice[1]
28
>>> slice[1] = 30
>>> slice
[99, 30, 90]
>>> 
>>> list[3:30]
[99, 28, 90, 20, 22, 34]
>>> list[-15:7]
[24, 56, 10, 99, 28, 90, 20]
>>> list[2:6]
[10, 99, 28, 90]
>>> list[5:10]
[90, 20, 22, 34]
>>> list[6:10]
[20, 22, 34]
>>> list[8:15]
[34]
>>> list[10:20]
[]
>>> list2 = [1,2,'a','c',[6,7,8],4,9]
>>> list2[4]
[6, 7, 8]
>>> list2[4][1]
7
>>> list3 =[1,2,3]
>>> list3 = list4
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list3 = list4
NameError: name 'list4' is not defined
>>> list3 = [1,2,3]
>>> list3 = list2
>>> list3
[1, 2, 'a', 'c', [6, 7, 8], 4, 9]
>>> list2
[1, 2, 'a', 'c', [6, 7, 8], 4, 9]
>>> list2 = list3
>>> list2
[1, 2, 'a', 'c', [6, 7, 8], 4, 9]
>>> 