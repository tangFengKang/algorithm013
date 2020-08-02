'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-08-01 18:06:45
@LastEditors: TangFengKang
@LastEditTime: 2020-08-01 19:44:03
'''
#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        #暴力法
        ans = 0
        size = len(height)
        i = 1
        while i < size - 1:
            j = i
            k = i
            max_left = 0
            max_right = 0
            while j >= 0:
                max_left = max(max_left,height[j])
                j -= 1
            while k < size:
                max_right = max(max_right,height[k])
                k += 1
            ans += min(max_left,max_right) - height[i]
            i += 1
        return ans    
        '''
        '''
        #动态规划
        ans = 0
        size = len(height)
        if size == 0: return 0
        i = 1
        left_max_arr = [0] * size
        left_max_arr[0] = height[0]
        while i < size:
            left_max_arr[i] = max(left_max_arr[i - 1], height[i])
            i += 1
        k = size - 2
        right_max_arr = [0] * size
        right_max_arr[size - 1] = height[size - 1]
        while k >= 0:
            right_max_arr[k] = max(right_max_arr[k + 1], height[k])
            k -= 1

        j = size - 1
        while j >= 0:
            ans += min(left_max_arr[j],right_max_arr[j]) - height[j]
            j -= 1
        return ans
        '''

        #双指针
        left, right = 0 , len(height) - 1
        left_max, right_max , ans= 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1        
        return ans

             
# @lc code=end

