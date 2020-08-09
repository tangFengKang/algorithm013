'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-08-03 14:09:18
@LastEditors: TangFengKang
@LastEditTime: 2020-08-03 14:34:34
'''
#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        dict = {}
        for char in strs:
            dict.setdefault(str(sorted(char)), []).append(char)  
        return list(dict.values())

# @lc code=end

