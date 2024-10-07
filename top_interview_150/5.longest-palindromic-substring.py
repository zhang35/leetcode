#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (34.36%)
# Likes:    29744
# Dislikes: 1821
# Total Accepted:    3.4M
# Total Submissions: 9.7M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrom = ''
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            longest_palindrom = s[i]

        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(longest_palindrom) < len(s[i : j + 1]):
                            longest_palindrom = s[i : j + 1]

        return longest_palindrom
# @lc code=end

