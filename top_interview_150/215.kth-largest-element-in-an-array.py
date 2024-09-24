#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (67.07%)
# Likes:    17255
# Dislikes: 906
# Total Accepted:    2.5M
# Total Submissions: 3.8M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
# 
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
# 
# Can you solve it without sorting?
# 
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start

# This method will fail one test case from Time Limit

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def partition(nums: list[int], low: int, high: int) -> int:
#             pivot = nums[high]
#             i = low

#             for j in range(i, high):
#                 if nums[j] < pivot:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     i += 1

#             nums[i], nums[high] = nums[high], nums[i]
#             return i
        
#         n = len(nums)
#         k = n - k
#         low, high = 0, n - 1

#         while low <= high:
#             p = partition(nums, low, high)
#             if p > k:
#                 high = p - 1
#             elif p < k:
#                 low = p + 1
#             else:
#                 return nums[p]
import random

class Solution:
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)

        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
              
# @lc code=end

