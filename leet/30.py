# Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter

def findSubstring(s, words):
    ls, word_ln = len(s), len(words[0])
    words_counter = Counter(words)
    start_indx_arr = []
    for i in range(word_ln):
        start_indx = i
        current_counter = Counter()
        for right_indx in range(i, ls + 1 - word_ln, word_ln):
            word = s[right_indx : right_indx + word_ln]
            if word in words_counter:
                current_counter[word] += 1
                while current_counter[word] > words_counter[word]:
                    starting_word = s[start_indx: start_indx + word_ln]
                    start_indx += word_ln
                    current_counter[starting_word] -= 1
                if current_counter == words_counter:
                    start_indx_arr.append(start_indx)
            else:
                current_counter.clear()
                start_indx = right_indx + word_ln
    return start_indx_arr

print(findSubstring("barfoothefoobarman", ["foo","bar"]))
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(findSubstring("aaaaaaaaaaaaaa", ["aa","aa"]))
