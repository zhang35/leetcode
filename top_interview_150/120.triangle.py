#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (57.61%)
# Likes:    9650
# Dislikes: 561
# Total Accepted:    842.4K
# Total Submissions: 1.5M
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle array, return the minimum path sum from top to bottom.
# 
# For each step, you may move to an adjacent number of the row below. More
# formally, if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.
# 
# 
# Example 1:
# 
# 
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined
# above).
# 
# 
# Example 2:
# 
# 
# Input: triangle = [[-10]]
# Output: -10
# 
# 
# 
# Constraints:
# 
# 
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
# 
# 
# 
# Follow up: Could you do this using only O(n) extra space, where n is the
# total number of rows in the triangle?
#

# @lc code=start
class Solution:
    # Time Limit Exceeded
    
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     i = j = 0

    #     def dfs(i, j, cur_sum) -> int:
    #         if i == n:
    #             return cur_sum

    #         cur_sum += triangle[i][j]
    #         return min(dfs(i + 1, j, cur_sum), dfs(i + 1, j + 1, cur_sum))
            
    #     return dfs(0, 0, 0)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # In-place DP, top-down
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                    
        return min(triangle[-1])
# @lc code=end

