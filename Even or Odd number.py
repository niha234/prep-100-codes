#Even or Odd number
num=int(input())
if num % 2==0:
    print("even")
else:
    print("odd")


num=int(input())
print("even" if num%2==0 else "odd")


def isEven(num):
  return not num&1

if __name__ == "__main__":
  num=int(input())
  if isEven(num):
    print('Even')
  else:
    print('Odd')