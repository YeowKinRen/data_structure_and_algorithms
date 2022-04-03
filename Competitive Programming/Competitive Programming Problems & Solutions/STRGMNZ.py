# cook your dish here
import math

for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:  # if n is even
        print(3 * n // 2)
    else:
        fc = 0
        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            # check if n is prime
            if n % i == 0:
                fc = n // i  # the bigger factor
                count = i  # the smaller factor
                break
        if fc != 0:  # if n is odd
            print(fc * (count + 1))
        else:  # if n is odd + prime
            print(n + 1)
