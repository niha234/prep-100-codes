number = 371
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)#1,7,3
  num = num/10#371/10=37,7
  sum += pow(digit,length)#1^3+7^3+3^3
if sum==number:
  print("Armstrong")
else:
  print("Not Armstrong")