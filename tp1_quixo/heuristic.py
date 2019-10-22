# HEURISTICS
from tp1_quixo.quixo import NEUTRAL

def rows_with_line_len(board,len):
    rows = []
    for row in range(5):
        count = len
        cell = board[row][0]
        if cell != NEUTRAL:
            count -= 1
        for col in range(1, 5):
            if board[row][col] == NEUTRAL:
                if col == 5-len+1:
                    break
                cell = board[row][col]
                count = len
                continue
            elif cell != board[row][col]:
                if col == 5-len+1:
                    break
                count = len
                cell = board[row][col]
            else:
                count -= 1
                if count == 1:
                    rows.append((row, cell))
                    break
    return rows

def cols_with_line_len(board,len):
    cols = []
    for col in range(5):
        count = len
        cell = board[0][col]
        if cell != NEUTRAL:
            count -= 1
        for row in range(1, 5):
            if board[row][col] == NEUTRAL:
                if row == 5-len+1:
                    break
                cell = board[row][col]
                count = len
                continue
            elif cell != board[row][col]:
                if row == 5-len+1:
                    break
                count = len
                cell = board[row][col]
            else:
                count -= 1
                if count == 1:
                    cols.append((col,cell))
                    break
    return cols

def simple_heuristic(board,player):
    rows = {}
    for len in range(2,4):
        rows[len] = rows_with_line_len(board,len)

    cols = {}
    for len in range(2,4):
        cols[len] = cols_with_line_len(board,len)


