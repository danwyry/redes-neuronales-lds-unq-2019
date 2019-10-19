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

def build_board() -> Board:
    return [ [NEUTRAL for col in range(5)]
                for row in range(5) ]

def game_over(board: Board) -> bool:
    if lookup_winning_row(board):
        return True
    if lookup_winning_col(board):
        return True
    return any_winning_diagonal(board)

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

def player_simbol(player: Player) -> str:
    if player == PLAYER1:
        return "X"
    elif player == PLAYER2:
        return "0"

def cell_simbol(cell: Cell) -> str:
    return '-' if cell == NEUTRAL else player_simbol(cell)

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
                return (r, player)
    return None

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
                return (col,player)
    return None

def any_winning_diagonal(board: Board):
    cell1 = board[0][0]
    cell2 = board[4][0]
    return (
        cell1 != NEUTRAL and (
            board[1][1] == cell1 and board[2][2] == cell1 and
            board[3][3] == cell1 and board[4][4] == cell1 )) or \
       cell2 != NEUTRAL and (
            board[3][1] == cell2 and board[2][2] == cell2 and
            board[1][3] == cell2 and board[0][4] == cell2 )

class Quixo:
    def __init__(self):
        self.current_player = PLAYER1
        self.board = build_board()

    def valid_moves(self) -> [Move]:
        return valid_moves_player(self.board, self.current_player)

    def playerPlay(self, move: Move):
        return play(PLAYER1, move)

    def oponentPlay(self, move: Move):
        return self.play(PLAYER2, move)

    def play(self, player: Player, move: Move):
        self.current_player = player
        orig,dest = move
        if not is_valid_move(self.board, self.current_player, move):
            raise InvalidMoveError("Ivalid move from %s to %s, for player %s"
                                   % (orig, dest, player_simbol(self.current_player)))
        return play(self.board, self.current_player, move)

class QuixoError(Exception):
    pass

class DrawGameError(QuixoError):
    pass

class InvalidMoveError(QuixoError):
    pass

class QuixoHeuristic(Quixo):
    def evaluate(self) -> int:
        return 0


    # 0  1  2  3  4
    # -  -  -  -  -  0
    # -  -  -  -  -  1
    # -  -  -  -  -  2
    # -  -  -  -  -  3
    # -  -  -  -  -  4

    # 0  1  2  3  4
    # .  .  .  .  .
    #  1  2  3  4  5  . 0
    # 16           6  . 1
    # 15           7  . 2
    # 14           8  . 3
    # 13 12 11 10  9  . 4
