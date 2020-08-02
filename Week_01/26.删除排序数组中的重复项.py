'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-07-27 19:54:06
@LastEditors: TangFengKang
@LastEditTime: 2020-08-02 19:55:41
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_index = 0
        fast_index = 1
        while fast_index < len(nums):
            if nums[fast_index] == nums[slow_index]:
                fast_index += 1
            else:
                slow_index += 1
                nums[slow_index] = nums[fast_index]    
        return slow_index + 1
# @lc code=end

