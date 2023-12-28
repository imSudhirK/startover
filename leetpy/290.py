# Word Pattern
# https://leetcode.com/problems/word-pattern/description/

pattern = input("Enter pattern: ")
s = input("Enter line s: ")
s_arr = s.split()
s_arr_pattern_index = [s_arr.index(w) for w in s_arr]
pattern_index = [pattern.find(c) for c in pattern]
print("Does string follows given pattern: ", s_arr_pattern_index == pattern_index)