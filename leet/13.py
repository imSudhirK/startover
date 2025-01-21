# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150


roman = "IVXLCDM"
vals = [1, 5, 10, 50, 100, 500, 1000]
hmp_rom_val = {roman[i]: vals[i] for i in range(len(roman))}

def romanToInteger(s):
    ret_val = 0
    zipp = zip(s, s[1:])
    for a, b in zipp:
        if hmp_rom_val[a] < hmp_rom_val[b]:
            ret_val -= hmp_rom_val[a]
        else:
            ret_val += hmp_rom_val[a]
    ret_val += hmp_rom_val[s[-1]]
    return ret_val

print(romanToInteger("MCMXCIV"))