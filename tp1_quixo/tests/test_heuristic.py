from tp1_quixo.heuristic_potentially_improving_lines import h_potentially_improving_lines


class Game:
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    current_player = 1

# print(is_one_move_improvable_diag_asc(Game.board,4,1))
print(h_potentially_improving_lines(Game))
# print(is_one_move_improvable_row(Game.board,0,4,1))
# print(is_one_move_improvable_row(Game.board,0,3,1))
# print(is_one_move_improvable_row(Game.board,0,2,1))
#
# def is_improvable_diagonal(board, l, pl, direction = 1):
#     i = l
#     f = False
#     col = 0
#     row = 0 if direction == 1 else 4
#     s = 0
#     while col <= 4:
#         prev_row = row - 1 if col_or_row > 0 else 4
#         next_row = col_or_row + 1 if col_or_row < 4 else 0
#         if not f:
#             if board[col_or_row][col_or_row] == pl:
#                 col_or_row += 1
#                 l -= 1
#             elif board[prev_row][col_or_row] == pl or board[next_row][col_or_row] == pl:
#                 f = True
#                 s = 0
#                 col_or_row += 1
#             else:
#                 col_or_row += 1
#                 l = i
#         else:
#             if l == s:
#                 return True
#             if 5 - col_or_row < l - s:
#                 return False
#             elif pl == board[col_or_row][col_or_row]:
#                 s += 1
#                 col_or_row += 1
#             else:
#                 f = False
#                 l = i
#
#     return (f and l == 0) or (f and l == s)


# class TestQuixoHeuristic(unittest.TestCase):
    #
    # def test_rows_with_line_len(self):
    #     b = build_board()
    #     b[0] = [0, 1, 1, 1, 0]
    #     b[1] = [0, -1, 1, 1, 0]
    #     self.assertListEqual(rows_with_line_len(b, 3),[(0,1)])
    #     self.assertListEqual(rows_with_line_len(b, 2),[(0,1),(1,1)])
    #
    # def test_cols_with_line_len(self):
    #     board = []
    #     board[0] = [0, 1, 0, 1, 0]
    #     board[1] = [0, 1, 0, 0, 0]
    #     board[2] = [0, 1, 0, 1, 0]
    #     board[3] = [0, 1, 0, 1, 0]
    #     board[4] = [0, 0, 0, 1, 0]
    #     self.assertListEqual(cols_with_line_len(board, 4),[1])
    #     self.assertListEqual(cols_with_line_len(board, 3),[1,3])




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


    #  1  2  3  4  5
    # 16           6
    # 15           7
    # 14           8
    # 13 12 11 10  9

