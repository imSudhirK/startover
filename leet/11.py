# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

height = [1,8,6,2,5,4,8,3,7]

lh = len(height)
most_water = 0
left_ptr, right_ptr = 0, lh - 1

while left_ptr < right_ptr:
    if height[left_ptr] <= height[right_ptr]:
        most_water = max(most_water, height[left_ptr] * (right_ptr - left_ptr))
        left_ptr += 1
    else:
        most_water = max(most_water, height[right_ptr] * (right_ptr - left_ptr))
        right_ptr -= 1

print("Maximum amount of water: ", most_water)