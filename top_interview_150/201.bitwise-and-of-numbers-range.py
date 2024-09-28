#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (47.22%)
# Likes:    4044
# Dislikes: 303
# Total Accepted:    415.8K
# Total Submissions: 880.3K
# Testcase Example:  '5\n7'
#
# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.
# 
# 
# Example 1:
# 
# 
# Input: left = 5, right = 7
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: left = 0, right = 0
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: left = 1, right = 2147483647
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= left <= right <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt

# @lc code=end

