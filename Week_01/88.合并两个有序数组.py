'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-07-30 14:42:00
@LastEditors: TangFengKang
@LastEditTime: 2020-07-30 14:53:42
'''
#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 双前指针
        nums_copay, nums1[:] = nums1[:m], []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums_copay[p1] < nums2[p2]:
                nums1.append(nums_copay[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums_copay[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
                                            
# @lc code=end

