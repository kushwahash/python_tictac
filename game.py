import tic_tac 

game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player_marker = {'Player 1':"X",'Player 2':"O"}

def game_continue(game_board,current_player):
    print(f"{current_player}  chose ...")
    position = tic_tac.player_choice(game_board)
    game_board[position]=player_marker[current_player]
    if tic_tac.win_check(game_board,player_marker[current_player]):
        print("\n\n===========================================================")
        print(f'\n\n******* {current_player} wins the game.  *******')
        print("\n\n===========================================================")
        return False
    elif tic_tac.full_board_check(game_board):
        print("\n\n===========================================================")
        print(f'\n\n******* Game is a Tie  *******')
        print("\n\n===========================================================")
        return False
    else:
        return True


def start_game():
    play_game = True
    while play_game:
        print('Welcome to Tic Tac Toe!')
        game_on = True
        second_player = ''
        player = tic_tac.choose_first()
        #initialize empty board
        game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        if player == 'Player 1':
            second_player = 'Player 2'
        else:
            second_player = 'Player 1'
        
        print(f"{player}, will go first..")
        marker_temp = tic_tac.player_input()
        if marker_temp == 'X':
            player_marker[player] = 'X'
            player_marker[second_player] = 'O'
        else:
            player_marker[player] = 'O'
            player_marker[second_player] = 'X'

        print(f"Player 1, Marker :: {player_marker['Player 1']}")
        print(f"Player 2, Marker :: {player_marker['Player 2']}")

        while game_on:
            game_on = game_continue(game_board,player)
            tic_tac.display_board(game_board)
            if game_on:
                game_on = game_continue(game_board,second_player)
                tic_tac.display_board(game_board)
        
        play_game = tic_tac.replay()   
            
            


#Start the game

start_game()
