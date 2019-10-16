# Types
Player = int
Pos = int  # from 1 to 16
Move = (Pos, Pos)
Cell = int  # 1 , -1 , 0
Board = [[Cell]]

# Constants
PLAYER1 = 1
PLAYER2 = -1
NEUTRAL = 0
POS_COL = 0
POS_ROW = 1
POSITIONS_MAP = {  # (col,row)
    1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (3, 0),
    5: (4, 0), 6: (4, 1), 7: (4, 2), 8: (4, 3),
    9: (4, 4), 10: (3, 4), 11: (2, 4), 12: (1, 4),
    13: (0, 4), 14: (0, 3), 15: (0, 2), 16: (0, 1)
}

def build_board() -> Board:
    return [
        [NEUTRAL for col in range(5)]
        for row in range(5)
    ]

def is_corner(pos: Pos) -> bool:
    return pos == 1 or pos == 5 or pos == 9 or pos == 13

def is_opossite(a: int,b: int) -> bool:
    return a == 0 and b == 4 or a == 4 and b == 0

def is_opossite_possition(pos1: Pos, pos2: Pos):
    col1, row1 = POSITIONS_MAP[pos1]
    col2, row2 = POSITIONS_MAP[pos2]
    return row1 == row2 and ((col1 == 0 and col2 == 4) or (col1 == 4 and col2 == 0)) or \
            col1 == col2 and ((row1 == 0 and row2 == 4) or (row1 == 4 and row2 == 0))

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

def valid_moves_player(board: Board, player: Player) -> [Move]:
    moves = []
    for orig in range(1, 17):
        col, row = POSITIONS_MAP[orig]
        if board[row][col] == -player:
            continue
        moves.extend([ (orig,dest) for dest in range(1, 17)
                if is_valid_move(board, player, (orig,dest)) ])
    return moves

def play(board: Board, player: Player, move: Move):
    orig, dest = move
    if not is_valid_move(board, player, move):
        raise InvalidMoveError("Ivalid move from %s to %s, for player %s"
                               % (orig, dest, player_simbol(player)))
    col_orig, row_orig = POSITIONS_MAP[orig]
    col_dest, row_dest = POSITIONS_MAP[dest]
    if col_orig == col_dest:
        shift_col(board, player, col_orig, row_orig, row_dest)
    else:
        shift_row(board, player, row_orig, col_orig, col_dest)

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

class Quixo:
    def __init__(self):
        self.current_player = PLAYER1
        self.board = build_board()

    def valid_moves(self) -> [Move]:
        return valid_moves_player(self.board, self.current_player)

    def playerPlay(self, move: Move):
        self.current_player = PLAYER1
        return play(self.board, self.current_player, move)

    def oponentPlay(self, move: Move):
        self.current_player = PLAYER2
        return play(self.board, self.current_player, move)

class QuixoError(Exception):
    pass

class DrawGameError(QuixoError):
    pass

class InvalidMoveError(QuixoError):
    pass

    #  0  1  2  3  4
    #  -  -  -  -  -  0
    #  -  -  -  -  -  1
    #  -  -  -  -  -  2
    #  -  -  -  -  -  3
    #  -  -  -  -  -  4

    #  0  1  2  3  4
    #  .  .  .  .  .
    #  1  2  3  4  5  . 0
    # 16           6  . 1
    # 15           7  . 2
    # 14           8  . 3
    # 13 12 11 10  9  . 4
