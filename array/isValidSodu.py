#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/10/31 上午11:04
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : isValidSodu.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

#
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 每一个字典表示一行的元素出现次数

        dic_row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3 * (i // 3) + (j // 3)]:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3 * (i // 3) + (j // 3)][num] = 1
                else:
                    return False
        return True

    def isValidSudokuv2(self, board):
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                g = r / 3 * 3 + c / 3
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])

        return True
