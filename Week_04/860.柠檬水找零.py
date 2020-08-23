'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-20 13:59:56
LastEditors: TangFengKang
LastEditTime: 2020-08-20 14:21:38
'''
#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            # 收到一张5块钱
            if bill == 5:
                five += 1
            # 收到一张10块钱
            elif bill == 10:
                # 没有5块钱零钱找
                if not five: return False
                # 有5块钱零钱找
                # 5块钱纸币数量 -1，10块钱纸币数量 +1
                five -= 1
                ten += 1
            else:
                # 20块钱的优先 找10块和5块
                if five and ten:
                    five -= 1
                    ten -= 1
                # 只有5块钱纸币 且大于等于3张
                elif five >= 3:
                    five -= 3
                # 5块钱和10块钱纸币都没有了 没法找零
                else:
                    return False
        return True            

# @lc code=end

