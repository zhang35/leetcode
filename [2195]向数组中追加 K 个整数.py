# 给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最
# 小 。 
# 
#  返回追加到 nums 中的 k 个整数之和。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,4,25,10,25], k = 2
# 输出：5
# 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
# nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
# 所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。 
# 
#  示例 2： 
# 
#  输入：nums = [5,6], k = 6
# 输出：25
# 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
# nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
# 所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i], k <= 10⁹ 
#  
#  Related Topics 贪心 数组 数学 排序 👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ret = 0
        nums.sort()
        nums.append(float('inf'))
        start = 0
        i = 0
        while k:
            x = min(k, nums[i] - start - 1)  # 待累加区间的元素个数
            if x > 0:
                ret += (start+1) * x + (x - 1) * x // 2  # 连续自然数求和公式
                k -= x
            start = nums[i]
            i += 1
        return ret
# leetcode submit region end(Prohibit modification and deletion)
