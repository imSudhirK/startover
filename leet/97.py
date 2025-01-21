# Interleaving String
# https://leetcode.com/problems/interleaving-string/description

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

def isInterleaveV1(s1, s2, s3):
    l1, l2, l3 = len(s1), len(s2), len(s3)
    if l1 + l2 != l3: return False
    # check if its possible to create s3 of from index i3
    # using index i1, i2, from in s1, s2 respectively till end
    def checkInterleaving(i1, i2, i3):
        if i1 >= l1: return s2[i2 : ] == s3[i3 : ]
        if i2 >= l2: return s1[i1 : ] == s3[i3 : ]
        if s3[i3] == s1[i1] and s3[i3] == s2[i2]:
            return checkInterleaving(i1 + 1, i2, i3 + 1) or checkInterleaving(i1, i2 + 1, i3 + 1)
        if s3[i3] == s1[i1]:
            return checkInterleaving(i1 + 1, i2, i3 + 1)
        if s3[i3] == s2[i2]:
            return checkInterleaving(i1, i2 + 1, i3 + 1)
        return False
    # call the above function
    return checkInterleaving(0, 0, 0)

def isInterleaveV2(s1, s2, s3):
    l1, l2, l3 = len(s1), len(s2), len(s3)
    if l1 + l2 != l3: return False

    # check if its possible to create s3 of from index i3
    # using index i1, i2, from in s1, s2 respectively till end
    dp = [[[-1] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    def checkInterleaving(i1, i2, i3):
        if dp[i1][i2][i3] != -1:
            return dp[i1][i2][i3]
        if i1 >= l1:
            ans = s2[i2 : ] == s3[i3 : ]
            dp[i1][i2][i3] = ans
            return ans
        if i2 >= l2:
            ans = s1[i1 : ] == s3[i3 : ]
            dp[i1][i2][i3] = ans
            return ans
        if s3[i3] == s1[i1] and s3[i3] == s2[i2]:
            ans = checkInterleaving(i1 + 1, i2, i3 + 1)
            dp[i1][i2][i3] = ans
            if ans: return ans
            ans = checkInterleaving(i1, i2 + 1, i3 + 1)
            dp[i1][i2][i3] = ans
            return ans
        if s3[i3] == s1[i1]:
            ans = checkInterleaving(i1 + 1, i2, i3 + 1)
            dp[i1][i2][i3] = ans
            return ans
        if s3[i3] == s2[i2]:
            ans = checkInterleaving(i1, i2 + 1, i3 + 1)
            dp[i1][i2][i3] = ans
            return ans
        return False
    # call the above function
    return checkInterleaving(0, 0, 0)

def isInterleaveV3(s1, s2, s3):
    l1, l2, l3 = len(s1), len(s2), len(s3)
    if l1 + l2 != l3: return False
    # dp[i][j] = True means first i, j from s1, s2 respectively
    # could form first i + j in s3
    dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
    dp[0][0] = True
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]
    return dp[l1][l2] 

print(isInterleaveV3(s1, s2, s3))

