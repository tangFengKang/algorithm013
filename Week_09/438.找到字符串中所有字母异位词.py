'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-09-26 14:53:44
LastEditors: TangFengKang
LastEditTime: 2020-09-27 21:54:22
'''
#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        s_count = [0] * 26
        res = []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res
        
# @lc code=end

