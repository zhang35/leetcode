#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (47.19%)
# Likes:    17383
# Dislikes: 807
# Total Accepted:    1.8M
# Total Submissions: 3.8M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start

# This iterative method exceeded time limit.
# Memo is needed.

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         possible_j = []
#         i = 0
#         while i < n:
#             while i < n and s[:i+1] not in wordDict:
#                 i += 1
#             if i < n:
#                 possible_j.append(i)
#             i += 1

#         if not possible_j:
#             return False

#         if possible_j[-1] == n - 1:
#             return True
        
#         for j in possible_j:
#             if self.wordBreak(s[j+1:], wordDict):
#                 return True
                
#         return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        return dp[-1]
# @lc code=end

