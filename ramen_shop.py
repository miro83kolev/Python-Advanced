from collections import deque

ramen_bowl = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while ramen_bowl and customers:
    value_ramen = ramen_bowl[-1]
    next_customer = customers[0]

    if next_customer > value_ramen:
        ramen_bowl.pop()
        customers[0] -= value_ramen
    elif next_customer < value_ramen:
        customers.popleft()
        ramen_bowl[-1] -= next_customer
    elif next_customer == value_ramen:
        ramen_bowl.pop()
        customers.popleft()


if len(customers) == 0:
    print("Great job! You served all the customers.")
elif len(ramen_bowl) == 0:
    print("Out of ramen! You didn't manage to serve all customers.")

if ramen_bowl:
    print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen_bowl])}")

if customers:
    print(f"Customers left: {', '.join([str(x) for x in customers])}")


