strings = input().split()

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('blue', 'yellow')

}

made_colors = []

while strings:
    first_el = strings.pop(0)
    second_el = ''

    if strings:
        second_el = strings.pop()


    first_combo = first_el + second_el
    second_combo = second_el + first_el

    if first_combo in main_colors or first_combo in secondary_colors:
        made_colors.append(first_combo)
    elif second_combo in main_colors or second_combo in secondary_colors:
        made_colors.append(second_combo)
    else:
        if len(first_el) > 1:
            strings.insert(len(strings) // 2, first_el[:-1])
        if len(second_el) > 1:
            strings.insert(len(strings) // 2, second_el[:-1])

for i in range(len(made_colors) - 1, -1, -1):
    current = made_colors[i]
    if current in secondary_colors and any(x not in main_colors for x in secondary_colors[current]):
        del made_colors[i]

print(made_colors)


