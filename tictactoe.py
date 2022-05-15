import random
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

current_player ="X"
winner = None
game_Running = True

def print_board(board):
        print(board[0]+"|"+board[1]+"|"+board[2])
        print(board[3]+"|"+board[4]+"|"+board[5])
        print(board[6]+"|"+board[7]+"|"+board[8])
        print("----------")
        
def player_input(board):
    n = int(input("enter a number from 1-9"))
    if (n>=1 and n<=9 and board[n-1]=="_"):
        board[n-1]= current_player
    else:
        print("player is already in that spot input another number")
        playerinput(board)

def check_horizontal(board):
    global winner
    if(board[0]==board[1]==board[2] and board[0]!="_"):
        winner=board[0]
        return True
    elif (board[3]==board[4]==board[5] and board[3]!="_"):
         winner=board[3]
         return True
    elif (board[6]==board[7]==board[8] and board[6]!="_"):
         winner=board[6]
         return True

def check_row(board):
    global winner
    if(board[0]==board[3]==board[6] and board[0]!="_"):
        winner=board[0]
        return True
    elif (board[2]==board[4]==board[7] and board[2]!="_"):
         winner=board[2]
         return True
    elif (board[3]==board[5]==board[8] and board[3]!="_"):
         winner=board[3]
         return True

def check_diagonal(board):
    global winner
    if(board[0]==board[4]==board[8] and board[0]!="_"):
        winner=board[0]
        return True
    elif (board[2]==board[4]==board[6] and board[2]!="_"):
         winner=board[2]
         return True

def check_tie(board):
    if "_" not in board:
        print_board(board)
        print("It is a tie")
        board = ["_", "_", "_",
                 "_", "_", "_",
                "_", "_", "_"]
        game_running= False

def check_win():
    global board
    if (check_diagonal(board) or check_row(board) or check_horizontal(board)):
        print("the winner is", winner)
        board = ["_", "_", "_",
                  "_", "_", "_",
                  "_", "_", "_"]

def switch_player():
    global current_player 
    if current_player =="X":
        current_player = "O"
    else:
        current_player ="X"

def computer(board):
    while current_player=="O":
        position = random.randint(0,8)
        if board[position]=="_":
            board[position]="O"
            switch_player()


while game_Running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)
