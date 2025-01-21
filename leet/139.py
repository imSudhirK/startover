# Word Break
# https://leetcode.com/problems/word-break/description


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wd = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# s = "applepenapple"
# wd = ["apple","pen"]

def wordBreakV1(s, wordDict):
    ls = len(s)
    # dp[i][j] == True means words from index i to j in s exists in word Dict
    dp = [[False] * ls for _ in range(ls)]
    for i in range(ls):
        for j in range(i, ls):
            sub_s = s[i : j + 1]
            if sub_s in wordDict:
                dp[i][j] = True
    
    # is possible to break string starting at index i till end
    def isPossible(i):
        if i >= ls: return True
        for j in range(i, ls):
            a = isPossible(j + 1)
            print(i, j, dp[i][j], a)
            if dp[i][j] and a:
                return True
        return False

    return isPossible(0)


def wordBreakV2(s, wordDict):
    ls = len(s)
    dp = [[False] * ls for _ in range(ls)]
    for i in range(ls):
        for j in range(i, ls):
            sub_s = s[i : j + 1]
            if sub_s in wordDict:
                dp[i][j] = True
    
    # -1, not computed yet, 1 computed and affirmative, 0 computed and negative
    disp = [-1]* (ls + 1)
    # base case if index exceeds we dont need to check
    disp[ls] = 1 
    def isPossible(i):
        if disp[i] == 1: return True
        elif disp[i] == 0: return False
        for j in range(i, ls):
            if dp[i][j] and isPossible(j + 1):
                disp[i] = True
                return True
        disp[i] = False
        return False

    return isPossible(0)


def wordBreakV3(s, wordDict):
    ls = len(s)
    dp = [False] * (ls + 1)
    dp[0] = True
    for i in range(1, ls + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[ls]

print(wordBreakV3(s, wd))

