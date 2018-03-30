import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from game_state import GameState
from board import Board

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.gameState = GameState();
        self.board = Board();

    def test_finished(self):
        self.assertEqual( self.gameState.finished(self.board), False )

    def test_check_win(self):
        self.assertEqual( self.gameState.check_win(self.board), False )

    def test_check_win_combination_one_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[0], self.board), False)

    def test_check_win_combination_two_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[1], self.board), False)

    def test_check_win_combination_three_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[2], self.board), False)

    def test_check_win_combination_four_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[3], self.board), False)

    def test_check_win_combination_five_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[4], self.board), False)

    def test_check_win_combination_six_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[5], self.board), False)

    def test_check_win_combination_seven_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[6], self.board), False)

    def test_check_win_combination_eight_state(self):
        self.assertEqual( self.gameState.check_combination_state(self.board.win_combinations[7],self.board), False)

    def test_check_tie(self):
        self.assertEqual( self.gameState.tie(self.board), False)

if __name__ == '__main__':
    unittest.main()
