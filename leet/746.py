# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

cost = [int(x) for x in input("Enter costs: ").split()]
lc = len(cost)

def minCost():
    if lc < 2: return 0
    dp = [0]*lc
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, lc):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[lc-1], dp[lc-2])

print("Minimum Cost: ", minCost())
