from collections import deque

tasks_stack = [int(x) for x in input().split(', ')]

searched_index = int(input())
result = 0
cycles = deque(sorted([tasks_stack[index], index] for index in range(len(tasks_stack))))

while cycles:
    number, index = cycles.popleft()
    result += number
    if index == searched_index:
        print(result)
        break