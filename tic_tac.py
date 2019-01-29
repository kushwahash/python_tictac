from IPython.display import clear_output


'''
Function will take a board list between index [0-9]
It will display the board
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
Output :
    X|O|X
    -|-|-
    O|X|O
    -|-|-
    X|O|X
'''
def display_board(board):
    clear_output()
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-|-|-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-|-|-")
    print(f"{board[7]}|{board[8]}|{board[9]}")

