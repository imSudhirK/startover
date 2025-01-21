# Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

strs = ["eat","tea","tan","ate","nat","bat"]
hmp = {}
for w in strs:
    w_sorted = ''.join(sorted(w))
    if w_sorted in hmp:
        hmp[w_sorted].append(w)
    else:
        hmp[w_sorted] = [w]

print("Group Anagrams: ", hmp.values())
