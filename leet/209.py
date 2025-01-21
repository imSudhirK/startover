# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150


def minSubArrayLen(target, nums):
    ln_nums = len(nums)
    min_ln = ln_nums + 1
    start_indx, current_window_sum = 0, 0
    for last_indx in range(ln_nums):
        current_window_sum += nums[last_indx]
        if current_window_sum < target:
            continue
        while current_window_sum >= target:
            current_window_sum -= nums[start_indx]
            start_indx += 1
        min_ln = min(min_ln, last_indx + 1 - start_indx + 1)
    return min_ln if min_ln <= ln_nums else 0

print('7, [2,3,1,2,4,3]\t', minSubArrayLen(7, [2,3,1,2,4,3]))
