# Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/

n = int(input("Enter 32 bit Binary Number: "))
rev = 0
for _ in range(32):
    rev = (rev << 1)^(n & 1)
    n >>= 1
print("Reverse of given Binary is: ", rev)