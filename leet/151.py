# Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150


def reverseWords(s):
    words = s.strip().split()
    words.reverse()
    return " ".join(words)

print(reverseWords("  hello world  "))