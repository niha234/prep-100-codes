#sum of digits of a number

def sum_of_digits(num):
    sum=0
    while num >0:
        digit=num%10
        sum+=digit
        num=num//10
    return sum
num=int(input())
print(sum_of_digits(num))

num = input("Enter Number: ")
sum = 0
for i in num:
    sum += int(i)

print(sum)