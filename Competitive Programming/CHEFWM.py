# cook your dish here
import math
for _ in range(int(input())):
    n, m = map(int, input().split())

    # get unique prime factor count
    primes = 0
    i,primes=2,0
    while i * i <= m:
        if m % i==0:
            primes += 1
            while m % i == 0:
                m /= i
        i += 1
                
    if m != 1:
        # prime number larger than root m
        primes += 1
        
    ans = 0
    # the maximum primes are able to divide n
    for i in range(primes, 0, -1):
        if n % i == 0: 
            ans = i
            break
    print(ans)