from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/score-after-flipping-matrix/
        """
        n = len(grid)
        m = len(grid[0])
        ans = (1 << (m - 1)) * n
        for j in range(1, m):
            val = 1 << (m - 1 - j)
            sets = 0
            for i in range(n):
                if grid[i][j] == grid[i][0]:
                    sets += 1
            ans += max(sets, n - sets) * val
        return ans
