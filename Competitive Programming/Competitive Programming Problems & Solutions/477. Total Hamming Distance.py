from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/total-hamming-distance/
        """
        ans = 0
        n = len(nums)
        for i in range(31):
            ones = 0
            zeros = 0
            val = 1 << i
            for j in range(n):
                if nums[j] & val:
                    ones += 1
                else:
                    zeros += 1
            ans += ones * zeros
        return ans