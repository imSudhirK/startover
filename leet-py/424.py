# Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement
from collections import Counter

s = "ABABABBACCD"
k = 2

low_ptr = 0 
hmp = Counter()

for high_ptr, c in enumerate(s):
    hmp[c] += 1
    most_common_char_freq = hmp.most_common(1)[0][1]
    if high_ptr - low_ptr - most_common_char_freq > k:
        hmp[s[low_ptr]] -= 1
        low_ptr += 1

# since gap = high_ptr - low_ptr is increasing function
print("Longest substring with at most k distinct characters: ", high_ptr - low_ptr)

