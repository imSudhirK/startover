# Largest Substring Between Two Equal Characters
# https://leetcode.com/problems/largest-substring-between-two-equal-characters

s = 'abbbaccbdfha'

len_largest_substr = -1
for indx, character in enumerate(s):
    first_indx = s.find(character)
    len_largest_substr = max(len_largest_substr, indx - 1 - first_indx)

print("Lenght of largest substring between two equal charatcters: ", len_largest_substr)