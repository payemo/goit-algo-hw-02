def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount > coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [(float('inf'))] * (amount + 1)
    dp[0] = 0

    last_coin = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                last_coin[x] = coin

    if dp[amount] == float('inf'):
        return {}
    
    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current -= coin
    
    return result

sum_to_give = 113
change = find_min_coins(sum_to_give)
print(change)  # Виведе: {50: 2, 10: 1, 2: 1, 1: 1}