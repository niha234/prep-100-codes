#prime factorial
n=int(input("enter"))
l=[]
for i in range(2,n):
    while n%i==0:#25%2!=0,25%5==0
        l.append(i)#[5]
        n=n//i#n=25//5=
print(l)

