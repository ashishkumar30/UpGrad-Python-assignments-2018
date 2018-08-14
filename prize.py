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

    
