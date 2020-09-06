'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-09-06 14:40:51
LastEditors: TangFengKang
LastEditTime: 2020-09-06 15:13:00
'''
#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        presum = [0 for i in range(len(nums))]
        presum[0] = nums[0]
        for i in range(1, len(nums)):
            presum[i] =  presum[i - 1]  + nums[i]            
        f = [[float('inf')] * len(nums) for i in range(m + 1)]
        for j in range(len(nums)):
            f[1][j] = presum[j]
        for i in range(2, m + 1):
            for j in range(i - 1, len(nums)):
                for k in range(0, j):
                    f[i][j] = min(f[i][j], max(f[i - 1][k], presum[j] - presum[k]))
        return f[m][len(nums) - 1]
# @lc code=end

