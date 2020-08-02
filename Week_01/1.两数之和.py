'''
@Description: 
@Version: 1.0
@Autor: Tang
@Date: 2020-07-22 10:37:39
@LastEditors: Tang
@LastEditTime: 2020-07-30 10:36:29
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index in range(len(nums)):
            diff_index = dict.get(target - nums[index])
            if diff_index is not None:
                return [diff_index, index] 
            dict[nums[index]] = index
                
# @lc code=end

