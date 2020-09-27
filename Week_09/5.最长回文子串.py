'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-09-27 20:05:52
LastEditors: TangFengKang
LastEditTime: 2020-09-27 21:49:49
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        dp = [[False] * len(s) for _ in range(len(s))]
        max_len = float("-inf")
        for j in range(len(s)):
            for i in range(j + 1):
                if s[j] == s[i] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j] and j - i + 1 > max_len:
                    result = s[i: j + 1]
                    max_len = j - i + 1
        return result
# @lc code=end

