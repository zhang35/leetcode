# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 9279 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i <= j:
            curSum = nums_sorted[i] + nums_sorted[j]
            if curSum > target: j -= 1
            elif curSum < target: i += 1
            else: break
        ret = []
        if (curSum==target):
            for k in range(0, len(nums)):
                if (nums[k]==nums_sorted[i]): ret.append(k)
                elif (nums[k]==nums_sorted[j]): ret.append(k)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
list = [8,3,2,1]
target = 13
print(s.twoSum(list, target))
