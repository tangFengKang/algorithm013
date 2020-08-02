'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-07-28 14:08:01
@LastEditors: TangFengKang
@LastEditTime: 2020-08-02 20:11:26
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits        
                    
# @lc code=end

