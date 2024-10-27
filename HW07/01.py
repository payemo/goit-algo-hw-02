import heapq
from typing import List

def minimize_expenses(cabels: List[int]):
    if not cabels:
        return 0
    
    # Transform list into min-heap
    heapq.heapify(cabels)
    tot_expenses = 0

    while len(cabels) > 1:
        cab1 = heapq.heappop(cabels)
        cab2 = heapq.heappop(cabels)

        expense = cab1 + cab2
        tot_expenses += expense

        heapq.heappush(cabels, expense)

        print(f"Об'єднано кабелі довжиною {cab1} та {cab2} -> новий кабель {expense}, загальні витрати: {tot_expenses}")

    return tot_expenses

cabels = [4, 3, 2, 6]
tot = minimize_expenses(cabels)
print(f"Мінімальні загальні витрати: {tot}")