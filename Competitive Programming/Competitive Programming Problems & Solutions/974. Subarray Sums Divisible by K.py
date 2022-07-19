# https://leetcode.com/problems/subarray-sums-divisible-by-k/
from typing import List

#*****
# https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/413234/DETAILED-WHITEBOARD!-BEATS-100-(Do-you-really-want-to-understand-It)
# The number of all possible subarrays of an array of size N is N * (N + 1)/2. Let countSubarrays(N) = N * (N + 1)/2
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod = [0]*k
        mod[0] = 1
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            mod[sum1%k] += 1
        # print(mod)
        ans = 0
        for i in range(k):
            x = mod[i]
            ans+= ((x*(x-1))//2)
        return ans