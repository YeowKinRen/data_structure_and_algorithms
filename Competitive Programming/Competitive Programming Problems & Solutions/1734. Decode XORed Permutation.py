from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/decode-xored-permutation/
        :param encoded:
        :return:
        """
        n = len(encoded)
        val1 = 0
        val = 0
        ans = []
        for i in range(1, n + 1 + 1):
            val1 ^= i
        for i in range(0, n):
            if i % 2:
                val ^= encoded[i]
        ans.append(val ^ val1)
        for i in range(1, n + 1):
            ans.append(ans[-1] ^ encoded[i - 1])

        return ans
