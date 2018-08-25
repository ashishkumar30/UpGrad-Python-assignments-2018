'''
# Q1:- Create a function to calculate the area of a circle by taking radius from user
a=float (input("enter the radius of circle " ))
b=print("this is your radius:",a)
z= (3.14*a*a)
print(z)
'''
################
'''
# Q.2   Write a function “perfect()” that determines if parameter number is a perfect number.
#      Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
def perfect(n):
  sum=0
  for i in range(1,n):
    if n%i==0:
      sum=sum+i
  if sum==n:
      return True
  else:
      return False
    
for i in range(1,1000):
  if perfect(i):
    print(i)

'''
#################


"""

# Q.3  Print multiplication table of 12 using recursion
def mult(n=12,a=1):
    print(12*a)
    if a!=10:
        mult(12,a+1)

"""

##################

'''
        
# Q.3 Write a function to calculate power of a number raised to other ( a^b ) using recursion

def rec(base,exponential):
    if(exponential==1):
        return(base)
    if(exponential !=1):
        return(base*rec(base,exponential-1))
    base=int(input("Enter the base: "))
    exponential=int(input("enter the exponential : "))
    print("Final Result:",rec(base,exponential))

'''
#################

"""
# Q5:- Write a function to find factorial of a number but also store the factorials calculated in a dictionary.

def fact(n):
    if n==1:
      return n
    else:
      return n*fact(n-1)
f=fact(n)
print(f)

d={n,f}
print(d)

"""


###### END
