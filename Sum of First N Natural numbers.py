  #Sum of First N Natural numbers
n=int(input())
sum=0
for i in range(n+1):
    sum+=i
print(sum)


n=int(input())
print((n*(n+1)/2))


def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 6
print(getSum(num))