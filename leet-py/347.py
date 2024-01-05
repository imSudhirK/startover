# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

hs_lst = list(Counter(nums).items())
hs_lst.sort(key = lambda pair: pair[1], reverse= True)
answer0 = [pair[0] for i, pair in enumerate(hs_lst) if i < k]
print("Answer: ", answer0)


nums_freq = {n: 0 for n in nums}
for n in nums: nums_freq[n] += 1
vals = nums_freq.keys()
freqs = nums_freq.values()
res = [x for x, _ in sorted(zip(vals, freqs), key= lambda p: p[1], reverse= True)]
res = res if len(res) <= k else res[:k]
print("Answer1: ", res)