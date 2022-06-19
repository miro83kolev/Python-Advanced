from collections import deque

boxes = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))

presents = {
    150: 'Doll',
    200: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while boxes and magic_values:
    current_box = boxes.pop()
    current_magic = magic_values.popleft()
    total_magic = current_magic * current_box

    if total_magic in presents:
        crafted_presents[presents[total_magic]] += 1
    else:
        if total_magic > 0:
            boxes.append(current_box + 15)
        elif total_magic < 0:
            result = current_box + current_magic
            boxes.append(result)
        else:
            if current_box:
                boxes.append(current_box)
            if current_magic:
               magic_values.append(current_magic)

success = (crafted_presents['Doll'] and crafted_presents['Wooden train'] or crafted_presents['Teddy bear'] and crafted_presents['Bicycle'])

if success:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents for Christmas!')

if boxes:
    print(f'Materials left: {", ".join(reversed([str(x) for x in boxes]))}')
if magic_values:
    print(f'Magic left: {", ".join([str(x) for x in magic_values])}')

for key, value in sorted(crafted_presents.items()):
    if value:
        print(f'{key}: {value}')


