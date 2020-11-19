# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 855 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # i、j，分别指向当前位置后第一个0和第一个非0
        n = len(nums)
        i = j = 0
        while j < n :
            while i<n and nums[i]!=0: i += 1
            j = i + 1
            while j<n and nums[j]==0: j += 1
            if j < n: nums[i], nums[j] = nums[j], 0
# leetcode submit region end(Prohibit modification and deletion)
