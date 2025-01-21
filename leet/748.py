# Shortest Completing Word
# https://leetcode.com/problems/shortest-completing-word/

from collections import Counter

license_plate = "1s3 PSt"
words = ["stripe", "steps", "stepple", "step"]

print((p:= Counter([c.lower() for c in license_plate if c.isalpha()])) and min([w for w in words if Counter(w) >= p], key=len))

hlp = Counter([c.lower() for c in license_plate if c.isalpha()])
res = min([w for w in words if Counter(w) >= hlp], key=len)
print(res)
# words.sort(key=len)
# words.sort(key = lambda w : len(w))
