# cook your dish here
import math

def calculate(primeSet, m):
    valueSet = [1]
    for x in primeSet:
        i = 0
        while i < len(valueSet):
            if (valueSet[i]*x) <= m:
                valueSet.append(valueSet[i]*x)
            i += 1
    return valueSet

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    primeSet1 = [s[i] for i in range(0, n, 2)]
    primeSet2 = [s[i] for i in range(1, n, 2)]
    valueSet1 = calculate(primeSet1, m)
    valueSet2 = calculate(primeSet2, m)
    valueSet1.sort()
    valueSet2.sort()
    ans = 0
    start = 0
    end = len(valueSet2)-1
    while start < len(valueSet1) and end >= 0:
        if valueSet1[start] * valueSet2[end] <= m:
            ans += (end+1)
            start += 1
        else:
            end -= 1
    
    print(ans)
        
        
              
              
              