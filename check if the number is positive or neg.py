# check if the number is positive or negative
num=int(input())
if num>0:
    print("Positive")
elif num<0:
    print("negative")
else:
    print("zero")


num=int(input())
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")


num=int(input())
print("positive" if num>=0 else "negative")