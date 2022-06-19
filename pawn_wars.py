def find_player_position(matrix, player):
    for (row_index, row) in enumerate(matrix):
        if player in row:
            return (row_index, row.index(player))

    return (None, None)

def get_chess_position(row, column):
    rown_names = [8, 7, 6, 5, 4, 3, 2, 1]
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return  rown_names[row], column_names[column]

ROW_COUNT = 8
COL_COUNT = 8

matrix = [input().split() for _ in range(ROW_COUNT)]

current_player = 'w'
other_player = 'b'

current_player_pos = find_player_position(matrix, 'w')
other_player_pos = find_player_position(matrix, 'b')

current_delta = -1
other_delta = +1

is_capture = False
is_queen = False

while not is_capture and not is_queen:
    current_player_row, current_player_col = current_player_pos
    other_player_row, other_player_col = other_player_pos

    current_player_row += current_delta
    current_player_pos = current_player_row, current_player_col

    if current_player_row == other_player_row and abs(current_player_col - other_player_col) == 1:
        is_capture = True
        current_player_pos = current_player_row, other_player_col
    elif current_player_row in (0, ROW_COUNT - 1):
        is_queen = True
    else:
        current_player, other_player = other_player, current_player
        current_delta, other_delta = other_delta, current_delta
        current_player_pos, other_player_pos = other_player_pos, current_player_pos

player = 'White' if current_player == 'w' else 'Black'
row_name, col_name = get_chess_position(*current_player_pos)
position_name = f'{col_name}{row_name}'

if is_capture:
    print(f'Game over! {player} win, capture on {position_name}.')

if is_queen:
    print(f'Game over! {player} pawn is promoted to a queen at {position_name}.')