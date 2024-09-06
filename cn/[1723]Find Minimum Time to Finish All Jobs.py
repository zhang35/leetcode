# You are given an integer array jobs, where jobs[i] is the amount of time it ta
# kes to complete the ith job. 
# 
#  There are k workers that you can assign jobs to. Each job should be assigned 
# to exactly one worker. The working time of a worker is the sum of the time it ta
# kes to complete all jobs assigned to them. Your goal is to devise an optimal ass
# ignment such that the maximum working time of any worker is minimized. 
# 
#  Return the minimum possible maximum working time of any assignment. 
# 
#  
#  Example 1: 
# 
#  
# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= jobs.length <= 12 
#  1 <= jobs[i] <= 107 
#  
#  Related Topics 递归 回溯算法 
#  👍 100 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtrack(workloads, idx, limit):
            if idx >= len(jobs):
                return True
            cur = jobs[idx]
            for i in range(len(workloads)):
                if workloads[i] + cur <= limit:
                    workloads[i] += cur
                    if backtrack(workloads, idx+1, limit):
                        return True
                    workloads[i] -= cur # 回溯
                if workloads[i] == 0 or workloads[i] + cur == limit:
                    break
            return False

        def check(k, limit):
            workloads = [0] * k
            return backtrack(workloads, 0, limit)

        jobs.sort(reverse=True)
        l = jobs[0]  # 完成时间下界为时间最长的工作
        r = sum(jobs)  # 完成时间上界为工作时间总和，只分给一个人
        while l < r:
            mid = (l + r) >> 1
            if check(k, mid):
                r = mid
            else:
                l = mid + 1
        return l
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
jobs = [1,2,4,7,8]
k = 2
ret = s.minimumTimeRequired(jobs, k)
print(ret)
