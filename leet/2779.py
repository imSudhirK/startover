# Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/

def maximumBeauty(nums, k):
    # ranges for each element
    events = []
    for n in nums:
        # 1 for start range and -1 for end range 
        events.append((n - k, 1))
        events.append((n + k + 1, -1))
    # sort by value
    events.sort()
    # check overlaping events
    current_overlap, max_overlap = 0, 0
    for _, event_type in events:
        current_overlap += event_type
        max_overlap = max(max_overlap, current_overlap)
    
    return max_overlap

print(maximumBeauty([4, 6, 1, 3], 2))



