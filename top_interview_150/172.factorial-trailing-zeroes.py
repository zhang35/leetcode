#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Medium (43.79%)
# Likes:    3243
# Dislikes: 1960
# Total Accepted:    487.6K
# Total Submissions: 1.1M
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# 
# Example 3:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^4
# 
# 
# 
# Follow up: Could you write a solution that works in logarithmic time
# complexity?
# 
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # In the n! operation, factors 2 is always ample.
        # So we just count how many 5 factors in all number from 1 to n.

        # count = n/5 + n/25 + n/125 + ... + 0
        
        # If n=5 ... there will be 1(5)
        # If n=10 ... there will be 2(5)
        # If n=15 ... there will be 3(5)
        # If n=25 ... there will be 5(5) + 1 (5)
        
        ret = 0

        while n:
            tmp = n // 5
            ret += tmp
            n = tmp

        return ret
# @lc code=end

