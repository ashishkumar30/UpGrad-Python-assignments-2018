
#Q1.Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

'''
class Animal:
   def animal_attribute(self,name,atri):
       print(name," has attribute to ",atri)

class Tiger(Animal):
   def show_attribute(self,name,atri):
       self.animal_attribute(name,atri)

T = Tiger()
T.show_attribute("Tiger","roar")

'''


####################



#Q2.What will be output of following code.

'''
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()

'''
''' Output :
A B
A B  '''

######################

#Q3.Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

"""
class Cop:
  name=""
  work=""
  experince=1
  designation=""
  
  def add(self,n,w,e,d):
    self.name=n
    self.work=w
    self.experince=e
    self.designation=d

  def display(self):
    print("Name: ",self.name) 
    print("Work: ",self.work)
    print("Experince(in months): ",self.experince,"months")
    print("Designation: ",self.designation)
 

class Mission(Cop):
  def add_mission_details(self,m):
      print("Mission: ",m)

m1 = Mission()
m1.add("Ashish Rathor","Crime Branch",48,"ACP")
m1.display()
m1.add_mission_details("Murder case of Rohit")
"""

######################



#Q4. Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.

'''
class Shape:
   length=int()
   breadth=int()
   def area(self,l,b):
       self.length=l
       self.breadth=b
       return self.length*self.breadth

class Rectangle(Shape):
   def display_area(self):
      l=int(input("Enter length of rectangle: "))
      b=int(input("Enter breadth of rectangle: "))
      print("Area of Rectangle: ",self.area(l,b))

r= Rectangle()
r.display_area()

class Square(Shape):
   def display_area(self):
      a=int(input("Enter side length of square: "))
      print("Area of Rectangle: ",self.area(a,a))

s= Square()
s.display_area()
'''


