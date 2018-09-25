#Q.2

'''
a=int(input ('\t \n enter lenth '))
print ('length is ',a)
b=int (input (' \t \n enter breadth   '))
print ('breadth is ',b)
if  ((a%b)== 0 ):
     print ("yo! \n \t it's a square")
else:
    print('its a rectangle')
'''


'''**Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. '''


#### code


a=int(input('  Enter Quantity'))
print('Quantity is ', a)
b=(a*100)
if b >=1000:
 print('CONGRATS ! \n \t  You got discount of 10% on purchasing of :', b)
 c=b*(10/100)
 print ("Your discount is ",c)
 d=b-c
 print('You have to pay only ',d)
else:
 print("You have to pay : ",b)
 print('\n \t "Buy some more to get 10 % discount on purchasing of quantity 10 or more. ', "\n \t \"Happy Shopping\" ")
     



''' Q.4- Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored,
 which is stored in the integer variable points(your input). points can only take on positive integer values up to 200. 
If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. 
If there's no prize, the message should state "Sorry! No prize this time."
Points	Prize
1-50	No Prize
51-150	Wooden Dog
151-180	Book
181-200	Chocolates '''

##### code

a=int(input( ' enter your point ' ))
print ("your point is ", a)
if a<=50 :
    print ('so sorry no prize for ponts between 1 to 50 , and your point is ' ,a  )
if a>=51 and a<=150 :
    print( " \n \t Congratulations ! \n \t \" You won a wooden Dog ! \" ")
if a>=151 and a<=180 :
 print (" \n \t Congratulations ! \n \t \" You won a Book ! \" ")
if a>=181 and a<=200 :
    print (" \n \t Congratulations ! \n \t \" You won Chocolates ! \" ")
if a>=201 :
    print ("thats an invalid point ! plese enter valid points ")



''' Q.5 Take the input age of 3 people and determine oldest and youngest among them '''

first=int(input(" Enter first person's  age:"))
second=int(input(" Enter second person's age:"))
third=int(input("Enter third person's age:"))

if first>second and first>third:
    print("First is  person is older   ")
    
if second>first and second>third:
    print("Second person is older  ")
    
if third>first and third>second:
    print("Third person is older   ")
    
if first<second and first<third:
    print("First person is younger   ")

if second<first and second<third:
    print("First person is younger   ")




# Q. leap year

year=int(input("Enter the year:"))
if((year%4)==0 and (year%400)==0 or (year%100)!=0):
    print("The entered year is the leap year:",year)
else:
    print("The entered year is not a leap year:",year)

if third<first and third<second:
    print("First person is younger   ")

if first==second and first==third and second==third:
    print("All of three are of equal age")
