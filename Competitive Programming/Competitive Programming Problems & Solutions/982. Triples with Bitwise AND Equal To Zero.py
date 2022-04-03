from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=tEmYcyxZxe8
        https://www.youtube.com/watch?v=7ibf14FeknE
        https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
        """
        dic = {}
        n = len(nums)
        for i in range(n):
            for j in range(n):
                val = nums[i] & nums[j]
                if val in dic:
                    dic[val] += 1
                else:
                    dic[val] = 1
        ans = 0
        for i in range(n):
            for key in dic:
                if (key & nums[i]) == 0:
                    ans += dic[key]
        return ans