#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (63.66%)
# Likes:    8023
# Dislikes: 701
# Total Accepted:    644.2K
# Total Submissions: 1M
# Testcase Example:  '[2,2,3,2]'
#
# Given an integer array nums where every element appears three times except
# for one, which appears exactly once. Find the single element and return it.
# 
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
# 
# 
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each element in nums appears exactly three times except for one element which
# appears once.
# 
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ones: Tracks the bits that have appeared once.
        # twos: Tracks the bits that have appeared twice.
        ones = twos = 0

        for num in nums:
            # The & operation ensures that only the bits that have appeared once (after XOR) 
            # and not twice (after negating twos) are retained.
            ones ^= (num & ~twos)

            # The & operation ensures that only the bits that have appeared twice (after XOR) 
            # and not once (after negating ones) are retained.
            twos ^= (num & ~ones)

        return ones
# @lc code=end

