a=int(input("Enter year: "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print(a,"is a leap year")
else:
    print(a,"is not a leap year")


