'''
@Description: 
@Version: 1.0
@Autor: TangFengKang
@Date: 2020-08-04 10:50:33
@LastEditors: TangFengKang
@LastEditTime: 2020-08-04 11:05:10
'''
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #后序遍历 左-右-根
        #递归
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]           

        """
        #迭代
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            result.append(current.val)
        return result[::-1]    



# @lc code=end

