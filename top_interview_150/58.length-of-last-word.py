#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (53.47%)
# Likes:    5319
# Dislikes: 294
# Total Accepted:    2.2M
# Total Submissions: 4.2M
# Testcase Example:  '"Hello World"'
#
# Given a string s consisting of words and spaces, return the length of the
# last word in the string.
# 
# A word is a maximal substring consisting of non-space characters only.
# 
# 
# Example 1:
# 
# 
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# 
# 
# Example 2:
# 
# 
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# 
# 
# Example 3:
# 
# 
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        cnt = 0
        while i >= 0 and s[i] != ' ':
            cnt += 1
            i -= 1
        return cnt  
# @lc code=end

