'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-06 13:54:07
LastEditors: TangFengKang
LastEditTime: 2020-08-06 14:32:05
'''
#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0: return False
        if num == 1: return True
        factor = [2, 3, 5]
        for n in factor:
            while num % n == 0:
                num /= n
        return num == 1        
            

# @lc code=end

