# Given an array A of strings made only from lowercase letters, return a list of
#  all characters that show up in all strings within the list (including duplicate
# s). For example, if a character occurs 3 times in all strings but not 4 times, y
# ou need to include that character three times in the final answer. 
# 
#  You may return the answer in any order. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
#  
# 
#  
#  Example 2: 
# 
#
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 100 
#  1 <= A[i].length <= 100 
#  A[i][j] is a lowercase letter 
#  
#  
#  Related Topics 数组 哈希表 
#  👍 160 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = Counter(A[0])
        for i in range(1, len(A)):
            ans &= Counter(A[i])
        return list(ans.elements())
# leetcode submit region end(Prohibit modification and deletion)
