import random


def draw_board(board):
    print(board[7] + '|' + board [8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board [5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board [2] + '|' + board[3])


def input_player_letter():
    letter = ''
    while not (letter == 'O' or letter == 'X'):
        print('Do you want to be X or O?')
        letter = raw_input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def first_player():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def get_board_copy(board):
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def free_space(board, move):
    return board[move] == ' '


def player_move(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
        print('\nWhat is your next move? (1-9)')
        move = raw_input()

    return int(move)


def random_move_from_list(board, moves_list):
    possible_moves = []

    for i in moves_list:
        if free_space(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if free_space(copy, i):
            make_move(copy, computer_letter, i)
            if winner(copy, computer_letter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if free_space(copy, i):
            make_move(copy, player_letter, i)
            if winner(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if free_space(board, 5):
        return 5

    # Move on one of the sides.
    return random_move_from_list(board, [2, 4, 6, 8])


def full_board(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True

print('***********************')
print('Welcome to Tic-Tac-Toe!')
print('***********************')
print('Here is a move guide')
print('\t''7' + '|' + '8' + '|' + '9')
print('\t''-+-+-')
print('\t''4' + '|' + '5' + '|' + '6')
print('\t''-+-+-')
print('\t''1' + '|' + '2' + '|' + '3')
print('***********************\n')

while True:
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = first_player()
    print('The ' + turn + ' will go first.\n')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn
            draw_board(the_board)
            move = player_move(the_board)
            make_move(the_board, player_letter, move)

            if winner(the_board, player_letter):
                draw_board(the_board)
                print('Hooray, you won the game!')
                game_is_playing = False
            else:
                if full_board(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn
            move = computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose!')
                game_is_playing = False
            else:
                if full_board(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
