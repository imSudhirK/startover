# Jump Game II
# https://leetcode.com/problems/jump-game-ii/

nums = [2,3,0,1,4]

ln = len(nums)
dp = [float("inf")]*ln
dp[ln-1] = 0

for i in range(ln - 2, -1, -1):
    if not nums[i]: continue
    min_jump = min(dp[i+1: min(ln, i + nums[i] + 1)])
    dp[i] = min_jump + 1

print("Minimum jump: ", dp[0])