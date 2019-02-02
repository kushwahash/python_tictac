import unittest
import tic_tac

class TestTicTacToe(unittest.TestCase):
    def test_full_board(self):
        board = ['#','X','O','X','O','X','O','X','O']
        ans = tic_tac.full_board_check(board)
        self.assertTrue(ans)


if __name__ == '__main__':
    unittest.main()

