'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-12 13:46:34
LastEditors: TangFengKang
LastEditTime: 2020-08-12 15:12:15
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        前序遍历 根左右
        中序遍历 左根右
        '''
        #递归终止条件
        if not preorder or not inorder:
            return
        #前序遍历 根左右 可以确定根节点
        root = TreeNode(preorder[0])
        #中序遍历 左根右 可以确定左右子树
        idx = inorder.index(preorder[0])
        #递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root
# @lc code=end

