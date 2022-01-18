# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    x = []
    for i in range(n):
        win = "X"
        for j in range(n-i-1):
            if win == "X":
                if j == n-1:
                    win = s[j+i]
                elif s[j+i] == s[j+1+i]:
                    win = s[j+i]
                elif (s[j+i] == "R" and s[j+1+i] == "P") or (s[j+i] == "P" and s[j+1+i] == "R"):
                    win = "P"
                elif (s[j+i] == "S" and s[j+1+i] == "P") or (s[j+i] == "P" and s[j+1+i] == "S"):
                    win = "S"
                elif (s[j+i] == "S" and s[j+1+i] == "R") or (s[j+i] == "R" and s[j+1+i] == "S"):
                    win = "R"
            else:
                if win == s[j+1+i]:
                    win = s[j+i]
                elif (win == "R" and s[j+1+i] == "P") or (win == "P" and s[j+1+i] == "R"):
                    win = "P"
                elif (win == "S" and s[j+1+i] == "P") or (win == "P" and s[j+1+i] == "S"):
                    win = "S"
                elif (win == "S" and s[j+1+i] == "R") or (win == "R" and s[j+1+i] == "S"):
                    win = "R"
        if i == n -1:
            win = s[i]
        x += [win]
    print("".join(x))