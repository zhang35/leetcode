#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#
# https://leetcode.com/problems/count-servers-that-communicate/description/
#
# algorithms
# Medium (60.68%)
# Likes:    1309
# Dislikes: 86
# Total Accepted:    61.5K
# Total Submissions: 101.3K
# Testcase Example:  '[[1,0],[0,1]]'
#
# You are given a map of a server center, represented as a m * n integer matrix
# grid, where 1 means that on that cell there is a server and 0 means that it
# is no server. Two servers are said to communicate if they are on the same row
# or on the same column.
# 
# Return the number of servers that communicate with any other server.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# 
# Example 2:
# 
# 
# 
# 
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other
# server.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each
# other. The two servers in the third column can communicate with each other.
# The server at right bottom corner can't communicate with any other
# server.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
# 
# 
#

# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        connected = 0               
        points=[]
        comps_per_row = [0] * rows
        comps_per_col = [0] * cols

        for row_i in range(rows):
            for col_i in range(cols):
                if grid[row_i][col_i]:
                    points.append((row_i,col_i))
                    comps_per_row[row_i]+=1
                    comps_per_col[col_i]+=1
        
        for row_i,col_i in points:
            if comps_per_row[row_i]>1 or comps_per_col[col_i]>1 :
                connected += 1                      
        
        return connected
# @lc code=end

