# coding: utf-8
"""
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，
比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
"""
# 这种退回操作一般就使用嵌套

def patrol(board, row, col, step=1):
    # 棋子不能跳出边界，且不能走重复, board[row][col] = 0 表明重来没有走过
    if 0 <= row < SIZE and 0 <= col < SIZE and board[row][col] == 0:
        board[row][col] = step
        global total
        if step == SIZE * SIZE:
            total += 1
            print("the way {} is: ".format(total))
            print("board: {}".format(board))
        # 棋子可以走的方向：
        # (1, 2) (2, 1) (-1, 2) (-2, 1)
        # (1, -2) (2, -1) (-1, -2) (-2, -1)
        patrol(board, row + 1, col + 2, step+1)
        patrol(board, row + 2, col + 1, step+1)
        patrol(board, row - 1, col + 2, step+1)
        patrol(board, row - 2, col + 1, step+1)
        patrol(board, row + 1, col - 2, step+1)
        patrol(board, row + 2, col - 1, step+1)
        patrol(board, row - 1, col - 2, step+1)
        patrol(board, row - 2, col - 1, step+1)
        # 所有的方向都试过后，如果条件不满足，舍弃该方案，board[row][col] 置 0
        board[row][col] = 0
    

total = 0
SIZE = 5
# 初始化棋盘
board = [[0] * SIZE for _ in range(SIZE)]
print("raw board: []".format(board))
# 坐标 (0, 0) 开始起跳
patrol(board, 0, 0)




