#---------------------- TIC TAC TOE ----------------------
import random

theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# This function prints out the board that it was passed
# "board" is a list of 10 strings representing the board
def drawBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' |  ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def drawKey():
    print('The board is laid out as follows:')
    print('     |     |   ')
    print('  1  |  2  |  3')
    print('     |     |   ')
    print('---------------')
    print('     |     |   ')
    print('  4  |  5  |  6')
    print('     |     |   ')
    print('---------------')
    print('     |     |   ')
    print('  7  |  8  |  9')
    print('     |     |   ')
    

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
            #[player, computer]
        elif letter != 'X' and letter!= 'O':
            print('That\'s not a choice!')
        else:
            return ['X', 'O']
            #[computer, player]

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'Computer goes first'
    else:
        return 'Player goes first'

def makeMove(board, letter, move):
    board[move] = letter

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
 #   else:
#        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
       playerLetter = 'X'

    # Tic Tac Toe core logic:
    # Check if the computer can win in the next move
    for i in range (1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player can win on their next move, and block them.
    for i in range (1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    #Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    #Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Else, return False.
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

# This function returns True if the player wants to play again, otherwise it returns False.
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#drawBoard(theBoard)

# The start of the game
print('Welcome to Tic Tac Toe!')
drawKey()

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst()
    print (turn)
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player goes first':
            # Running the Player's Turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Computer goes first'
        else:
            # Running the Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player goes first'
    if not playAgain():
        break