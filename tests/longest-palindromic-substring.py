# velocity
# Given a string s,
# return the longest palindromic substring in s

# example 
s = "babad"

# solution
def bruteForce(s):
    def isPalindromicString(ss):
        lss = len(ss)
        mid = lss // 2
        for ind in range(mid + 1):
            if ss[ind] != ss[-1 * (ind + 1)]:
                return False
        return True
    
    def longestPalindromicSubstring(s):
        ls = len(s)
        for si in range(ls):
            li = ls
            while si < li:
                ss = s[si : li]
                if isPalindromicString(ss):
                    return ss
                li -= 1
        return ""
    
    return longestPalindromicSubstring(s)

print('bruteForce', bruteForce(s))

# solution
def dynamicProgramming(s):
    ls = len(s)
    if not ls: return ""

    start, max_ln = 0, 1
    dp = [[False] * ls for _ in range(ls)]
    for i in range(ls): dp[i][i] = True

    for ln in range(2, ls + 1):
        for si in range(ls + 1 - ln):
            li = si + ln - 1
            if s[si] == s[li] and dp[si + 1][li - 1]:
                dp[si][li] = True
                start = si
                max_ln = ln
    
    return s[start: start + max_ln]

print('dynamicProgramming', dynamicProgramming(s))

# solution
def expandAroundCenter(s):
    def expandAround(leftInd, rightInd):
        ls = len(s)
        while leftInd >= 0 and rightInd < ls and s[leftInd] == s[rightInd]:
            leftInd -= 1
            rightInd += 1
        return s[leftInd + 1 : rightInd]

    ls = len(s)
    if not ls: return ""
    lps = ""
    for i in range(ls):
        oddPS = expandAround(i, i)
        evenPS = expandAround(i, i + 1)
        if len(oddPS) > len(lps): lps = oddPS
        if len(evenPS) > len(lps): lps = evenPS
    
    return lps

print('expandAroundCenter', expandAroundCenter(s))