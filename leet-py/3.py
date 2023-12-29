# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

inp_str = input("Enter string: ")

start_indx = max_len = 0
hash_seen = {}

for curr_indx, character in enumerate(inp_str):
    if hash_seen.get(character, -1) >= start_indx:
        start_indx = hash_seen[character] + 1
    hash_seen[character] = curr_indx
    max_len = max(max_len, curr_indx + 1 - start_indx)

print("Length of Longest non-repeating character: ", max_len)