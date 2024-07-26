Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> subjectCodes = [['Sanskrit',43],['English',85],['Maths',65],['History',36]]
>>> subjectCodes[1]
['English', 85]
>>> print(subjectCodes[1][0])
English
>>> print(subjectCodes[1][1])
85
>>> print(subjectCodes[1][0],subjectCodes[1][1])
English 85
>>> 
>>> L1 = [1,2,3]
>>> L2 = [1,2,3]
>>> L3 = [1,[2,3]]
>>> L1 == L2
True
>>> L1 == L3
False
>>> [1,2,3,4]<[4,5,6]
True
>>> [1,2,3,4]<[1,2,5,3]
True
>>> [1,2,3,4]<[1,2,3,2]
False
>>> [1,2,3,4]>[0,1,1,3]
True
>>> l1 = [20,30]
>>> l2 = [20,30]
>>> l3 = ['20','30']
>>> l4 = [20.0,30.0]
>>> l5 = [20,30,50]
>>> l1 == l2
True
>>> l1 > l3
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l1 > l3
TypeError: '>' not supported between instances of 'int' and 'str'
>>> l1 == l3
False
>>> l1 > l2
False
>>> l4 > l1
False
>>> l4 == l1
True
>>> l1 < l5
True
>>> 

>>> 