Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '''Q.1- Write a program to create a tuple with different data types and do the following operations.1. Find the length of tuples '''
'Q.1- Write a program to create a tuple with different data types and do the following operations.1. Find the length of tuples '
>>> t1=("python","ashok","nitish","mohit","raghav","manish","rahul","ankit","ayush","ashish","rajayt")
>>> t2=(55,22,8,6,3,4,7,1,5,1,6,8,2,3,1,9,1,3,8)
>>> len(t1)
11
>>> len(t2)
19
>>> #Q.2-Find largest and smallest elements of a tuples
>>> max(t1)
'rajayt'
>>> min(t1)
'ankit'
>>> min(t2)
1
>>> max(t2)
55
>>> #Q.3- Write a program to find the product of all elements of a tuple.
>>> ts=(2,5,8,7,3,8)
>>> ts
(2, 5, 8, 7, 3, 8)
>>> tc=(2*5*8*7*3*8)
>>> tc
13440
>>> #
>>> 
>>> 
>>> 
>>>                               #                                                      SETS
>>> 
>>> 
>>> 
>>> 
>>> '''Q.Q.1- Create two set using user defined values. 

1. Calculate difference between two sets.
2. Compare two sets.
3. Print the result of intersection of two sets.'''
'Q.Q.1- Create two set using user defined values. \n\n1. Calculate difference between two sets.\n2. Compare two sets.\n3. Print the result of intersection of two sets.'
>>> seta={2,8,6,7,6,8,2,7,2,1}
>>> type(seta)
<class 'set'>
>>> setb={5,9,6,7,4,2,,8,4,2,3,1,4}
SyntaxError: invalid syntax
>>> setb={5,9,6,7,4,2,8,4,2,3,1,4}
>>> seta
{1, 2, 6, 7, 8}
>>> setb
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> seta-setb
set()
>>> setb-seta
{9, 3, 4, 5}
>>> seta & setb
{1, 2, 6, 7, 8}
>>> seta | setb
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> 1 in seta
True
>>> 0 in seta
False
>>> c=seta|setb
>>> c
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> d=seta & setb
>>> d
{1, 2, 6, 7, 8}
>>> 
>>> 
>>> 
>>> type(c)
<class 'set'>
>>> 
>>> 
>>>    #                                                                                    DICTIONARIES
>>> 
>>> 
>>> #Q1:- Create a dictionary to store name and marks of 10 students by user inputs
>>> a={"ashish":"90", "rajat":"99","manish":"44","raghav":"99","millan":"88","rajesh":"58", "nilesh":"44", "nikita":"55","kanika":"88","mohit":"55"}
>>> type(a)
<class 'dict'>
>>> 
>>> 
>>> # Q.2 sorting dictionary acc to marks
>>> 
>>> a
{'ashish': '90', 'rajat': '99', 'manish': '44', 'raghav': '99', 'millan': '88', 'rajesh': '58', 'nilesh': '44', 'nikita': '55', 'kanika': '88', 'mohit': '55'}
>>> sorted(a.values())
['44', '44', '55', '55', '58', '88', '88', '90', '99', '99']
>>> c=sorted(a.values())
>>> c
['44', '44', '55', '55', '58', '88', '88', '90', '99', '99']
>>> 
>>> 
>>> #Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
>>> 
>>> d={"MISSISSIPPI"}
>>> type(d)
<class 'set'>
>>> d.count(m)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    d.count(m)
AttributeError: 'set' object has no attribute 'count'
>>> d.count("m")
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    d.count("m")
AttributeError: 'set' object has no attribute 'count'
>>> d=("MISSISSIPPI")
>>> d.count("M")
1
>>> d.count("I")
4
>>> d.count("S")
4
>>> d.count("P")
2
>>> c=dict()
>>> type(c)
<class 'dict'>
>>> a=d.count("M")
>>> a
1
>>> b=d.count("I")
>>> b
4
>>> c=d.count("S")
>>> c
4
>>> e=d.count("P")
>>> e
2
>>> dicionary=dict()
>>> dictionary={a,b,c,e}
>>> dictionary
{1, 2, 4}
>>> dictionary.append(b)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dictionary.append(b)
AttributeError: 'set' object has no attribute 'append'
>>> dictionary={a,b,c,e}
>>> dictionary
{1, 2, 4}
>>> 
