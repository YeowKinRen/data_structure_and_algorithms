from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-the-shortest-superstring/
    https://www.youtube.com/watch?v=C_qo3s1fxhM
    """

    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        # Step 1: Build a graph of the words overlap
        graph = self.build_graph(words)
        dp = [[240] * n for _ in range(1 << n)]
        path = [[-1] * n for _ in range(1 << n)]
        min = float("inf")
        last = -1
        # Step 2: Find the shortest path to visit all word
        # 2 states (used/unused)
        for curr_state in range(1, 1 << n):  # Iterate all states
            # dp[curr_state] = float('inf') // 2
            for curr_node in range(n):  # Iterate all ending nodes for the curr_state
                if curr_state & (1 << curr_node) == 0:
                    continue
                prev_state = curr_state ^ (1 << curr_node)
                if prev_state == 0:
                    dp[curr_state][curr_node] = len(words[curr_node])
                else:
                    for prev_node in range(n):
                        if dp[prev_state][prev_node] + graph[prev_node][curr_node] < dp[curr_state][curr_node]:
                            dp[curr_state][curr_node] = dp[prev_state][prev_node] + graph[prev_node][curr_node]
                            path[curr_state][curr_node] = prev_node
                if (curr_state == ((1 << n) - 1)) and dp[curr_state][curr_node] < min:
                    min = dp[curr_state][curr_node]
                    last = curr_node

        sb = ""
        s = (1 << n) - 1
        while s > 0:
            prev_node = path[s][last]
            if prev_node == -1:  # first node
                sb = (words[last] + sb)
            else:
                sb = (words[last][len(words[last]) - graph[prev_node][last]:] + sb)

            print(sb)
            s = s ^ (1 << last)
            last = prev_node
        return sb

    def build_graph(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                found = False
                for index in range(len(words[i])):
                    if words[j].startswith(words[i][index:]):
                        graph[i][j] = len(words[j]) - (len(words[i]) - index)
                        found = True
                        break
                if not found:
                    graph[i][j] = len(words[j])

        return graph


if __name__ == '__main__':
    words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
    # Output: "gctaagttcatgcatc"
    sol = Solution()
    print(sol.build_graph(words))
    print(sol.shortestSuperstring(words))
