
"""
CORNER STRAGETY
"""

# - find_best_move: Ermittelt den besten Zug basierend auf der Heuristik.
# - find_best_move_random_agent: Wählt zufällig einen Zug aus.
# - execute_move: Führt einen bestimmten Zug aus.
# - board_equals: Vergleicht zwei Spielbretter auf Gleichheit.
# - heuristic_score: Bewertet ein Spielfeld nach bestimmten Kriterien.


import random
import game
import sys
import numpy as np

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def find_best_move(board):
    best_move = None
    best_score = float('-inf')

    for move in [UP, DOWN, LEFT, RIGHT]:
        newboard = execute_move(move, board)

        if board_equals(board, newboard):
            continue

        score = heuristic_score(newboard)

        if score > best_score:
            best_score = score
            best_move = move

    if best_move is None:
        return find_best_move_random_agent()

    return best_move

def find_best_move_random_agent():
    return random.choice([UP, DOWN, LEFT, RIGHT])

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
