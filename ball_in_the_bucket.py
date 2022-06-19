def sum_column(ma, col):
    points = 0
    for row_index in range(len(ma)):
        if matrix[row_index][col] != "B":
            points += int(matrix[row_index][col])
    return points


n = 6
matrix = []
trows_count = 3
total_points = 0

for _ in range(n):
    matrix.append(input().split())

for _ in range(trows_count):
    row, col = [int(x) for x in eval(input())] #eval takes and makes tuples - evaluates to what to cast

    try:
        if matrix[row][col] == "B":
            total_points += sum_column(matrix, col)
            matrix[row][col] = '0'
    except IndexError:
        continue

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
elif 100 <= total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")