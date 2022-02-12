# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。 
# 
#  一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。 
# 
#  返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 500 
#  grid[i][j] 的值为 0 或 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 123 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ret = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    cnt = 0
                    dq = deque()
                    dq.append((i, j))
                    visited[i][j] = True
                    isEnclave = True
                    while dq:
                        cur_i, cur_j = dq.popleft()
                        cnt += 1
                        if cur_i==0 or cur_i==m-1 or cur_j==0 or cur_j==n-1:
                            isEnclave = False
                        for ni, nj in [(cur_i-1, cur_j), (cur_i+1, cur_j), (cur_i, cur_j-1), (cur_i, cur_j+1)]:
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]==1 and not visited[ni][nj]:
                                dq.append((ni, nj))
                                visited[ni][nj] = True
                    if isEnclave:
                        ret += cnt
        return ret
# leetcode submit region end(Prohibit modification and deletion)
