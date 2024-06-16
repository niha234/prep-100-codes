#palindrome number
n=121
temp=n
reverse=0
while temp >0:
    reminder=temp %10
    reverse=(reverse*10)+reminder
    temp=temp//10
print(reverse)
if n == reverse:
    print("palindrome")
else:
    print("not palindrome")



