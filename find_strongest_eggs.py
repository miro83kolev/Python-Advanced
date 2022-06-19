def find_strongest_eggs(eggs, sublist_count):
    sub_lists = []
    best_eggs = []

    for _ in range(sublist_count):
        sub_lists.append([])

    for idx in range(len(sub_lists)):
        sub_lists[idx] = [eggs[index] for index in range (idx, len(eggs), sublist_count)]

    for sublist in sub_lists:
        mid_element = sublist[len(sublist) // 2]
        left_element = sublist[len(sublist) // 2 - 1]
        right_element = sublist[len(sublist) // 2 + 1]
        if left_element < mid_element > right_element > left_element:
            best_eggs.append(mid_element)

    return best_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))