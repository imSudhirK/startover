# Jump Game II
# https://leetcode.com/problems/jump-game-ii/

def jumpV1(nums):
    n = len(nums)
    # minimum jumps to reach at index i from 0
    dp = [float('inf')] * n
    dp[0] = 0
    for curr_indx in range(n - 1):
        # could make jump to any of reachable index
        for next_indx in range(curr_indx + 1, min(n, curr_indx + nums[curr_indx] + 1)):
            dp[next_indx] = min(dp[next_indx], dp[curr_indx] + 1)
    return dp[n - 1]

def jumpV2(nums):
    n = len(nums)
    # minimum jump to reach from i to n - 1
    dp = [float('inf')] * n
    dp[n - 1] = 0
    for curr_indx in range(n - 2, -1, -1):
        if not nums[curr_indx]: continue
        min_jump = min(dp[curr_indx + 1 : min(n, curr_indx + nums[curr_indx] + 1)])
        dp[curr_indx] = min_jump + 1
    return dp[0]

print(jumpV2([2,3,0,1,4]))
