# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/


def merge(nums1, nums2, m, n):
    i, j = m - 1, n - 1
    indx = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[indx] = nums1[i]
            i -= 1
        else:
            nums1[indx] = nums2[j]
            j -= 1
        indx -= 1
    while j >= 0:
        nums1[indx] = nums2[j]
        j -= 1
        indx -= 1
    return nums1

print(merge([1,2,3,0,0,0], [2,5,6], 3, 3))

    