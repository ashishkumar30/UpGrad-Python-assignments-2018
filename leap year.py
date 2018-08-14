year=int(input("Enter the year:"))
if((year%4)==0 and (year%400)==0 or (year%100)!=0):
    print("The entered year is the leap year:",year)
else:
    print("The entered year is not a leap year:",year)
