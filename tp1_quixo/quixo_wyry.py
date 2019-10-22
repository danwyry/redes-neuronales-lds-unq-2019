from copy import deepcopy

import math

# TYPES

Player = int
Pos = int           # 1 .. 16
Move = (Pos, Pos)
Cell = int          # 1/-1/0
Board = [[Cell]]

# CONSTANTS
PLAYER1 = 1
PLAYER2 = -1
NEUTRAL = 0
POS_COL = 0
POS_ROW = 1
POSITIONS_MAP = {  # (col,row)
    1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (3, 0),
    5: (4, 0), 6: (4, 1), 7: (4, 2), 8: (4, 3),
    9: (4, 4), 10: (3, 4), 11: (2, 4), 12: (1, 4),
    13: (0, 4), 14: (0, 3), 15: (0, 2), 16: (0, 1) }

## Game logic & board manipulation functions
############################################

def build_board() -> Board:
    return [ [NEUTRAL for col in range(5)]
                for row in range(5) ]

def game_over(board: Board) -> int:
    row = lookup_winning_row(board)
    if row != NEUTRAL:
        return row
    col = lookup_winning_col(board)
    if col  != NEUTRAL:
        return col
    diagonal = lookup_winning_diagonal(board)
    return diagonal

def play(board: Board, player: Player, move: Move):
    orig, dest = move
    col_orig, row_orig = POSITIONS_MAP[orig]
    col_dest, row_dest = POSITIONS_MAP[dest]
    if col_orig == col_dest:
        shift_col(board, player, col_orig, row_orig, row_dest)
    else:
        shift_row(board, player, row_orig, col_orig, col_dest)

def valid_moves_player(board: Board, player: Player) -> [Move]:
    moves = []
    for orig in range(1, 17):
        col, row = POSITIONS_MAP[orig]
        if board[row][col] == -player:
            continue
        moves.extend([ (orig,dest) for dest in range(1, 17)
                if is_valid_move(board, player, (orig,dest)) ])
    return moves

def is_valid_move(board: Board, player: Player, move: Move) -> bool:
    orig, dest = move
    col_orig, row_orig = POSITIONS_MAP[orig]
    col_dest, row_dest = POSITIONS_MAP[dest]
    return  orig > 0 and orig < 17 and \
            dest > 0 and dest < 17 and \
            (board[row_orig][col_orig] == player or board[row_orig][col_orig] == NEUTRAL) and \
            (   (is_corner(orig) and is_corner(dest) and is_opossite_possition(orig,dest)) or
                not is_corner(orig) and (
                    ( is_corner(dest) and (col_dest == col_orig or row_dest == row_orig) ) or
                    ( not is_corner(dest) and is_opossite_possition(orig,dest) )
            ))

def is_corner(pos: Pos) -> bool:
    return pos == 1 or pos == 5 or pos == 9 or pos == 13

def is_opossite_possition(pos1: Pos, pos2: Pos):
    col1, row1 = POSITIONS_MAP[pos1]
    col2, row2 = POSITIONS_MAP[pos2]
    return row1 == row2 and ((col1 == 0 and col2 == 4) or (col1 == 4 and col2 == 0)) or \
            col1 == col2 and ((row1 == 0 and row2 == 4) or (row1 == 4 and row2 == 0))

def shift_row(board: Board, player: Player, row: int, orig: Pos, dest: Pos):
    sense = 1 if orig < dest else -1
    for pos in range(orig, dest, sense):
        board[row][pos] = board[row][pos + sense]
    board[row][dest] = player

def shift_col(board: Board, player: Player, col: int, orig: Pos, dest: Pos):
    sense = 1 if orig < dest else -1
    for pos in range(orig, dest, sense):
        board[pos][col] = board[pos + sense][col]
    board[dest][col] = player

def player_symbol(player: Player) -> str:
    if player == PLAYER1:
        return "X"
    elif player == PLAYER2:
        return "0"

def cell_simbol(cell: Cell) -> str:
    return '-' if cell == NEUTRAL else player_symbol(cell)

def print_board(board: Board):
    for row in board:
        prow = "| "
        for cell in row:
            prow = prow + cell_simbol(cell) + " | "
        print(prow)

def lookup_winning_row(board: Board):
    for r in range(5):
        is_winning_row = True
        row = board[r]
        player = row[0]
        if player != NEUTRAL:
            for cell in row:
                if cell != player:
                    is_winning_row = False
                    break
            if is_winning_row:
                return player
    return NEUTRAL

def lookup_winning_col(board: Board):
    for col in range(5):
        player = board[0][col]
        won = True
        if player != NEUTRAL:
            for row in range(5):
                if board[row][col] != player:
                    won = False
                    break
            if won:
                return player
    return NEUTRAL

def lookup_winning_diagonal(board: Board):
    cell1 = board[0][0]
    cell2 = board[4][0]
    diag1 = cell1 != NEUTRAL and (
                board[1][1] == cell1 and board[2][2] == cell1 and board[3][3] == cell1 and board[4][4] == cell1)
    if diag1:
        return cell1
    diag2 = cell2 != NEUTRAL and (
                board[3][1] == cell2 and board[2][2] == cell2 and board[1][3] == cell2 and board[0][4] == cell2)
    if diag2:
        return cell2
    else :
        return NEUTRAL


# ALPHA BETA PRUNNING
#####################

def alphabeta(game, depth, player, alpha, beta, h) -> (int, Move):
    if depth == 0 or game.game_over():
        return h(game), None

    if player == PLAYER1:
        player_best_value = -math.inf
        player_best_move = None
        valid_moves = valid_moves_player(game.board,PLAYER1)
        for move in valid_moves:
            game_copy = deepcopy(game)
            game_copy._play(PLAYER1, move)
            ab_value, ab_move = alphabeta(game_copy, depth-1, PLAYER2, alpha, beta,h)
            if ab_value > player_best_value:
                player_best_value = ab_value
                player_best_move = move
            alpha = max(alpha,player_best_value)
            if alpha >= beta:
                break
        return player_best_value, player_best_move
    else:
        player_worst_value = math.inf
        player_worst_move = None
        valid_moves = valid_moves_player(game.board,PLAYER2)
        for move in valid_moves:
            game_copy = deepcopy(game)
            game_copy._play(PLAYER2, move)
            ab_value, ab_move = alphabeta(game_copy, depth-1, PLAYER1, alpha, beta, h)
            if ab_value < player_worst_value:
                player_worst_value = ab_value
                player_worst_move = move
            beta = min(beta,player_worst_value)
            if alpha >= beta:
                break
        return player_worst_value, player_worst_move

# TODO: ITERATIVE DEEPENING
def iterative_deep_alphabeta(game, max_depth, player, alpha, beta, h) -> (int, Move):
    best_value, best_move = alphabeta(game, 1, player, alpha, beta, h)
    for depth in range(2,max_depth):
        value, move = alphabeta(game, 1, player, alpha, beta, h)
        if best_value < value:
            best_value = value
            best_move = move
        else : break

    return best_value, best_move



#### CLASSES
############

class Quixo:

    def __init__(self):
        self.current_player = PLAYER1
        self.board = build_board()

    def game_over(self) -> int:
        return game_over(self.board)

    def _play(self, player: Player, move: Move):
        over = self.game_over()
        if over != NEUTRAL:
            raise GameOverException("Game is over. Winner is %s" % over)
        self.current_player = player
        orig,dest = move
        if not is_valid_move(self.board, self.current_player, move):
            raise InvalidMoveError("Ivalid move from %s to %s, for player %s"
                                   % (orig, dest, player_symbol(self.current_player)))
        play(self.board, self.current_player, move)

class QuixoPlayerWyry(Quixo):

    def __init__(self, h, depth):
        self.h = h
        self.depth = depth
        super().__init__()

    def playerPlay(self) -> Move:
        _,move = iterative_deep_alphabeta(self, self.depth, PLAYER1, -math.inf, math.inf, self.h)
        # _,move = alphabeta(self, self.depth, PLAYER1, -math.inf, math.inf, self.h)
        self._play(PLAYER1,move)
        return move

    def oponentPlay(self, move: Move):
        self._play(PLAYER2, move)

# EXCEPTIONS
############

class QuixoError(Exception):
    pass
class GameOverException(Exception):
    pass
class DrawGameError(QuixoError):
    pass
class InvalidMoveError(QuixoError):
    pass


# HEURISTICS
############

def h_potentially_improving_lines_overdosed(game: Quixo):
    over = game.game_over()
    if over:
        return 1000 if over == game.current_player else -1
    player = game.current_player
    board = game.board
    lenght_weights = {1: 1, 2: 2, 3: 4, 4: 8 }
    sum_current_player = sum_potentially_improving_lines_player(board, lenght_weights, player)
    discount = 0
    if sum_current_player > 0 :
        sum_oponent = sum_potentially_improving_lines_player(board, lenght_weights, -player)
        if sum_oponent > sum_current_player:
            diff = sum_oponent - sum_current_player
            discount = diff*100/sum_current_player
            discount = sum_current_player*discount/100
    return sum_current_player-discount

def h_potentially_improving_lines(game: Quixo):
    over = game.game_over()
    if over:
        return 1000 if over == game.current_player else -1
    player = game.current_player
    board = game.board
    lenght_weights = {1: 1, 2: 2, 3: 4, 4: 8 }
    return sum_potentially_improving_lines_player(board, lenght_weights, player)

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

def sum_potentially_improving_lines_player(board, lenght_weights, player):
    sum = 0
    for col_or_row in range(5):
        found_row, found_col = False, False
        for length in range(4, 1, -1):
            if not found_col and is_one_move_improvable_col(board, col_or_row, length, player):
                found_col = True
                sum += lenght_weights[length]
            if not found_row and is_one_move_improvable_row(board, col_or_row, length, player):
                found_row = True
                sum += lenght_weights[length]
    found_diag_desc, found_diag_asc = False, False
    for length in range(4, 1, -1):
        # Las diagonales suman un poco más porque pueden mejorar a traves de 4 casilleros en vez de 2 como las lineas
        # horizontales y verticales
        if not found_diag_asc and is_one_move_improvable_diag_asc(board, length, player):
            found_diag_asc = True
            sum += lenght_weights[length] * 1.5
        if not found_diag_desc and is_one_move_improvable_diag_desc(board, length, player):
            found_diag_desc = True
            sum += lenght_weights[length] * 1.5
    return sum

