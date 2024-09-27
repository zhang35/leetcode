#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (40.64%)
# Likes:    8788
# Dislikes: 1906
# Total Accepted:    793K
# Total Submissions: 1.9M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# You are given an m x n matrix board containing letters 'X' and 'O', capture
# regions that are surrounded:
# 
# 
# Connect: A cell is connected to adjacent cells horizontally or
# vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the
# region with 'X' cells and none of the region cells are on the edge of the
# board.
# 
# 
# A surrounded region is captured by replacing all 'O's with 'X's in the input
# matrix board.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 
# Explanation:
# 
# In the above diagram, the bottom region is not captured because it is on the
# edge of the board and cannot be surrounded.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# 
# Output: [["X"]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i in (-1, m) or j in (-1, n) or board[i][j] != 'O':
                return

            board[i][j] = '#'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        li = []
        for i in range(m):
            if board[i][0] == 'O':
                li.append((i, 0))
            if board[i][n - 1] == 'O':
                li.append((i, n - 1))

        for j in range(n):
            if board[0][j] == 'O':
                li.append((0, j))
            if board[m - 1][j] == 'O':
                li.append((m - 1, j))

        for i, j in li:
            dfs(i, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = 'X' if board[i][j] != '#' else 'O'

        return
# @lc code=end

