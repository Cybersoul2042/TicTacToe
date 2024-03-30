"""
Tic Tac Toe Player
"""

import math
import copy
import termios

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    
    return board

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        user = X
    else:
        xCount = 0
        oCount = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == X:
                    xCount += 1
                elif board[i][j] == O:
                    oCount += 1
        if xCount > oCount:
            user = O
        else:
            user = X
    return user


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    player_actions = set()
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                move = (i, j)
                player_actions.add(move)
    
    return player_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    i, j = action
    if action not in actions(board):
        raise ValueError("Not a correct move")
    else:
        nBoard = copy.deepcopy(board)
        if player(board) == X:
            nBoard[i][j] = X
        elif player(board) == O:
            nBoard[i][j] = O

        return nBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[0][i]) == (board[1][i]) == (board[2][i]) != None:
            return board[0][i]
    for i in range(len(board)):
        if (board[i][0]) == (board[i][1]) == (board[i][2])  != None:
            return board[i][0]
    if (board[0][0]) == (board[1][1]) == (board[2][2]) != None or (board[0][2]) == (board[1][1]) == (board[2][0]) != None:
        return board[1][1]
    else:
        return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(terminal(board) == True):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None 
    else:
        best_move = (1, 1)
        if player(board) == X:
            if board == initial_state():
                return best_move
            val = -math.inf
            for i in actions(board):
                nVal = min_val(result(board, i))
                if val < nVal:
                    val = nVal
                    best_move = i
        else:
            if board == initial_state():
                return best_move
            val = math.inf
            for i in actions(board):
                nVal = max_val(result(board, i))
                if val > nVal:
                    val = nVal
                    best_move = i
        return best_move
    
def min_val(board):
    if terminal(board):
        return utility(board)
    val = math.inf
    for action in actions(board):
        val = min(val, max_val(result(board, action)))
    return val

def max_val(board):
    if terminal(board):
        return utility(board)
    val = -math.inf
    for action in actions(board):
        val = max(val, min_val(result(board, action)))
    return val
