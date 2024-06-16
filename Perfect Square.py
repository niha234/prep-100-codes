n = int(input())
if n < 0:
    print("negative")
else:
    is_perfect_square = False
    for i in range(1, n + 1):
        if i * i == n:
            print("perft")
            is_perfect_square = True
            break
    if not is_perfect_square:
        print("nt perft")



import math

n = int(input("Enter a number: "))
if n < 0:
    print("negative")
else:
    sqrt_n = math.isqrt(n)
    if sqrt_n * sqrt_n == n:
        print("perft")
    else:
        print("nt perft")