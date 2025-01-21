# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence


nums = [10,9,2,5,3,7,101,18]

def lengthOfLIS(arr):
    la = len(arr)
    dp = [0]*la
    for i in range(la):
        max_len = 0
        for j in range(i):
            if arr[i] > arr[j]:
                max_len = max(max_len, dp[j])
        dp[i] = max_len + 1
    return max(dp)

print(lengthOfLIS(nums))