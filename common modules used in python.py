# Q1:- What is Time Tuple?
''' time tupples are used to access various time
these are:

import time
print(time.time())
print(time.asctime())
print(time.gmtime())
print(time.perf_counter())
print(time.localtime())
print(time.ctime())
print(time.timezone) '''

##############

#Q.2 Write a program to get formatted time

'''

import time
import os
while True:
    print(time.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system('cls')

'''
##############

#Q.3 Extract month from the time

'''
import datetime
a="28-8-2018"
b=datetime.datetime.strptime(a,"%d-%m-%Y")
print(b.month)

'''

##############

#Q.4 Extract day from the time

'''
import datetime
a="28-8-2018"
b=datetime.datetime.strptime(a,"%d-%m-%Y")
print(b.day)

'''
##############

#Q.5 Extract date (ex : 11 in 11/01/2021) from the time.

'''
import datetime
a=datetime.date.today()
print(a)

'''

###############

#Q.6 Write a program to print time using localtime method

'''
import time
a=time.localtime()
print(a)

'''

################

#Q.7  Find the factorial of a number input by user using math package functions.

'''
import math
a=int(input("enter no of which you want factorial: "))
a=math.factorial(a)
print(a)

'''

##################

#Q.8 Find the GCD of a number input by user using math package functions.

"""

import math
a=int(input("enter 1st number : "))
b=int(input("enter second number : "))
c=math.gcd(a,b)
print( " \t \" ", c , " \"  ", " \n This is the greatest common divisior of ","\"",a,"\"","and","\"",b,"\"")

'''
################## END
