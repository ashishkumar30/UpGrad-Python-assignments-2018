                                                                                                                            # THREAD's

import time
import threading


#Q1.Create a threading process such that it sleeps for 5 seconds and then prints out a message.

'''
def task():
   print("Wait for 5 seconds")
   time.sleep(5)
   print("Hello")

threading.Thread(target=task).start()

'''

###############################


#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between 

'''
def task():
   for i in range(1,11):
      print(i)
      time.sleep(1)

threading.Thread(target=task).start()

'''
                                                                                                              
#################################


#Q3.Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display. Delay goes like 2sec-4sec-6sec-8sec-10sec 

'''
l1=[1,2,3,4,5]

def task():
   delay=2
   for i in l1:
      print(i)
      time.sleep(delay)
      delay+=2

threading.Thread(target=task).start()
'''

#################################


#Q4.Call factorial function using thread.

'''
def fact(num,d):
    f=1
    for i in range(2,num+1):
       f*=i
    time.sleep(d)
    print("Factorial of %d is %d"%(num,f))

n=int(input("Enter number: "))
threading.Thread(target=fact,args=(n,2)).start()
'''

##################### END
