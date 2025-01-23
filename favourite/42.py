# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description


def waterTrap(heights):
    num_heights = len(heights)
    left_max, right_max = 0, 0
    left_pointer, right_pointer = 0, num_heights - 1
    total_water = 0
    while left_pointer <= right_pointer:
        if heights[left_pointer] < heights[right_pointer]:
            if left_max > heights[left_pointer]:
                total_water += left_max - heights[left_pointer]
            else:
                left_max = heights[left_pointer]
            left_pointer += 1
        else:
            if right_max > heights[right_pointer]:
                total_water += right_max - heights[right_pointer]
            else:
                right_max = heights[right_pointer]
            right_pointer -= 1
    return total_water

print('[0,1,0,2,1,0,1,3,2,1,2,1]\t', waterTrap([0,1,0,2,1,0,1,3,2,1,2,1]))
print('[4,2,0,3,2,5]\t', waterTrap([4,2,0,3,2,5]))
