# Longest Square Streak in an Array
# https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=daily-question&envId=2024-10-29


def longestSquareStreakBruteForce(nums):
    max_streak_array = []
    for n in nums:
        current_streak_array = []
        while n in nums:
            current_streak_array.append(n)
            n *= n
        lca = len(current_streak_array)
        if lca > 1 and lca >= len(max_streak_array):
            max_streak_array = current_streak_array
    lms = len(max_streak_array) or -1
    return lms

print(longestSquareStreakBruteForce([4,3,6,16,8,2]))
print(longestSquareStreakBruteForce([2,3,5,6,7]))
