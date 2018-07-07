#---------------------- TIC TAC TOE ----------------------
import random

theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# This function prints out the board that it was passed
# "board" is a list of 10 strings representing the board
def printBoard(board):
    print('   |   |')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        if letter == 'X:'
            return ['Player: X', 'Computer: O']
        else:
            return ['Computer: X', 'Player: O']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'Computer goes first'
    else:
        return 'Player goes first'

def makeMove(board, letter, move):
    boad[move] = letter

# This function checks the list "board" for winning scenarios
# b = board and l = letter
def isWinner(b, l):
    return (
    (b[7] == l and b[8] == l and b[9] == l) or # top row
    (b[4] == l and b[5] == l and b[6] == l) or # middle row
    (b[1] == l and b[2] == l and b[3] == l) or # bottom row
    (b[7] == l and b[4] == l and b[1] == l) or # left column
    (b[8] == l and b[5] == l and b[2] == l) or # mid column
    (b[9] == l and b[6] == l and b[3] == l) or # right column
    (b[7] == l and b[5] == l and b[3] == l) or # diagonal 1
    (b[9] == l and b[5] == l and b[1] == l)    # diagonal 2
    )

# Safest way to return board information. Original board is replicated in dupeBoard and then returned
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
        return dupeBoard

# Returns true if the passed move if space is free
def isSpaceFree(board, move):
    return board[move] == ' '

# Asks the player for their move
def getPlayerMove(board):
    move = ' '
    # Is there a more straightforward way to represent this?
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# This function returns True if the player wants to play again, otherwise it returns False.
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

printBoard(theBoard)