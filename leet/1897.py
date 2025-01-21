# Redistribute Characters to Make All Strings Equal
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from collections import Counter

words = ["abc","aabbb","bc"]

hmp = Counter()
lw = len(words)
ans = True

for w in words: hmp.update(w)
for v in hmp.values():
    if v%lw: ans = False

print("Answer: ", ans)

array = list(hmp.items())
array.sort(key= lambda tpl: tpl[1])
print(array)