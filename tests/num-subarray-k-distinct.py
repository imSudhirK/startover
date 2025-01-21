# sosuv consulting
# Given an integer array nums and an integer k, 
# return the number of subarrays of nums
# that contain atmost k distinct integers.

# example 
arr = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4 , 5, 6, 7]
k = 3


# solution
def bruteForce(arr, k):
    count = 0
    la = len(arr)
    for ln_subarr in range(1, la + 1):
        for start_ind in range(la):
            if start_ind + ln_subarr > la:
                continue
            subset  = set(arr[start_ind : start_ind + ln_subarr])
            if len(subset) <= k:
                count += 1
    return count

print('bruteForce', bruteForce(arr, k))

# solution 
from collections import defaultdict
def slidingWindow(arr, k):
    frequency_counter = defaultdict(int)
    count = 0
    left_ind = 0
    la = len(arr)
    for right_ind in range(la):
        frequency_counter[arr[right_ind]] += 1
        while len(frequency_counter) > k:
            frequency_counter[arr[left_ind]] -= 1
            if not frequency_counter[arr[left_ind]]:
                del frequency_counter[arr[left_ind]]
            left_ind += 1
        count += right_ind - left_ind  + 1
    return count

print('slidingWindow', slidingWindow(arr, k))


    
