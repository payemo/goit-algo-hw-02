items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]

    return selected_items, total_calories

def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(items)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(budget + 1):
            if costs[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    total_calories = dp[n][budget]
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(names[i - 1])
            j -= costs[i - 1]

    selected_items.reverse()
    return selected_items, total_calories

budget = 100

# Greedy approach
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Greedy approach:")
print("Selected items:", greedy_result)
print("Total calories:", greedy_calories)

# Dynamic programming approach
dp_result, dp_calories = dynamic_programming(items, budget)
print("\nDynamic Programming approach:")
print("Selected items:", dp_result)
print("Total calories:", dp_calories)