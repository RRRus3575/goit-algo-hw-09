def find_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result


print(find_coins(150))
