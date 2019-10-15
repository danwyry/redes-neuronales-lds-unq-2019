import unittest
from tp1_quixo.quixo import Quixo

class TestQuixoBoard(unittest.TestCase):

    def test_build_board_is_5_x_5_matrix(self):
        board = Quixo.build_board()
        self.assertEqual(len(board), 5)
        for row in board:
            self.assertEqual(len(row), 5)

    def test_board_is_all_neutrals(self):
        board = Quixo.build_board()
        for row in board:
            for cell in row:
                self.assertEqual(cell, Quixo.Neutral)

    def test_same_row_for_positions_in_same_rows_are_true(self):
        self.assertTrue(Quixo.same_row(1,2))
        self.assertTrue(Quixo.same_row(1,3))
        self.assertTrue(Quixo.same_row(1,4))
        self.assertTrue(Quixo.same_row(1,5))
        self.assertTrue(Quixo.same_row(16,6))
        self.assertTrue(Quixo.same_row(15,7))
        self.assertTrue(Quixo.same_row(14,8))
        self.assertTrue(Quixo.same_row(13,9))
        self.assertTrue(Quixo.same_row(13,10))
        self.assertTrue(Quixo.same_row(13,11))
        self.assertTrue(Quixo.same_row(13,12))

    def test_same_row_for_positions_in_different_rows_are_false(self):
        self.assertFalse(Quixo.same_row(1,16))
        self.assertFalse(Quixo.same_row(1,15))
        self.assertFalse(Quixo.same_row(1,14))
        self.assertFalse(Quixo.same_row(1,13))
        self.assertFalse(Quixo.same_row(5,6))
        self.assertFalse(Quixo.same_row(5,7))
        self.assertFalse(Quixo.same_row(5,8))
        self.assertFalse(Quixo.same_row(5,9))

    def test_same_col_for_positions_in_same_columns_are_true(self):
        self.assertTrue(Quixo.same_col(1,16))
        self.assertTrue(Quixo.same_col(1,15))
        self.assertTrue(Quixo.same_col(1,14))
        self.assertTrue(Quixo.same_col(1,13))
        self.assertTrue(Quixo.same_col(5,6))
        self.assertTrue(Quixo.same_col(5,7))
        self.assertTrue(Quixo.same_col(5,8))
        self.assertTrue(Quixo.same_col(5,9))

    def test_same_col_for_positions_in_different_columns_are_false(self):
        self.assertFalse(Quixo.same_col(1,2))
        self.assertFalse(Quixo.same_col(1,3))
        self.assertFalse(Quixo.same_col(1,4))
        self.assertFalse(Quixo.same_col(1,5))
        self.assertFalse(Quixo.same_col(13,12))
        self.assertFalse(Quixo.same_col(13,11))
        self.assertFalse(Quixo.same_col(13,10))
        self.assertFalse(Quixo.same_col(13,9))

    def test_is_corner(self):
        self.assertTrue(Quixo.is_corner(1))
        self.assertTrue(Quixo.is_corner(5))
        self.assertTrue(Quixo.is_corner(9))
        self.assertTrue(Quixo.is_corner(13))

    def test_not_is_corner(self):
        self.assertFalse(Quixo.is_corner(2))
        self.assertFalse(Quixo.is_corner(3))
        self.assertFalse(Quixo.is_corner(4))
        self.assertFalse(Quixo.is_corner(6))
        self.assertFalse(Quixo.is_corner(7))
        self.assertFalse(Quixo.is_corner(8))
        self.assertFalse(Quixo.is_corner(10))
        self.assertFalse(Quixo.is_corner(11))
        self.assertFalse(Quixo.is_corner(12))
        self.assertFalse(Quixo.is_corner(14))
        self.assertFalse(Quixo.is_corner(15))
        self.assertFalse(Quixo.is_corner(16))

    def test_is_valid_move_if_orig_has_neutral_piece(self):
        player = Quixo.P1
        board = Quixo.build_board()
        self.assertTrue(Quixo.is_valid_move(board, player, (1, 1)))

    def test_is_valid_move_if_orig_has_same_player_piece(self):
        player = Quixo.P1
        board = Quixo.build_board()
        Quixo.play(board, player, (1, 1))
        self.assertTrue(Quixo.is_valid_move(board, player, (1, 1)))

    def test_not_is_valid_move_if_orig_has_other_player_piece(self):
        player = Quixo.P1
        other_player = Quixo.P2
        board = Quixo.build_board()
        Quixo.play(board, other_player, (1, 1))
        self.assertFalse(Quixo.is_valid_move(board,player,(1,5)))

    def test_not_is_valid_move_if_orig_and_dest_dont_match_either_row_or_column(self):
        player = Quixo.P1
        board = Quixo.build_board()
        self.assertFalse(Quixo.is_valid_move(board,player,(1,6)))
        self.assertFalse(Quixo.is_valid_move(board,player,(1,7)))
        self.assertFalse(Quixo.is_valid_move(board,player,(1,8)))
        self.assertFalse(Quixo.is_valid_move(board,player,(1,9)))
        self.assertFalse(Quixo.is_valid_move(board,player,(1,10)))
        self.assertFalse(Quixo.is_valid_move(board,player,(1,11)))
        self.assertFalse(Quixo.is_valid_move(board,player,(1,12)))

    def test_is_valid_move_if_orig_and_dest_match_either_row_or_column(self):
        player = Quixo.P1
        board = Quixo.build_board()
        self.assertTrue(Quixo.is_valid_move(board,player,(1,5)))
        self.assertTrue(Quixo.is_valid_move(board,player,(1,13)))

    #  1  2  3  4  5
    # 16           6
    # 15           7
    # 14           8
    # 13 12 11 10  9

