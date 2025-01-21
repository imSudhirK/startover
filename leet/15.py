# 3Sum
# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150


def threeSum(nums):
    nums.sort()
    result = []
    ln = len(nums)
    
    for i in range(ln - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left_pointer, right_pointer = i + 1, ln - 1
        while left_pointer < right_pointer:
            current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
            if not current_sum:
                result.append([nums[i], nums[left_pointer], nums[right_pointer]])
                while left_pointer < right_pointer and  nums[left_pointer] == nums[left_pointer + 1]:
                    left_pointer += 1
                while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                    right_pointer -= 1
                left_pointer += 1
                right_pointer -= 1
            elif current_sum < 0:
                left_pointer += 1
            else:
                right_pointer -= 1
    return result

print('[-1,0,1,2,-1,-4]', threeSum([-1,0,1,2,-1,-4]))