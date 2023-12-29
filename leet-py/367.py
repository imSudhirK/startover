# Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/description/
import math

n  = int(input("Enter Number: "))
print("Is perfect Square: ", math.sqrt(n)%1 == 0)

is_perfect_square = False
low, high = 0, n
mid = (low + high) >> 1
while low <= high:
    mm = mid*mid
    if mm == n:
        is_perfect_square = True
        break
    elif mm < n:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) >> 1

print("Is perfect square: ", is_perfect_square)