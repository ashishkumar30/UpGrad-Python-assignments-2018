#Q1. Circle class
'''
class Circle:
  def __init__(self,r):
    self.radius=r
  def getArea(self):
    return (3.414*self.radius*self.radius)
  def getCircumference(self):
    return (2*3.414*self.radius)

r=int(input("Enter radius of circle: "))
obj = Circle(r)
print("Area : ",obj.getArea())
print("Circumference : ",obj.getCircumference())

'''

################


#Q2. Student class
'''
class Student:
  def __init__(self,r,rn):
     self.name=n
     self.roll_number=rn
  def display(self):
     print("Name : ",self.name)
     print("Roll number : ",self.roll_number)

n=input("Enter Student's name: ")
rn=int(input("Enter Student's roll number: "))
std = Student(n,rn)
std.display()
'''

###################

#Q3. Temperature class

"""
class Temperature:
  def convertFahrenheit(self):
     C = int(input("Enter Temperature in Celcius : "))
     F=9/5*C+32
     print("Temperature in Fahrenheit : ",F)
  def convertCelsius(self):
     F = int(input("Enter Temperature in Fahrenheit : "))
     C=5/9*(F-32)
     print("Temperature in Celcius : ",C)

temp1 = Temperature()
temp1.convertFahrenheit()
temp1.convertCelsius()

"""



########################


#Q4. Movie class

'''


class Movie:
  def __init__(self,n,an,yor,r):
     self.name=n
     self.artistname=an
     self.year_of_release=yor
     self.ratings=r
  def display(self):
     print("Movie Discription :\nName : %s\nArtist Name: %s\nYear of release: %d\nRatings: %d"%(self.name,self.artistname,self.year_of_release,self.ratings))
  def update(self,n,an,yor,r):
     self.name=n
     self.artistname=an
     self.year_of_release=yor
     self.ratings=r 

m= Movie("Incredibles","xyz",2004,8)
m.display()
print("Updated details :------")
m.update("Incredibles 2","xyz1",2018,9)
m.display()


#Q5. Expenditure class
class Expenditure:
  salary=0
  def __init__(self,s,e):
     self.expenditure=e
     self.savings=s
  def display(self):
     print("Expenditure = Rs.%d\nSavings = Rs.%d"%(self.expenditure,self.savings))
  def calc_total_salary(self):
     self.salary=self.expenditure+self.savings
  def display_salary(self):
     print("Salary = Rs.",self.salary)

e=int(input("Enter expenditure amount: "))
s=int(input("Enter savings amount: "))
emp1 = Expenditure(e,s)
emp1.display()
emp1.calc_total_salary()
emp1.display_salary()
'''


## END
