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

if third<first and third<second:
    print("First person is younger   ")

if first==second and first==third and second==third:
    print("All of three are of equal age")
