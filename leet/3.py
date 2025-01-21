# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

inp_str = input("Enter string: ")

def lengthOfLongestSubstringV1(s):
    max_len, start_indx = 0, 0
    hmap_cs = {}
    for last_indx, c in enumerate(s):
        while hmap_cs.get(c, 0):
            hmap_cs[s[start_indx]] = 0
            start_indx += 1
        hmap_cs[c] = 1
        max_len = max(max_len, last_indx + 1 - start_indx)
    return max_len

print(lengthOfLongestSubstringV1(inp_str))

def lengthOfLongestSubstringV2(s):
    max_len, start_indx = 0, 0
    latest_seen_at = {}
    for last_indx, c in enumerate(s):
        if latest_seen_at.get(c, -1) >= start_indx:
            start_indx = latest_seen_at[c] + 1
        latest_seen_at[c] = last_indx
        max_len = max(max_len, last_indx + 1 - start_indx)
    return max_len

print(lengthOfLongestSubstringV2(inp_str))