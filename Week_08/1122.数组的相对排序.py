'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-09-20 21:06:02
LastEditors: TangFengKang
LastEditTime: 2020-09-21 09:36:22
'''
#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        bins = [0 for _ in range(1001)]
        res = []
        for i in arr1:
            bins[i] += 1
        for i in arr2:
            res += [i] * bins[i]
            bins[i] = 0
        for i in range(len(bins)):
            res += [i] * bins[i]
        return res
        
# @lc code=end

