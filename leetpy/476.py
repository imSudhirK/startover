# Number Complement
# https://leetcode.com/problems/number-complement/

num = int(input("Enter number: "))
i = 1
while i < num: i <<= 1
twos_compliment = (i - 1) ^ num
print("2's compliment: ", twos_compliment)