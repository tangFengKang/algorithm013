'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-12 17:09:27
LastEditors: TangFengKang
LastEditTime: 2020-08-13 18:24:19
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, size = [], len(nums)
        def backtrack(stack = []):
            if(len(stack) == len(nums)):
                res.append(stack[:])
            for i in range(size):
                if nums[i] in stack:
                    continue
                else:
                    stack.append(nums[i])
                    backtrack(stack)
                    stack.pop()
        backtrack()
        return res
# @lc code=end

