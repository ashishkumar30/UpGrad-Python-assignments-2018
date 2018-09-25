'''# Q1:- Take 10 integers from user and print it on screen.
x=int(input ("enter input"))
while x>0:
    print("hey is a loop",x)
    x-=1
else:
        print("terminated") '''

'''# Q2:- Write an infinite loop.An infinite loop never ends. Condition is always true.
x=1
while x>=1:                  
    print("infinite loop ! press control+c to stop, and counting no is",x)         
    x+=1   '''


#Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.


'''f=int(input("enter inputs"))
e=int(input("enter inputs"))
d=int(input("enter inputs"))
c=int(input("enter inputs"))
b=int(input("enter inputs"))
x=(b*b)
y=(c*c)
z=(d*d)
s=(e*e)
h=(f*f)
print("list os square is ", x,y,c,e,f)
print(b)
'''

# Q4:- From a list containing ints, strings and floats, make three lists to store them separately.
'''
l=['a','b','c',1,2,3,1.0,1.2,1.3]
m=[]
n=[]
o=[]
for x in range(0,len(l)):
    if type(l[x])==float:
        m.append(l[x])
    elif type(l[x])==int:
        n.append(l[x])
    else:
        o.append(l[x])
print(m,n,o)
'''

# Q5:-Using range(1,101), make a list containing even and odd numbers
'''
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even number list:\n",even)
print("Odd number list:\n",odd)     '''



'''  Q.6Print the following patterns: 
*
**
***
****
'''

'''
for x in range(5):
    print("*"*x)
'''

# Q7:- Create a user defined dictionary and get keys corresponding to the value using for loop.

'''
names=['Rajat','Ashish','Param','Naveen','Sahil','Vedant','Puru','Nitin','Manas']
marks=[84,77,95,65,75,57,98,50,87]
dict={}
for i in range(len(names)):
    dict[names[i]]=marks[i]
for i in dict.keys():
    print(i)
'''


# Q8:- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element,
#      if found. Iterate over list using for loop.

print("Enter the values for the list:")
hello=[]
hello=[str(x) for x in input().split()]
value=input("Value to be deleted from the list:")
for x in hello:
    if x==value:
        hello.remove(x)
print(hello)
    








