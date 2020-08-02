'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-07-02 13:06:26
@LastEditors: TangFengKang
@LastEditTime: 2020-08-02 20:07:17
'''
#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0 :
                if i != j:
                    nums[i],nums[j] = nums[j],nums[i]
                i += 1
        return nums
# @lc code=end

