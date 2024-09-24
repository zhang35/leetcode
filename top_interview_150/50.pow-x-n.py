#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (35.45%)
# Likes:    9956
# Dislikes: 9668
# Total Accepted:    1.8M
# Total Submissions: 5.2M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
# 
# 
# Example 1:
# 
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: x = 2.10000, n = 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# Constraints:
# 
# 
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= x^n <= 10^4
# 
# 
#

# @lc code=start

# Time Limit Exceeded
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1

#         if n < 0:
#             n = -n
#             x = 1 / x
        
#         ret = 1

#         for i in range(n):
#             ret *= x
        
#         return ret
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x
        
        ret = 1

        while n:
            if n % 2 == 1:
                ret *= x
            x *= x
            n //= 2

        return ret
# @lc code=end

