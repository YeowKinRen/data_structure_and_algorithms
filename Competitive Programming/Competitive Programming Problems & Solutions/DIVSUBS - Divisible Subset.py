# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    d={}
    for i in range(n):
        s=(s+l[i])%n
        if s==0:
            print(i+1)
            for j in range(i):
                print(j+1,end=" ")
            print(i+1)
            break
        elif s in d:
            print(i-d[s])
            for j in range(d[s]+1,i):
                print(j+1,end=" ")
            print(i+1)
            break
        else:
            d[s]=i