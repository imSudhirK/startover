# Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

from bisect import bisect_right


nums = [4,5,2,1]
queries = [3,10,21]

nums.sort()
ln = len(nums)

for i in range(1, ln): nums[i] = nums[i-1] + nums[i]

ans = []
for q in queries:
    indx = bisect_right(nums, q)
    ans.append(indx)

print("answer: ", ans)