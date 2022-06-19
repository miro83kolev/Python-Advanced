from collections import deque

elf_energies = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]

turns = 0
total_energy = 0
toys = 0

while boxes and elf_energies:
    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    turns += 1
    toys_to_be_created_count = 1
    energy_to_be_spent = box
    cookie = 1

    if turns % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turns % 5 == 0:
        toys_to_be_created_count = 0
        cookie = 0
    if energy_to_be_spent <= elf_energy:
        toys += toys_to_be_created_count
        total_energy += energy_to_be_spent
        elf_energies.append(elf_energy - energy_to_be_spent + cookie)
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2) # hot chocolate

print(f'Toys: {toys}')
print(f'Energy: {total_energy}')
if elf_energies:
    print(f'Elves left: {", ".join([str(x) for x in elf_energies])}')
if boxes:
    print(f'Boxes left: {", ".join([str(x) for x in boxes])}')