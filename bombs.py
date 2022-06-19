from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_castings = [int(x) for x in input().split(', ')]

bombs_table = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

crafted_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0

}


def is_bomb_pouch_filled(crafted_bombs):
    for count in crafted_bombs.values():
        if count < 3:
            return False
    return True


while bomb_effects and bomb_castings and not is_bomb_pouch_filled(crafted_bombs):
    bomb_effect = bomb_effects[0]
    bomb_casting = bomb_castings[-1]
    result = bomb_effect + bomb_casting

    if result in bombs_table:
        bomb_effects.popleft()
        bomb_castings.pop()
        bomb_type = bombs_table[result]
        crafted_bombs[bomb_type] += 1
    else:
        bomb_castings[-1] -= 5

if is_bomb_pouch_filled(crafted_bombs):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print('Bomb Effects: empty')

if bomb_castings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_castings])}")
else:
    print('Bomb Casings: empty')

for bomb_type, bomb_count in sorted(crafted_bombs.items()):
    print(f'{bomb_type}: {bomb_count}')