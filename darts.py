def get_turn():
    turn_string = input()
    vals = turn_string[1:-1].split(', ')
    return [int(val) for val in vals]


def in_range(val, max_val):
    return 0 <= val < max_val


def get_value(board, row_index, col_index, n, m):
    if not in_range(row_index, n) or not in_range(col_index, m):
        return 0

    value = board[row_index][col_index]

    if value.isdigit():
        return int(value)

    sum_value = int(board[row_index][0]) + int(board[row_index][-1]) + int(board[0][col_index]) + int(board[-1][col_index])

    if value == "D":
        return 2 * sum_value
    if value == "T":
        return 3 * sum_value

    return 501

def solve(board, player_names, n, m):
    player_one = player_names[0], 501, 0
    player_two = player_names[1], 501, 0

    while True:
        name, points, turns = player_one
        row_index, col_index = get_turn()

        points -= get_value(board, row_index, col_index, n, m)
        turns += 1

        player_one = (name, points, turns)

        if points <= 0:
            break

        player_one, player_two = player_two, player_one

    print(f'{name} won the game with {turns} throws!')


player_names = input().split(', ')
n = 7
m = 7
board = [input().split() for _ in range(n)]

solve(board, player_names, n, m)



