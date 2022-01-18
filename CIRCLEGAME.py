# cook your dish here
for _ in range(int(input())):
    m, x = map(int, input().split())
    win = [1]*x
    for n in range(1, x):
        # f denotes the removed player
        if m % (n+1) == 0:
            f = (n+1)
        else:
            f = m % (n+1)
        
        if f > win[n-1]:
            win[n] = win[n-1]
        else:
            win[n] = win[n-1] + 1
    print(*win)
    