class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Given two integers left and right that represent the range [left, right],
        return the bitwise AND of all numbers in this range, inclusive.
        https://leetcode.com/problems/bitwise-and-of-numbers-range/
        https://www.youtube.com/watch?v=6aHmj9ihjMY
        """
        diff = right - left
        ans = 0
        for i in range(31):
            val = 1 << i  # 2^i
            if diff // val == 0:  # if
                if (left & val) & (right & val):
                    ans += val
        return ans
