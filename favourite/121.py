# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


def maxProfits(prices):
    # corner cases
    n = len(prices)
    if n < 2: return 0
    
    max_profit, current_profit = 0, 0
    for i in range(1, n):
        current_profit += (prices[i] - prices[i - 1])
        if current_profit > 0:
            max_profit = max(max_profit, current_profit)
        else:
            current_profit = 0
    return max_profit

print(maxProfits([7,1,5,3,6,4]))