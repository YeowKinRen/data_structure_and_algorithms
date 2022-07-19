# HOLI - Holiday Accommodation
# https://www.spoj.com/problems/HOLI/

# HOLI - Holiday Accommodation
# https://www.spoj.com/problems/HOLI/

def dfs(u, parent, adj, N):
    global ans
    currentTreeSize = 1
    for p in adj[u]:
        v, wt = p
        # Skip the parent node (which is acting as nbr)
        if v == parent:
            continue
        childTreeSize = dfs(v, u, adj, N)
        edgeContribution = 2 * min(childTreeSize, N - childTreeSize) * wt
        ans += edgeContribution
        # update the tree size by adding childTree Size
        currentTreeSize += childTreeSize
    return currentTreeSize


t = int(input())
for _ in range(t):
    n = int(input())
    adj = [[] for _ in range(100005)]
    # print(adj)
    for i in range(n-1):
        u, v, w = map(int, input().split())
        adj[u] += [(v, w)]
        adj[v] += [(u, w)]
    ans = 0
    dfs(1, -1, adj, n)
    print(ans)