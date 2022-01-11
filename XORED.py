# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    if n == 1:
        print(x)
    else:
        ans = [0]*n
        temp_xor = 0
        for i in range(n-1):
            temp_xor ^= i            
            ans[i] = i
        last = x ^ temp_xor
        set_18 = 1 << 18
        # Case 1: n-1 <= last <= 5*10^5 
        if n-1 <= last <= 5*10**5:
            ans[n-1] = last
        else:
            ans[n-1] = last ^ set_18
            # Case 2: last < n-1 
            if ans[0] ^ set_18 == ans[n-1]:
                ans[1] ^= set_18
            # Case 3: last > 5*10^5
            else:
                ans[0] ^= set_18
        print(*ans)
            