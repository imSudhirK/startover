# a = [1,2,3,4,5]
# t = 7
# r = [[2,5], [3,4], [1, 2, 4]]


arr = [1,2,3,4,5]
target = 7


res = []
la = len(arr)
def backtrack(i, ret):
    if sum(ret) == target and ret not in res:
        res.append(ret)
    if i >= la:
        return
    
    backtrack(i + 1, ret.copy() + [arr[i]])
    backtrack(i + 1, ret.copy())

backtrack( 0, [])

print(res)
    




