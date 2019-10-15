# Types
PLAYER = int
POS = int  # from 1 to 16
MOVE = (POS, POS)
CELL = int  # 1 , -1 , 0
BOARD = [[CELL]]

class Quixo:
    P1 =  1
    P2 = -1
    Neutral = 0
    POS_COL = 0
    POS_ROW = 1
    positions_map = {
        # (col,row)
        1: (0,0), 2: (1,0), 3: (2,0), 4: (3,0),
        5: (4,0), 6: (4,1), 7: (4,2), 8: (4,3),
        9: (4,4), 10: (3,4), 11: (2,4), 12: (1,4),
        13: (0,4), 14: (0,3), 15: (0,2), 16: (0,1)
    }

    @staticmethod
    def build_board() -> BOARD:
        return [
            [Quixo.Neutral for col in range(5)]
            for row in range(5)
        ]

    @staticmethod
    def same_col(orig: POS, dest: POS) -> bool:
        return Quixo.positions_map[orig][Quixo.POS_COL] == Quixo.positions_map[dest][Quixo.POS_COL]

    @staticmethod
    def same_row(orig: POS, dest: POS) -> bool:
        return Quixo.positions_map[orig][Quixo.POS_ROW] == Quixo.positions_map[dest][Quixo.POS_ROW]

    @staticmethod
    def is_corner(pos: POS) -> bool:
        return pos == 1 or pos == 5 or pos == 9 or pos == 13

    @staticmethod
    def is_valid_move(board: BOARD, player: PLAYER, move: MOVE) -> bool:
        orig, dest = move
        col,row = Quixo.positions_map[orig]
        return orig > 0 and orig < 21 and \
                dest > 0 and dest < 21 and \
                (Quixo.same_row(orig, dest) or Quixo.same_col(orig, dest)) and \
                (board[row][col] == player or board[row][col] == Quixo.Neutral)
        # (not Quixo.is_corner(orig) or
                #     orig != dest and Quixo.is_corner(orig)) and \

    @staticmethod
    def list_valid_moves(board: BOARD, player: PLAYER):
        return [move for move in range(1, 17) if Quixo.is_valid_move(board, player, move)]

    @staticmethod
    def play(board: BOARD, player: PLAYER, move: MOVE):
        orig, dest = move
        if not Quixo.is_valid_move(board, player, move):
            raise InvalidMoveError("Ivalid move from %s to %s, for player %s"
                                   % (orig, dest, Quixo.player_simbol(player)))
        col_orig, row_orig = Quixo.positions_map[orig]
        col_dest, row_dest = Quixo.positions_map[dest]
        if col_orig == col_dest:
            Quixo.shift_col(board, player, col_orig, row_orig, row_dest)
        else:
            Quixo.shift_row(board, player, row_orig, col_orig, col_dest)

    @staticmethod
    def shift_row(board: BOARD, player:PLAYER, row: int, orig: int, dest: int):
        sense = 1 if orig < dest else -1
        for pos in range(orig,dest,sense):
            board[row][pos] = board[row][pos + sense]
        board[row][dest] = player

    @staticmethod
    def shift_col(board: BOARD, player: PLAYER, col: int, orig: int, dest: int):
        sense = 1 if orig < dest else -1
        for pos in range(orig, dest, sense):
            board[pos][col] = board[pos + sense][col]
        board[dest][col] = player

    def __init__(self):
        self.current_player = Quixo.P1
        self.board = Quixo.build_board()

    def valid_moves(self) -> [MOVE]:
        return Quixo.list_valid_moves(self.board, self.current_player)

    def playerPlay(self, move: MOVE):
        self.current_player = Quixo.P1
        return Quixo.play(self.board, self.current_player, move)

    def oponentPlay(self, move: MOVE):
        self.current_player = Quixo.P2
        return Quixo.play(self.board, self.current_player, move)

def print_board(board):
    for row in board:
        prow = "| "
        for cell in row:
            p
            prow += player_simbol(cell) + " | "
        print(prow + "\n")

def player_simbol(player):
    if player == Quixo.P1:
        return "X"
    elif player == Quixo.P2:
        return  "0"
    else:
        return "-"


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


class QuixoError(Exception):
    pass

class DrawGameError(QuixoError):
    pass

class InvalidMoveError(QuixoError):
    pass

