# cook your dish here
for _ in range(int(input())):
    n = int(input())
    mp = {}
    if n == 1:
        mp[1] = 1
    elif n == 2:
        mp[3] = 1
        mp[4] = 1
    elif n == 4:
        mp[1] = 4
    else:
        mp[2] = n-1
        mp[n-2] = 1
    print(len(mp))
    for x in mp:
        print(x, mp[x])