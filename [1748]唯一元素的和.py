# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。 
# 
#  请你返回 nums 中唯一元素的 和 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3,2]
# 输出：4
# 解释：唯一元素为 [1,3] ，和为 4 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,1,1,1,1]
# 输出：0
# 解释：没有唯一元素，和为 0 。
#  
# 
#  示例 3 ： 
# 
#  输入：nums = [1,2,3,4,5]
# 输出：15
# 解释：唯一元素为 [1,2,3,4,5] ，和为 15 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 数组 哈希表 计数 👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ss = set()
        ret = 0
        for num in nums:
            if num not in ss:
                ss.add(num)
                ret += num
        return ret
# leetcode submit region end(Prohibit modification and deletion)
