'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-08-04 11:05:42
@LastEditors: TangFengKang
@LastEditTime: 2020-08-04 14:01:24
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #中序遍历 左-根-右
        
        if not root:
            return []
        """    
        #递归
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """
        #迭代2 前序/中序后序遍历通用
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right    
        return result
    
# @lc code=end

