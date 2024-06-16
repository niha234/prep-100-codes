# Greatest of two numbers
n1=int(input())
n2=int(input())
if n1>n2:
    print(n1)
else:
    print(n2)


n1=int(input())
n2=int(input())
print(n1 if n1>n2 else n2)
print(max(n1,n2))