# Integer to Roman
# https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def intToRoman(num):
    ret_rom = ''
    for i, v in enumerate(vals):
        ret_rom += (num // v) * roman[i]
        num %= v
    return ret_rom

print(intToRoman(1994))