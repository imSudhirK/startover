# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter

def minWindow(s, t):
    ls = len(s)
    tcounter = Counter(t)
    win_counter = Counter()
    min_win = s + "1"
    start_indx = 0
    for right_indx, c in enumerate(s):
        win_counter[c] += 1
        while start_indx < right_indx and win_counter[s[start_indx]] > tcounter[s[start_indx]]:
            win_counter[s[start_indx]] -= 1
            start_indx += 1
        if win_counter >= tcounter and len(min_win) >= right_indx + 1 - start_indx:
            min_win = s[start_indx: right_indx + 1]
    return min_win if len(min_win) <= ls else ""

print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
print(minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
print(minWindow("abc", "b"))
