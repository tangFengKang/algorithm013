'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-08-04 10:25:17
@LastEditors: TangFengKang
@LastEditTime: 2020-08-04 10:53:11
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 前序遍历  根-左-右
        #递归
        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)    

        #迭代1
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            #栈 先进后出
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result           

                        
# @lc code=end

