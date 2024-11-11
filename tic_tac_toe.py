def main():
# Main game
    p1, p2 = intro()
    board = initBoard()
    printBoard(board)
    winner = None
    win = False
    turn = 1
    while (not win and turn <= 9):
        selectSquare(p1, p2, board, turn)
        printBoard(board)
        winner, win = winnerCheck(board)
        turn += 1
    announceWinner(p1, p2, winner)


def intro():
# Opening
    print("___________")
    print("           ")
    print("TIC TAC TOE")
    print("___________")
    print("\n")
    print("Rules: Player 1 : X, Player 2: O\nTake turn marking spaces on the 3x3 board."\
          "Whoever succeeds in placing three of their marks in a horizontal, vertical, "\
          "or diagonal row is the winner.")

    p1 = input("Enter name of Player 1: ")
    p2 = input("Enter name of Player 2: ")

    print("Here is your board! Have Fun!")
    return p1, p2

def initBoard():
# Initializes the board
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    return board

def printBoard(board):
# Prints the board
    print("---------")
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    print("---------")

def selectSquare(p1, p2, board, turn):
# Game play, selecting squares
    # Turn check
    if turn % 2 == 1:
        player = p1
        mark = 'X'
    else:
        player = p2
        mark = 'O'
    # Player selection    
    print(f"{player}'s Turn!")
    while True:
        try:
            row = int(input("Pick a row:\nupper: enter 0, middle: enter 1, lower: enter 2\n"))
            column = int(input("Pick a column:\nleft: enter 0, middle: enter 1, right: enter 2\n"))
            if validCheck(row, column) and filledCheck(board, row, column):
                board[row][column] = mark
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for an unfilled square.")

def validCheck(row, column):
# Checks if player entered a valid option
    if row in [0, 1, 2] and column in [0, 1, 2]:
        return True
    else:
        print("Please enter a valid number (0, 1, or 2).")
        return False

def filledCheck(board, row, column):
# Checks if the square is empty
    if board[row][column] in ['X', 'O']:
        print("The square is filled. Please select an empty square.")
        return False
    return True

def winnerCheck(board):
# Determines the winner by using prime numbers
    primeBoard = [[2,3,5],[7,11,13],[17,19,23]]
    winPrime = [2*3*5, 7*11*13, 17*19*23, 2*7*17, 3*11*19, 5*13*23, 2*11*23, 5*11*17]
    p1mult = 1
    p2mult = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                p1mult *= primeBoard[i][j]
            if board[i][j] == 'O':
                p2mult *= primeBoard[i][j]
    if 0 in [p1mult % x for x in winPrime]:
        return 'P1', True
    elif 0 in [p2mult % x for x in winPrime]:
        return 'P2', True
    else:
        return 'none', False

def announceWinner(p1, p2, winner):
# Announces the winner
    if winner == 'P1':
        print(f"{p1} wins!")
    elif winner == 'P2':
        print(f"{p2} wins!")
    else:
        print("It's a tie!")

# Calls game to start
main()