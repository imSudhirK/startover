# Given an array of integers and a number k, 
# write a function that returns true 
# if the given array can be divided into pairs 
# such that the 
# sum of every pair is divisible by k.


# Input: arr = [9, 7, 5, 3], k = 6
# Output: True
# Input: arr[] = [91, 74, 66, 48], k = 10
# Output: False

def helper(arr, k):
    la =  len(arr)
    if not la: return False
    if la % 2: return False
    if not k: return False
    return check(arr, k)

def check(arr, k):
    la = len(arr)
    if not la: return True
    isFound = False
    for i in range(1, la):
        if not (arr[i] + arr[0]) % k:
            arr.pop(i)
            arr.pop(0)
            isFound = True
            break
    if not isFound: return False
    return check(arr, k)

print(helper([9, 7, 6, 3], 6))
print(helper([91, 74, 66, 48], 10))