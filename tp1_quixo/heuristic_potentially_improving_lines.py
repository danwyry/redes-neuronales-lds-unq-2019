def h_potentially_improving_lines(game):
    player = game.current_player
    board = game.board
    lenght_weights = { 2: 2, 3: 4, 4: 8 }
    sum = 0
    for col_or_row in range(5):
        found_row, found_col= False,False
        for length in range(4, 1, -1):
            if not found_col and is_one_move_improvable_col(board,col_or_row,length,player):
                found_col = True
                sum += lenght_weights[length]
            if not found_row and is_one_move_improvable_row(board,col_or_row,length,player):
                found_row = True
                sum += lenght_weights[length]

    found_diag_desc, found_diag_asc = False,False
    for length in range(4, 1, -1):
        if not found_diag_asc and is_one_move_improvable_diag_asc(board,length,player):
            found_diag_asc = True
            sum += lenght_weights[length] * 1.5
        if not found_diag_desc and is_one_move_improvable_diag_desc(board,length,player):
            found_diag_desc = True
            sum += lenght_weights[length] * 1.5

    return sum

def is_one_move_improvable_row(board, row, l, pl):
    prev_row = row - 1 if row > 0 else 4
    next_row = row + 1 if row < 4 else 0
    i = l
    f = False
    col = 0
    s = 0
    while col < 5:
        if not f:
            if board[row][col] == pl:
                col += 1
                if l > 0:
                    l -= 1
            elif board[prev_row][col] == pl or board[next_row][col] == pl:
                f = True
                s = 0
                col += 1
            else:
                col += 1
                l = i
        else:
            if l == s:
                return True
            if 5 - col < l - s:
                return False
            elif pl == board[row][col]:
                s += 1
                col += 1
            else:
                f = False
                l = i

    return f and (l == 0 or l == s)

def is_one_move_improvable_col(board, col, l, pl):
    prev_col = col - 1 if col > 0 else 4
    next_col = col + 1 if col < 4 else 0
    i = l
    f = False
    row = 0
    s = 0
    while row < 5:
        if not f:
            if board[row][col] == pl:
                row += 1
                if l > 0:
                    l -= 1
            elif board[row][prev_col] == pl or board[row][next_col] == pl:
                f = True
                s = 0
                row += 1
            else:
                row += 1
                l = i
        else:
            if l == s:
                return True
            if 5 - row < l - s:
                return False
            elif pl == board[row][col]:
                s += 1
                row += 1
            else:
                f = False
                l = i

    return f and (l == 0 or l == s)

def is_one_move_improvable_diag_desc(board, l, pl):
    i = l
    f = False
    pos = 0
    s = 0
    while pos < 5:
        prev_pos = pos - 1 if pos > 0 else 4
        next_pos = pos + 1 if pos < 4 else 0
        if not f:
            if board[pos][pos] == pl:
                pos += 1
                if l > 0:
                    l -= 1
            elif board[pos][prev_pos] == pl or board[pos][next_pos] == pl \
                    or board[prev_pos][pos] == pl or board[next_pos][pos] == pl:
                f = True
                s = 0
                pos += 1
            else:
                pos += 1
                l = i
        else:
            if l == s:
                return True
            if 5 - pos < l - s:
                return False
            elif pl == board[pos][pos]:
                s += 1
                pos += 1
            else:
                f = False
                l = i

    return f and (l == 0 or l == s)

def is_one_move_improvable_diag_asc(board, l, pl):
    i = l
    f = False
    col = 0
    s = 0
    row = 4
    while col < 5:
        prev_col = col - 1 if col > 0 else 4
        next_col = col + 1 if col < 4 else 0
        prev_row = row - 1 if row > 0 else 4
        next_row = row + 1 if row < 4 else 0
        if not f:
            if board[row][col] == pl:
                col += 1
                row -= 1
                if l > 0:
                    l -= 1
            elif board[prev_row][col] == pl or board[next_row][col] == pl or \
                    board[row][prev_col] == pl or board[row][next_col] == pl :
                f = True
                s = 0
                col += 1
            else:
                col += 1
                row -= 1
                l = i
        else:
            if l == s:
                return True
            if 5 - col < l - s:
                return False
            elif pl == board[row][col]:
                s += 1
                col += 1
                row -= 1
            else:
                f = False
                l = i

    return f and (l == 0 or l == s)
