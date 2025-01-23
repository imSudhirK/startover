# Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

def removeDuplicates(nums):
    # corner cases
    n = len(nums)
    if n < 3: return n
    # slow pointer
    sp = 1
    for fp in range(2, n):
        if nums[fp] == nums[sp - 1]: continue
        nums[sp + 1] = nums[fp]
        sp += 1
    # print(nums)
    return sp

print(removeDuplicates([1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4]))
