'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-06 16:51:14
LastEditors: TangFengKang
LastEditTime: 2020-08-09 20:45:04
'''
#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 解法1
        result = []
        #统计出现的次数
        count_dirct = {}
        for num in nums:
            count = count_dirct.setdefault(num, 0) + 1
            count_dirct[num] = count
        #反转统计次数键值对 key对应的是list [1,2] 2 出现次数都是1 key冲突 所以存list
        reversal_count_dirct = {}
        for key in count_dirct:
            if count_dirct[key] not in reversal_count_dirct:
                reversal_count_dirct[count_dirct[key]] = [key]
            else:
                reversal_count_dirct[count_dirct[key]].append(key)

        while len(result) < k:
            max_key = max(reversal_count_dirct)
            for num in reversal_count_dirct[max_key]:
                result.append(num)
            reversal_count_dirct.pop(max_key)
        return result

        #解法2
        '''
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get) 
        '''

            
# @lc code=end

