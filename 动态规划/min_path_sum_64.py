#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 23:10
# @Author  : liuhu
# @Site    : 
# @File    : min_path_sum_64.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:

    @staticmethod
    def min_path_sum_one(grid):
        # 自顶向下
        import functools
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        @functools.lru_cache(None)
        def helper(i, j):
            if i == row - 1 and j == col - 1:
                return grid[i][j]
            if i >= row or j >= col:
                return float("inf")
            tmp = 0
            tmp += grid[i][j] + min(helper(i, j + 1), helper(i + 1, j))
            return tmp

        return helper(0, 0)

    @staticmethod
    def min_path_sum(grid):
        # 不可以在原表上修改
        if not grid:
            return
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]

        dp[0][0] = grid[0][0]
        # 初始化第一列
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 初始化第一排
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for r in range(1, row):
            for c in range(1, col):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[-1][-1]
