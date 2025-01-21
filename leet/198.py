# House Robber
# https://leetcode.com/problems/house-robber/description/

nums = [2,7,9,3,1]

ln = len(nums)
dp = [0]*ln
dp[0], dp[1] = nums[0], max(nums[0], nums[1])

for i in range(2, ln): dp[i] = max(dp[i-1], dp[i-2] + nums[i])
print("Maximum Amount: ", dp[ln - 1])

