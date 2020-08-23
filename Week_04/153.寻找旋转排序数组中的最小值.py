'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-22 21:35:56
LastEditors: TangFengKang
LastEditTime: 2020-08-22 21:45:28
'''
#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0 ,len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]: #中值 小于 右值  最小值在左半边 缩小右边界
                right = mid  #中值有可能是最小值  右边界 只能取到 中界
            else: #中值 > 右值，最小值在右半边，收缩左边界
                left = mid + 1
        return nums[left]  #循环结束，left == right，最小值输出nums[left]或nums[right]均可
# @lc code=end

