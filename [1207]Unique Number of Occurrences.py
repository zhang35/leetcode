# Given an array of integers arr, write a function that returns true if and only
#  if the number of occurrences of each value in the array is unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
#  have the same number of occurrences. 
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 1000 
#  -1000 <= arr[i] <= 1000 
#  
#  Related Topics 哈希表 
#  👍 80 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for a in arr:
            if a in dict: dict[a] += 1
            else: dict[a] = 1
        # type: set
        seen = set()
        for v in dict.values():
            if v not in seen: seen.add(v)
            else: return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
