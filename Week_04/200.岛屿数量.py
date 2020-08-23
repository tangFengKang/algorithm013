'''
Description: 
Version: 1.0
Autor: TangFengKang
Date: 2020-08-21 15:29:54
LastEditors: TangFengKang
LastEditTime: 2020-08-21 17:26:38
'''
#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        #岛屿个数
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0': return
        grid[i][j] = '0'
        # 当前岛屿的相邻相邻相邻...上下左右标记为0
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

# @lc code=end

