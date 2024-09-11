#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (43.68%)
# Likes:    17879
# Dislikes: 4590
# Total Accepted:    3.7M
# Total Submissions: 8.5M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_n = 200
        for s in strs:
            s_n = len(s)
            if len(s) < min_n:
                min_n = s_n
        
        n = len(strs)
        common = ""
        for i in range(min_n):
            ch = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != ch:
                    return common
            common += ch

        return common
# @lc code=end

