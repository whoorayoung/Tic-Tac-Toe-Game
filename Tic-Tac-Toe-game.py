'''
Tic-Tac-Toe-Game
Author: Youngwho Park
'''

def main():
    board = create_board()
    display_board(board)
    turn = 0    
    
    while winner(board) != True:
        turn = x_or_o(turn)
        make_move(turn, board)
        print()
        display_board(board)
        winner(board)
    
    print()
    print("Good game. Thanks for playing!")
        

def create_board():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board

def display_board(board):
    count = 0
    for number in board:
        count +=1
        if count % 3 != 0:
            print(f"{number}|",end='')
        elif count % 3 ==0 :
            if count == 9: 
                print(number)
            else:
                print(number)
                print("-+-+-")
    
def x_or_o(turn):
    turn += 1
    if turn % 2 == 0:
        return turn
    else:
        return turn

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(turn, board):
    if turn % 2 == 0: 
        number = int(input("o's turn to choose a square (1-9): "))
        board[number-1] = "o"
    else:
        number = int(input("x's turn to choose a square (1-9): "))
        board[number-1] = "x"    

def player():
    pass

if __name__ == "__main__":
    main()
    
