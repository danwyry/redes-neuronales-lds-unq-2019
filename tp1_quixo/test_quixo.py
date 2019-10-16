import unittest
from tp1_quixo.quixo import build_board, is_opossite_possition, NEUTRAL, is_corner, is_valid_move, PLAYER1, PLAYER2, play

class TestQuixo(unittest.TestCase):

    def test_build_board_is_5_x_5_matrix_when_built(self):
        board = build_board()
        self.assertEqual(len(board), 5)
        for row in board:
            self.assertEqual(len(row), 5)

    def test_board_is_all_neutrals_when_built(self):
        board = build_board()
        for row in board:
            for cell in row:
                self.assertEqual(cell, NEUTRAL)

    def test_is_corner(self):
        self.assertTrue(is_corner(1))
        self.assertTrue(is_corner(5))
        self.assertTrue(is_corner(9))
        self.assertTrue(is_corner(13))

    def test_not_is_corner(self):
        self.assertFalse(is_corner(2))
        self.assertFalse(is_corner(3))
        self.assertFalse(is_corner(4))
        self.assertFalse(is_corner(6))
        self.assertFalse(is_corner(7))
        self.assertFalse(is_corner(8))
        self.assertFalse(is_corner(10))
        self.assertFalse(is_corner(11))
        self.assertFalse(is_corner(12))
        self.assertFalse(is_corner(14))
        self.assertFalse(is_corner(15))
        self.assertFalse(is_corner(16))

    def test_not_is_opossite_position(self):
        self.assertFalse(is_opossite_possition(1,2))
        self.assertFalse(is_opossite_possition(1,3))
        self.assertFalse(is_opossite_possition(1,4))
        self.assertFalse(is_opossite_possition(1,6))
        self.assertFalse(is_opossite_possition(1,7))
        self.assertFalse(is_opossite_possition(1,8))
        self.assertFalse(is_opossite_possition(1,9))
        self.assertFalse(is_opossite_possition(1,10))
        self.assertFalse(is_opossite_possition(1,11))
        self.assertFalse(is_opossite_possition(1,12))
        self.assertFalse(is_opossite_possition(1,14))
        self.assertFalse(is_opossite_possition(1,15))
        self.assertFalse(is_opossite_possition(2,3))
        self.assertFalse(is_opossite_possition(2,4))
        self.assertFalse(is_opossite_possition(2,5))
        self.assertFalse(is_opossite_possition(2,6))
        self.assertFalse(is_opossite_possition(2,7))
        self.assertFalse(is_opossite_possition(2,8))
        self.assertFalse(is_opossite_possition(2,9))
        self.assertFalse(is_opossite_possition(2,10))
        self.assertFalse(is_opossite_possition(2,11))
        self.assertFalse(is_opossite_possition(2,14))
        self.assertFalse(is_opossite_possition(2,15))

    def test_is_opossite_position(self):
        self.assertTrue(is_opossite_possition(1,5))
        self.assertTrue(is_opossite_possition(1,13))
        self.assertTrue(is_opossite_possition(5,9))
        self.assertTrue(is_opossite_possition(9,13))
        self.assertTrue(is_opossite_possition(2,12))
        self.assertTrue(is_opossite_possition(3,11))
        self.assertTrue(is_opossite_possition(4,10))
        self.assertTrue(is_opossite_possition(6,16))
        self.assertTrue(is_opossite_possition(7,15))
        self.assertTrue(is_opossite_possition(8,14))

    def test_is_valid_move_if_orig_has_neutral_piece(self):
        player = PLAYER1
        board = build_board()
        self.assertTrue(is_valid_move(board, player, (1, 5)))

    def test_is_valid_move_if_orig_has_same_player_piece(self):
        player = PLAYER1
        board = build_board()
        play(board, player, (1, 5))
        self.assertTrue(is_valid_move(board, player, (1, 5)))

    def test_not_is_valid_move_if_orig_has_other_player_piece(self):
        player = PLAYER1
        other_player = PLAYER2
        board = build_board()
        play(board, other_player, (1, 5))
        self.assertFalse(is_valid_move(board,player,(5,1)))

    def test_not_is_valid_move_if_orig_and_dest_dont_match_either_row_or_column(self):
        player = PLAYER1
        board = build_board()
        self.assertFalse(is_valid_move(board,player,(1,6)))
        self.assertFalse(is_valid_move(board,player,(1,7)))
        self.assertFalse(is_valid_move(board,player,(1,8)))
        self.assertFalse(is_valid_move(board,player,(1,9)))
        self.assertFalse(is_valid_move(board,player,(1,10)))
        self.assertFalse(is_valid_move(board,player,(1,11)))
        self.assertFalse(is_valid_move(board,player,(1,12)))

    def test_is_valid_move_if_orig_and_dest_match_either_row_or_column(self):
        player = PLAYER1
        board = build_board()
        self.assertTrue(is_valid_move(board,player,(1,5)))
        self.assertTrue(is_valid_move(board,player,(1,13)))

    def test_not_is_valid_move_if_orig_is_corner_and_dest_not_in_corner_and_not_opposites(self):
        player = PLAYER1
        board = build_board()
        self.assertFalse(is_valid_move(board, player, (1, 2)))
        self.assertFalse(is_valid_move(board, player, (2, 3)))
        self.assertFalse(is_valid_move(board, player, (2, 4)))
        self.assertFalse(is_valid_move(board, player, (6, 13)))




    #  1  2  3  4  5
    # 16           6
    # 15           7
    # 14           8
    # 13 12 11 10  9

