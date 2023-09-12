"""
MINIMAX STRATEGY
"""

# Die Funktion find_best_move verwendet einen Minimax-Algorithmus, um den besten Zug zu finden.
# Der Minimax-Algorithmus berücksichtigt Züge bis zu einer festgelegten Tiefe (DEPTH_LIMIT).
# execute_move führt den ausgewählten Zug auf dem Spielbrett aus.
# board_equals überprüft, ob zwei Spielbretter gleich sind.
# heuristic_score bewertet ein Spielbrett anhand einer Heuristik, um Züge zu priorisieren.


import random
import game
import sys
import numpy as np

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
DEPTH_LIMIT = 3

def find_best_move(board):
    _, best_move = minimax(board, DEPTH_LIMIT, True)
    return best_move

def minimax(board, depth, is_maximizing_player):
    if depth == 0 or game.is_terminal(board):
        return heuristic_score(board), None
    
    best_move = None
    if is_maximizing_player:
        max_eval = float('-inf')
        for move in [UP, DOWN, LEFT, RIGHT]:
            newboard = execute_move(move, board)
            if not board_equals(board, newboard):
                eval, _ = minimax(newboard, depth-1, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in [UP, DOWN, LEFT, RIGHT]:
            newboard = execute_move(move, board)
            if not board_equals(board, newboard):
                eval, _ = minimax(newboard, depth-1, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
        return min_eval, best_move

def execute_move(move, board):
    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")

def board_equals(board, newboard):
    return (newboard == board).all()

def heuristic_score(board):
    corner_weight = board[0, 0] * 4
    cells_around_corner_weight = -np.sum(board[0:2, 0:2] == 0) * 10
    merge_count_weight = np.sum(board > 0) * 3
    return corner_weight + cells_around_corner_weight + merge_count_weight
