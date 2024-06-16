n=145
num=n
sum=0
while n>0:
    fact=1
    rem=n%10
    n=n//10
    for j in range(1,rem+1):
        fact=fact*j
    sum+=fact
if sum==num:
    print("strng num")
else:
    print("not strng num")
