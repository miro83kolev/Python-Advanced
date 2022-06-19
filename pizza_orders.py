from collections import deque

# pizzas = deque([int(x) for x in input().split(', ') if int(x) > 0 and int(x) < 11])
# employees = [int(x) for x in input().split(', ')]
#
# total_pizzas_count = 0
# is_finished = False
#
# while pizzas and employees:
#     while pizzas[0] > employees[-1]:
#         total_pizzas_count += employees[-1]
#         pizzas[0] = pizzas[0] - employees[-1]
#         employees.pop()
#
#         if not pizzas or not employees:
#             is_finished = True
#             break
#     if is_finished:
#         break
#
#     total_pizzas_count += pizzas.popleft()
#     employees.pop()
#
# if pizzas:
#     print('Not all orders are completed.')
#     print(f'Orders left: {", ".join([str(x) for x in pizzas])}')
# else:
#     print('All orders are successfully completed!')
#     print(f'Total pizzas made: {total_pizzas_count}')
#     print(f'Employees: {", ".join([str(x) for x in employees])}')

def process_pizzas(pizzas, employees):
    total_pizzas_count = 0

    while pizzas and employees:
        while pizzas[0] > employees[-1]:
            total_pizzas_count += employees[-1]
            pizzas[0] = pizzas[0] - employees[-1]
            employees.pop()

            if not pizzas or not employees:
                return total_pizzas_count

        total_pizzas_count += pizzas.popleft()
        employees.pop()
    return total_pizzas_count

pizzas = deque([int(x) for x in input().split(', ') if int(x) > 0 and int(x) < 11])
employees = [int(x) for x in input().split(', ')]

total_pizzas_count = process_pizzas(pizzas, employees)

if pizzas:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizzas])}')
else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas_count}')
    print(f'Employees: {", ".join([str(x) for x in employees])}')