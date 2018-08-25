Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Q.1 Write a Python program to read last n lines of a file
>>> a=open ("C:\\Users\\sony vaio\\Desktop\\ashish\\filehandling.txt","w")
>>> a.write(" practice file handling ")
24
>>> a.close()
>>> a.read()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.read()
ValueError: I/O operation on closed file.
>>> a=open ("C:\\Users\\sony vaio\\Desktop\\ashish\\filehandling.txt","r")
>>> a.read()
' practice file handling \n“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. \nShoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” \nThat was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. \n“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. \nThey don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. \nThat’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird'
>>> ## Q.2 Write a Python program to count the frequency of words in a file
>>> a=open ("C:\\Users\\sony vaio\\Desktop\\ashish\\filehandling.txt","r")
>>> a.tell()
0
>>> a.read()
' practice file handling \n“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. \nShoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” \nThat was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. \n“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. \nThey don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. \nThat’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird'
>>> a.tell()
666
>>> ###############
>>> #Q.3 Write a Python program to copy the contents of a file to another file.
>>> 
>>> b=open("C:\\Users\\sony vaio\\Desktop\\python\\copy.txt","w")
>>> b.close()
>>> with open("C:\\Users\\sony vaio\\Desktop\\ashish\\filehandling.txt","rb") as d:
	var=d.read()

	
>>> with open("C:\\Users\\sony vaio\\Desktop\\ashish\\copy.txt","wb") as e:
	e.write(var)

	
666
>>> ###
>>> #Q4:- Write a Python program to combine each line from first file with the corresponding line in second file
>>> 
>>> with open("C:\\Users\\sony vaio\\Desktop\\ashish\\filehandling.txt") as one,open("C:\\Users\\sony vaio\\Desktop\\ashish\\copy.txt") as two:
    for l1,l2 in zip(one,two):
	    print(l1+l2)

	    
 practice file handling 
 practice file handling 

“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. 
“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. 

Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” 
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” 

That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. 
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. 

“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. 
“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. 

They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. 
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. 

That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a MockingbirdThat’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird
>>> ################
>>> # Q.5 Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
>>> import random
>>> with open ("C:\\Users\\sony vaio\\Desktop\\ashish\\random.txt","w") as a:
	for i in range (10):
		r=str(random.randint(1,50))
		a.writelines(r+"\n")
		print(r)

		
26
27
9
37
34
47
29
37
4
50
>>> with open ("C:\\Users\\sony vaio\\Desktop\\ashish\\random.txt") as a ,open("C:\\Users\\sony vaio\\Desktop\\ashish\\randomtwo.txt","w") as b:
	r=a.read().splitlines()
	r.sort()
	for i in r:
		b.write(str(i)+"\n")

		
3
3
3
3
3
3
2
3
3
2
>>> 
