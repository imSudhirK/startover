from collections import Counter


c00 = Counter("geeksforgeeks")
print("Counter is: ", c00)
for e in c00.elements():
    print(e, " : ", c00[e])
print("\n")


c01 = Counter([x for x in "balrampur"])
print(c01)
for k in c01.keys():
    print(k, " : ", c01[k])

c01_keys = list(c01.keys())
c01_values = list(c01.values())
print("List of keys: ", c01_keys)
print("List of values: ", c01_values)

hs00 = Counter([c for c in "as1as2lk4lk5" if c.isalpha()])
for c in hs00:
    print(c, " : ", hs00[c])
hs01 = Counter([c for c in "as1as2lk4l5" if c.isalpha()])
print("is hs00 > hs01: ", hs00 > hs01)
