'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-07-03 12:32:10
@LastEditors: TangFengKang
@LastEditTime: 2020-08-02 19:58:16
'''
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #解法1
        # l = len(nums)
        # if l > 1:
        #     t = k % l 
        #     nums[:] = nums[l - t:] + nums[:l - t]

        #解法2
        l = len(nums)
        k %= l
        l -= 1
        def reversal(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reversal(0,l)
        reversal(0, k -1)
        reversal(k, l)
# @lc code=end

