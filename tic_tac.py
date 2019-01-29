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


'''
Take in a player input and assign their marker as 'X' or 'O'.
Return : Selected marker X or O
'''
def player_input():
    player1 = 'W'
    got_right_value = True
    while got_right_value:
        player1 = input('Player 1 select your marker X or O')
        if(player1.upper() == 'X' or player1.upper() == 'O'):
            return player1.upper()
        else:
            print('Please select a valid marker X or O')


'''
Takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9)
and assigns it to the board.
'''
def place_marker(board, marker, position):
    board[position]=marker

'''
Check for winning condition for tictac
Input : Current index, game board, mark (mark to check for winner)
Output : True or False
'''
def is_winner(index,board,mark):
     #//check row wise
    if index in [1,4,7]:
        if board[index+1] == mark and board[index+2] == mark:
            return True
    
    #//check col wise
    if index in [1,2,3]:
        if board[index+3] == mark and board[index+4] == mark:
            return True
    
    #check diagonal wise
    if index == 1:
        if board[5] == mark and board[9] == mark:
            return True
    
    # check anti diagonal wise
    if index == 3 :
        if board[5] == mark and board[7] == mark:
            return True
    
    return False

'''
function that takes in a board and a mark (X or O) and then checks 
to see if that mark has won
Output : Return True or False
'''
def win_check(board, mark):
    for index in range(1,len(board)):
        if(board[index] == mark and is_winner(index,board,mark)):
           return True
    
    return False    

