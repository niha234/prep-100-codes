#Sum of numbers in a given range
n1=int(input())
n2=int(input())
sum=0
for i in range(n1,n2+1):
    sum+=i
print(sum)