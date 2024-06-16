#Leap year or not
year=int(input())
if year %4==0 and year%100!=0:
    print("leap year")
elif year%400==0:
    print("leap year")
else:
    print("not leap year")


year=2003
if (year%400==0) or (year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not leap year")


import calendar
year=int(input())
if calendar.isleap(year):
    print("leap year")
else:
    print("not leapyear")


