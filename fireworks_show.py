from collections import deque

firework_effects = deque([int(x) for x in input().split(', ') if int(x) > 0])
explosive_power_stack = [int(x) for x in input().split(', ') if int(x) > 0]

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

def is_fireworks_enough(fireworks):
    return all(x >= 3 for x in fireworks.values())


while firework_effects and explosive_power_stack and not is_fireworks_enough(fireworks):
    firework_effect = firework_effects.popleft()
    explosive_power = explosive_power_stack.pop()
    current_sum = firework_effect + explosive_power

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
    elif current_sum % 3 == 0:
        fireworks['Palm Fireworks'] += 1
    elif current_sum % 5 == 0:
        fireworks['Willow Fireworks'] += 1
    else:
        if firework_effect > 1:
            firework_effects.append(firework_effect - 1)
        explosive_power_stack.append(explosive_power)


if is_fireworks_enough(fireworks):
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: {", ".join([str(x) for x in firework_effects])}')

if explosive_power_stack:
    print(f'Explosive Power left: {", ".join([str(x) for x in explosive_power_stack])}')

for firework, count in fireworks.items():
    print(f'{firework}: {count}')