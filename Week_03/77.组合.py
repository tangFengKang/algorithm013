'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-12 15:52:26
LastEditors: TangFengKang
LastEditTime: 2020-08-13 17:27:20
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
           
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)             
                curr.pop()
        output = []
        backtrack()
        return output
# @lc code=end

