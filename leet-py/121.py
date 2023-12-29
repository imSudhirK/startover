# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

prices = [int(x) for x in input("Enter number: ").split()]
lp, maxp, currp = len(prices), 0, 0
for i in range(1, lp):
    currp += prices[i] - prices[i-1]
    if currp > 0:
        maxp = max(maxp, currp)
    else:
        currp = 0

print("Maximum profit: ", maxp)