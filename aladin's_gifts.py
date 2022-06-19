from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

# print(materials)
# print(magic)
count_gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

gifts_dict = {
    "Gemstone": list(range(100, 200)),
    "Porcelain Sculpture": list(range(200, 300)),
    "Gold": list(range(300, 400)),
    "Diamond Jewellery": list(range(400, 500))
}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    result = current_material + current_magic

    if result < 100:
        if result % 2 == 0:
            result = (current_material * 2) + (current_magic * 3)
        else:
            result *= 2

    elif result > 499:
        result = result // 2

    if 100 < result < 499:
        for key in gifts_dict:
            if result in gifts_dict[key]:
                count_gifts[key] += 1
                break
    else:
        continue

# print(count_gifts)
if (count_gifts["Gemstone"] > 0 and count_gifts["Porcelain Sculpture"] > 0) \
        or (count_gifts["Gold"] > 0 and count_gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(count_gifts.items()):
    if value > 0:
        print(f"{key}: {value}")