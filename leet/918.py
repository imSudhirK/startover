# Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/


def kadane(nums):
    max_sum, curr_sum = float('-inf'), 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def maxSubarraySumCircular(nums):
    max_sum_non_circular = kadane(nums)
    total_sum = sum(nums)
    nums = [-num for num in nums]
    min_sum_non_circular = kadane(nums)
    max_sum_circular = total_sum + min_sum_non_circular
    return max_sum_non_circular if not max_sum_circular else max(max_sum_non_circular, max_sum_circular)

print(maxSubarraySumCircular([1,-2,3,-2]))