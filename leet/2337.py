# Move Pieces to Obtain a String
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/

def canChangeV1(s, t):
    ls, lt = len(s), len(t)
    if ls != lt: return False
    oos, lcs, rcs, ccs = '', [], [], 0
    oot, lct, rct, cct = '', [], [], 0

    for i in range(ls):
        if s[i] == '_':
            ccs += 1
        elif s[i] == 'L':
            oos += 'L'
            lcs.append(ccs)
        else:
            oos += 'R'
            rcs.append(ccs)
        
        if t[i] == '_':
            cct += 1
        elif t[i] == 'L':
            oot += 'L'
            lct.append(cct)
        else:
            oot += 'R'
            rct.append(cct)

    if oos != oot: return False
    ll, lr = len(lcs), len(rcs)
    for i in range(ll):
        if lcs[i] < lct[i]:
            return False
    for i in range(lr):
        if rcs[i] > rct[i]:
            return False
    
    return True

def canChangeV2(start, target):
    if start.replace("_", "") != target.replace("_", ""):
        return False
    
    startLi = [i for i, c in enumerate(start) if c == 'L']
    startRi = [i for i, c in enumerate(start) if c == 'R']
    targetLi = [i for i, c in enumerate(target) if c == 'L']
    targetRi = [i for i, c in enumerate(target) if c == 'R']

    for s, t in zip(startLi, targetLi):
        if s < t: return False
    for s, t in zip(startRi, targetRi):
        if s > t: return False
    
    return True

print(canChangeV1("_L__R__R_", "L______RR"))
print(canChangeV2("_L__R__R_", "L______RR"))