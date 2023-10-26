import math

X = 'X'
O = 'O'
EMPTY = ' '

def initialize_board():
    return [[EMPTY] * 3 for _ in range(3)]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def is_game_over(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

def is_winner(board, player):
    for i in range(3):
       
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def evaluate_board(board):
    if is_winner(board, X):
        return 1
    elif is_winner(board, O):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_game_over(board):
        return evaluate_board(board)
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = X
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

if _name_ == "_main_":
    board = initialize_board()
    current_player = X
    
    while not is_game_over(board):
        print_board(board)
        if current_player == X:
            print("Player X's turn")
            move = find_best_move(board)
        else:
            print("Player O's turn")
            while True:
                try:
                    move = tuple(map(int, input("Enter row and column (comma-separated): ").split(',')))
                    if board[move[0]][move[1]] == EMPTY:
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")
                except IndexError:
                    print("Invalid input. Try again.")
        
        board[move[0]][move[1]] = current_player
        current_player = O if current_player == X else X

    print_board(board)
    if is_winner(board, X):
        print("Player X wins!")
    elif is_winner(board, O):
        print("Player O wins!")
    else:
        print("It's a tie!")