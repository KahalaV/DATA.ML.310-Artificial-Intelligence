"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #if the number of markers is zero or an even number return X, otherwise return O
    markers = 0
    for row in board:
        markers += row.count(X)
        markers += row.count(O)
    if markers == 0 or markers % 2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionsSet.append((i, j))

    return actionsSet

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = deepcopy(board)
    playerTurn = player(newBoard)
    xCoord, yCoord = action
    
    #if the cell is already filled, raise exception
    if newBoard[xCoord][yCoord] != EMPTY:
        raise Exception

    #if the action is legal, return new board
    else:
        newBoard[xCoord][yCoord] = playerTurn
        return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for p in (X, O):
        #check horizontal
        for row in board:
            if 3 * [p] == row:
                return p

        #check vertical
        for i in range(3):
            col = [board[0][i], board[1][i], board[2][i]]
            if 3 * [p] == col:
                return p

        #check diagonal
        if 3 * [p] == [board[0][0], board[1][1], board[2][2]]:
            return p
        elif 3 * [p] == [board[2][0], board[1][1], board[0][2]]:
            return p

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check for winner
    if winner(board) != None:
        return True

    #check if the board is full and no winner
    markers = 0
    for row in board:
        markers += row.count(X)
        markers += row.count(O)
    if markers >= 9:
        return True

    #else return false
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
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

    #return none if terminal
    if terminal(board):
        return None

    #define functions that return the best possible value and the associated action
    def max(board):
        if terminal(board):
            return utility(board), ()
        else:
            value = -math.inf
            for action in actions(board):
                minValue = min(result(board, action))[0]
                if minValue > value:
                    value = minValue
                    optimalAction = action
            return value, optimalAction

    def min(board):
        if terminal(board):
            return utility(board), ()
        else:
            value = math.inf
            for action in actions(board):
                maxValue = max(result(board, action))[0]
                if maxValue < value:
                    value = maxValue
                    optimalAction = action
            return value, optimalAction

    #return optimal action depending on the current player turn
    if player(board) == X:
        return max(board)[1]

    else:
        return min(board)[1]