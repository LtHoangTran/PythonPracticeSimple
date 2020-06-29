# define the board
board = ['-','-','-',
         '-','-','-',
         '-','-','-']

gameStillGoing = True
winner = None
currentPlayer='X'

# display the board
def displayBoard():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])


# handle turn
def handleTurn(player):
    print('Turn of ' + player)
    position = input('Choose a position from 1 to 9: ')
    
    valid = False
    while not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Invalid input. Please input again: ')
        position = int(position)-1   
        if board[position] == '-':
            valid = True
        else:
            print('Cell has been filled. You can fill there.')
        
    board[position] = player
    displayBoard()
    print('')

# check if game is over
def checkIfGameOver():
    checkIfWin()
    checkIfTie()

# check rows for end game
def checkRows():
    global gameStillGoing
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        gameStillGoing = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

# check columns for end game
def checkColumns():
    global gameStillGoing
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1 or column2 or column3:
        gameStillGoing = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

# check diagonals for end game
def checkDiagonals():
    global gameStillGoing
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        gameStillGoing = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return
    
# check if win:
def checkIfWin():
    global winner
    
    # check rows
    rowWinner = checkRows()
    # check columns
    columnWinner = checkColumns()
    # check diagonals
    diagonalWinner = checkDiagonals()

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None
    return

# check if tie
def checkIfTie():
    global winner
    global gameStillGoing
    if '-' not in board:
        gameStillGoing = False
    return

# play game
def playGame():
    displayBoard()
    while gameStillGoing:
        handleTurn(currentPlayer)
        checkIfGameOver()
        flipPlayer()
        
    # Game ends here
    if winner == 'X' or winner == 'O':
        print('The winner is ' + winner)
    elif winner == None:
        print('The game is tie.')
    
# flip player
def flipPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    elif currentPlayer == 'O':
        currentPlayer = 'X'
    return

# Begin the program proper
# Instruction
print('This is a Tic Tac Toe game, with size 3x3')
rawBoard = ['1','2','3',
            '4','5','6',
            '7','8','9']
print('The index instruction for filling in is as follow: ')
print(rawBoard[0] + '|' + rawBoard[1] + '|' + rawBoard[2])
print('-----')
print(rawBoard[3] + '|' + rawBoard[4] + '|' + rawBoard[5])
print('-----')
print(rawBoard[6] + '|' + rawBoard[7] + '|' + rawBoard[8])
print('')

# Actually run the main part of the scrit
playGame()
input('Press enter to escape')
