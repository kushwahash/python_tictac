import tic_tac 

game_board = ['#','X','O','X','O','X','O','X','O','X']

def start_game():
    play_game = True
    game_on = True
    while play_game:
        print('Welcome to Tic Tac Toe!')
        #list for player
        player_list = ['Player 1','Player 2']
        player = tic_tac.choose_first()
        if player == 'Player 1':
            player_list[0] = 'Player 1'
            player_list[1] = 'Player 2'
        else:
            player_list[0] = 'Player 2'
            player_list[1] = 'Player 1'
        
        print(f"{player}, will go first..")
        #map for player marker
        player_marker = {player_list[0]:"X",player_list[1]:"O"}
        marker_temp = tic_tac.player_input()
        if marker_temp == 'X':
            player_marker[player_list[0]] = 'X'
            player_marker[player_list[1]] = 'O'
        else:
            player_marker[player_list[0]] = 'O'
            player_marker[player_list[1]] = 'X'

        print(f"Player 1, Marker :: {player_marker['Player 1']}")
        print(f"Player 2, Marker :: {player_marker['Player 2']}")

        while game_on:
            print(f"Player 1 ...")
            position = tic_tac.player_choice(game_board)
            game_board[position] = player_marker['Player 1']
            #Check if space available
            if tic_tac.full_board_check(game_board):
                #check for win condition
                print('No more space available.')
                game_on = False
                if tic_tac.win_check(game_board,player_marker['Player 1']):
                    print('Player 1 wins the game.')
                else:
                    print('Game is a Tie')
            


#Start the game

start_game()
