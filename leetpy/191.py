# Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/

n = input("Enter binary: " )

n0 = n.split('0')
hamd0 = 0
for v in n0:
    hamd0 += len(v)
print("hamd0: ", hamd0)

hamd1 = n.count('1')
print("hamd1: ", hamd1)

decimal_number = int(n, 2)
hamming = 0
while decimal_number:
    hamming += 1
    decimal_number &=  decimal_number - 1
print("hamming: ", hamming)


