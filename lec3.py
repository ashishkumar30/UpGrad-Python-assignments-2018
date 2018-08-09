Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Q.1- Create a list with user defined inputs.
>>> 
>>> a=["ashish","facebook","rajat","google","linkedin","tesla""ravi","google","aayush"]
>>> a
['ashish', 'facebook', 'rajat', 'google', 'linkedin', 'teslaravi', 'google', 'aayush']
>>> 
>>> 
>>> #'''Q.2- Add the following list to above created list:
[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]'''
SyntaxError: invalid character in identifier
>>> 
>>> b=a+["facebook","google","microsoft","tesla","apple"]
>>> b
['ashish', 'facebook', 'rajat', 'google', 'linkedin', 'teslaravi', 'google', 'aayush', 'facebook', 'google', 'microsoft', 'tesla', 'apple']
>>> 
>>> 
>>> #@Q.3- Count the number of time an object occurs in a list.
>>> 
>>> b.counnt("ashish")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b.counnt("ashish")
AttributeError: 'list' object has no attribute 'counnt'
>>> b.count("ashish")
1
>>> b.count('google')
3
>>> 
>>> 
>>> 
>>> 
>>> #Q.4- create a list with numbers and sort it in ascending order.
>>> 
>>> a=[7,9,6,4,6,4,2,7,6,5,2,4,6,8,7]
>>> a.sort()
>>> a
[2, 2, 4, 4, 4, 5, 6, 6, 6, 6, 7, 7, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> #Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
>>> 
>>> 
>>> 
>>> a=[5,8,8,3,2,5,6,9,5,7]
>>> a
[5, 8, 8, 3, 2, 5, 6, 9, 5, 7]
>>> b=[5,9,5,9,9,3,9,7,2,9,7]
>>> b
[5, 9, 5, 9, 9, 3, 9, 7, 2, 9, 7]
>>> a.sort()
>>> a
[2, 3, 5, 5, 5, 6, 7, 8, 8, 9]
>>> b.sort()
>>> b
[2, 3, 5, 5, 7, 7, 9, 9, 9, 9, 9]
>>> c=[a+b]
>>> c
[[2, 3, 5, 5, 5, 6, 7, 8, 8, 9, 2, 3, 5, 5, 7, 7, 9, 9, 9, 9, 9]]
>>> c.sort()
>>> c
[[2, 3, 5, 5, 5, 6, 7, 8, 8, 9, 2, 3, 5, 5, 7, 7, 9, 9, 9, 9, 9]]
>>> ##
>>> 
>>> 
>>> 
>>> 
>>> ##END
