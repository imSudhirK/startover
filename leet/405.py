# Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

n = int(input("Enter: "))
print("Hex n: ", hex(n))
hex_nums = '0123456789abcdef'
n_hex = ''
while n:
    n_hex = hex_nums[n & 15] + n_hex
    n >>= 4
print("Hex n: ", n_hex)

