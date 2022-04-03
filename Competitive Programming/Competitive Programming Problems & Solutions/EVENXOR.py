# cook your dish here
a =  []
num = 0

while len(a) < 1000:
    if bin(num).count('1') % 2 == 0:
        a.append(num)
    num += 1

for _ in range(int(input())):
    n = int(input())
    print(*a[:n])