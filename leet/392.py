
def isSubsequence(s, t):
    ls, lt = len(s), len(t)
    si, ti = 0, 0
    while si < ls and ti < lt:
        if s[si] == t[ti]:
            si += 1
        ti += 1
    if si == ls: return True
    return False

print(isSubsequence("abc", "ahbgdc"))