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
# Determines the winner
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return ('P1' if row[0] == 'X' else 'P2'), True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return ('P1' if board[0][col] == 'X' else 'P2'), True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return ('P1' if board[0][0] == 'X' else 'P2'), True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return ('P1' if board[0][2] == 'X' else 'P2'), True
    
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