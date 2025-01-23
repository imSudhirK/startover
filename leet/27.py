# Remove Element
# https://leetcode.com/problems/remove-element

def removeElement(nums, val):
    n = len(nums)
    indx = 0
    for i in range(n):
        if nums[i] != val:
            nums[indx] = nums[i]
            indx += 1
    return indx

print(removeElement([3,2,2,3], 3))
