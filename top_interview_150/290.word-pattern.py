#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (42.37%)
# Likes:    7331
# Dislikes: 1043
# Total Accepted:    793.8K
# Total Submissions: 1.9M
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s. Specifically:
# 
# 
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same
# letter.
# 
# 
# 
# Example 1:
# 
# 
# Input: pattern = "abba", s = "dog cat cat dog"
# 
# Output: true
# 
# Explanation:
# 
# The bijection can be established as:
# 
# 
# 'a' maps to "dog".
# 'b' maps to "cat".
# 
# 
# 
# Example 2:
# 
# 
# Input: pattern = "abba", s = "dog cat cat fish"
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", s = "dog cat cat dog"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split(' ')
        
        m, n = len(pattern), len(words)
        if m != n:
            return False

        for i in range(m):
            if pattern[i] not in d:
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i]
            elif d[pattern[i]] != words[i]:
                return False

        return True
# @lc code=end

