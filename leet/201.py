# Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

# 500 = 11111 0100 
# 510 = 11111 1110 

# find where difference of bits starts
# common bits are our answer

def rangeBitwiseAnd(left, right):
    shifts = 0
    while left != right:
        left >>= 1
        right >>= 1
        shifts += 1
    return left << shifts

print(rangeBitwiseAnd(500, 510))