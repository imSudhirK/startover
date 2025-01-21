# Delete Operation for Two Strings
# https://leetcode.com/problems/delete-operation-for-two-strings/description/

# find longest common subsequence length
def LCS(word1, word2):
    lw1, lw2 = len(word1), len(word2)
    dp = [[0]* (lw2 + 1) for _ in range(lw1 + 1)]
    for i in range(1, lw1 + 1):
        for j in range(1, lw2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[lw1][lw2]

def minDistance(word1, word2):
    len_lcs = LCS(word1, word2)
    return len(word1) + len(word2) - 2 * len_lcs

print(minDistance("leetcode", "etco"))