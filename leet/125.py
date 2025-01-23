# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description


def isPalindromeV1(s):
    arr = []
    for c in s:
        if c.isalnum():
            arr.append(c.lower())

    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    return True

def isPalindromeV2(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


    

print(isPalindromeV2("A man, a plan, a canal: Panama"))