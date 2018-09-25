Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Q.1- Print anything you want on screen.
>>> print("hii my name is ashish and m learning well")
hii my name is ashish and m learning well
>>> x="hy my name is ashish and m learning well"
>>> x
'hy my name is ashish and m learning well'
>>> x ="hy my name is ashish"
>>> print(x)
hy my name is ashish
>>> print("%s"%("hy y name is ashish"))
hy y name is ashish
>>> #END
>>> 
SyntaxError: invalid syntax
>>> >>> #Q.2- Join two strings using '+'.
>>> x="\"Acad\""
>>> y="\"View\""
>>> print(x+y)
"Acad""View"
>>> #without ""
>>> x="Acad"
>>> y="View"
>>> print(x+y)
AcadView
>>> #END
SyntaxError: invalid syntax
>>> >>> #Q.3- Take the input of 3 variables x, y and z . Print their values on screen
>>> x="rajat"
>>> y="ashish"

>>> z="yash"
>>> print(x,y,z)
rajat ashish yash
>>> #another
>>> 

>>> x="1"
>>> y="2"
>>> z="3"
>>> print(x,y,z)
1 2 3
SyntaxError: invalid syntax
>>> >>> #Q.4- Print “Let’s get started” on screen.
>>> print(" \" Let’s get started \"   ")
 " Let’s get started "   
>>> #another
>>> x=" \" Let’s get started \"   "
>>> x
' " Let’s get started "   '
>>> #another
>>> 
>>> x=" \" Let’s get started \"   "
>>> print(x)
 " Let’s get started "   
>>> 
>>> #end
SyntaxError: invalid syntax
>>> >>> #Q.5- Print the following values using placeholders.
#s=”Acadview”
#course=”Python”
#fees=5000
>>> 
>>> print(" s = \"%s\", \n course = \"%s\" , \n fees = \"%d\"" % ("python","acadview", 5000))
 s = "python", 
 course = "acadview" , 
 fees = "5000"
>>> #End
SyntaxError: invalid syntax
>>> >>> #Q.6- Let’s do some interesting exercise:
#name=”Tony Stark”
#salary=1000000
#print(‘%s’’%d’)%(____ ,____) 

>>> name= "\"tony stark\""
>>> saliry= "\"100000\""
>>> print("%s,%s" % (name,saliry))
"tony stark","100000"
>>> #END
