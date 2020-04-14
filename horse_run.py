# coding: utf-8
"""
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，
比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
"""
# 这种退回操作一般就使用嵌套

def horse_run(board, row, col, step=1):
    # 棋子不能跳出边界，且不能走重复, board[row][col] = 0 表明重来没有走过
    if 0<=row<ROWS and 0<=col<COLS and board[row][col] == 0:
        board[row][col] = step
        global total
        if step == ROWS*COLS:
            total += 1
            print("the way {} is: ".format(total))
            #print("board: {}".format(board))
        # 棋子可以走的方向：
        # (1, 2) (2, 1) (-1, 2) (-2, 1)
        # (1, -2) (2, -1) (-1, -2) (-2, -1))
        horse_run(board, row + 1, col + 2, step+1)
        horse_run(board, row + 2, col + 1, step+1)
        horse_run(board, row - 1, col + 2, step+1)
        horse_run(board, row - 2, col + 1, step+1)
        horse_run(board, row + 1, col - 2, step+1)
        horse_run(board, row + 2, col - 1, step+1)
        horse_run(board, row - 1, col - 2, step+1)
        horse_run(board, row - 2, col - 1, step+1)
        # 所有的方向都试过后，如果条件不满足，舍弃该方案，board[row][col] 置 0
        board[row][col] = 0

ROWS = 5
COLS = 5
# 创建一个 5x5 的棋盘
board = [[0] * COLS for _ in range(ROWS)]
print(board)
total = 0
horse_run(board, 0, 0)



