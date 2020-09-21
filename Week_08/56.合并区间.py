'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-09-20 19:05:26
LastEditors: TangFengKang
LastEditTime: 2020-09-21 09:26:38
'''
#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])  
        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]: 
                res.append(inter)
            else: 
                res[-1][1] = max(res[-1][1], inter[1])
        return res
# @lc code=end

