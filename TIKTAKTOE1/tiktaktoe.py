# -*- utf-8 -*-

import os



the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

board = f'''

{the_board[7]}  |  {the_board[8]}  |  {the_board[9]}
-------------
{the_board[4]}  |  {the_board[5]}  |  {the_board[6]}
-------------
{the_board[1]}  |  {the_board[2]}  |  {the_board[3]}


'''


class Player():

    def __init__(self):
        print(board)

    def player_input(self):

        print("\nWelcome to the Tic Tac Toe, made by me... really? well I'm not that creative so...\n")

        player_one = input("What should thou be, X or 0?? decide now, or...\n Whenever I'm a line of code not you father ")

        if player_one == "X" or player_one == "O":
            if player_one.upper() == "X":
                player_two = "O"
                return (player_one,player_two)
            else:
                player_two = "X"
                return (player_one,player_two)

        else:
            os.system('cls')
            return self.player_input()

    def position_asker(self):

        position = int(input("\nWhere is thy next move? sele 1 trougt 9(like a numpad)\n"))

        return position

    def place_marker(self,player,position):

        if player == "X":
            the_board[position] = "X"
            return the_board
        else:
            the_board[position] = "O"
            return the_board

    def game_over(self,board,player):
        return ((board[7] == player and board[8] == player and board[9] == player) or # across the top
        (board[4] == player and board[5] == player and board[6] == player) or # across the middle
        (board[1] == player and board[2] == player and board[3] == player) or # across the bottom
        (board[7] == player and board[4] == player and board[1] == player) or # down the middle
        (board[8] == player and board[5] == player and board[2] == player) or # down the middle
        (board[9] == player and board[6] == player and board[3] == player) or # down the right side
        (board[7] == player and board[5] == player and board[3] == player) or # diagonal
        (board[9] == player and board[5] == player and board[1] == player)) # diagonal
    def board_printer(self,board):
        print('                                            ')
        print(' '+board[7]+'  |  '+board[8]+'  |  '+board[9])
        print('---------------')
        print(' '+board[4]+'  |  '+board[5]+'  |  '+board[6])
        print('---------------')
        print(' '+board[1]+'  |  '+board[2]+'  |  '+board[3])
        

def main():

    game = Player()

    the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    turn = "Player 1"

    game_on = True

    player1, player2 = game.player_input()

    while game_on:
        if turn == "Player 1":
            print("Turno do " + turn)
            position = game.position_asker()
            the_board = game.place_marker(player1,position)
            os.system('cls')
            game.board_printer(the_board)
            if game.game_over(the_board,player1):
                game.board_printer(the_board)
                print("Player 1 Venceu")
                game_on = False
            else:
                if " " not in the_board:
                    print("Empatou")
                    game_on = False
                else:
                    turn ="Player 2"
        else:
            print("Turno do " + turn)
            position = game.position_asker()
            the_board = game.place_marker(player2,position)
            os.system('cls')
            game.board_printer(the_board)
            if game.game_over(the_board,player2):
                game.board_printer(the_board)
                print("Player 2 Venceu")
                game_on = False
            else:
                if " " not in the_board:
                    print("Empatou")
                    game_on = False
                else:
                    turn ="Player 1"
    else:
         print("Foi bom jogar com você")


if __name__ == "__main__":
       main()