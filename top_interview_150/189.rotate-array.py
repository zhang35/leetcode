#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Medium (41.44%)
# Likes:    18230
# Dislikes: 1991
# Total Accepted:    2.5M
# Total Submissions: 6M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an integer array nums, rotate the array to the right by k steps, where
# k is non-negative.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# Try to come up with as many solutions as you can. There are at least three
# different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
# 
#

# @lc code=start
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n  # be careful of this!
#         temp_nums = nums[n-k: n]

#         i = n - k - 1
#         while i >= 0:
#             nums[i+k] = nums[i]
#             i -= 1
        
#         nums[:k] = temp_nums
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
# @lc code=end

