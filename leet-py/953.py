# Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

hs_od = {c : i for i, c in enumerate(order)}

num_words = [[hs_od[c] for c in w] for w in words]
sorted_num_words = num_words.copy()
sorted_num_words.sort() 
print(sorted_num_words == num_words)


# print(hs_od.keys())
# print(hs_od.values())