# Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

def minOperationsV1(boxes):
    n = len(boxes)
    ans = [0] * n
    for i in range(n):
        operations = 0
        for j in range(n):
            if i == j: continue
            if boxes[j] == '0': continue
            operations += abs(j - i)
        ans[i] = operations
    return ans


def minOperationsV2(boxes):
    n = len(boxes)
    ans = [0]*n
    operations = 0 
    right_ones = 0
    left_ones = 0
    # number of operations for position 0
    for i in range(1, n):
        # here is i is number of operations to move 1 ball from i th to 0th box
        if boxes[i] == '1':
            operations += i
            right_ones += 1
    ans[0] = operations
    # number of operations for other position
    for i in range(1, n):
        if boxes[i - 1] == '1': left_ones += 1
        # number of balls at left will add number of operations
        # number of balls at right will decrease number of operations 
        operations += left_ones - right_ones
        if boxes[i] == '1': right_ones -= 1
        ans[i] = operations
    return ans


def minOperationsV3(boxes):
    n = len(boxes)
    ans = [0] * n
    # number of operations to move all balls to i th position from its left side 
    operations = num_balls = 0
    for i in range(n):
        ans[i] +=  operations
        if boxes[i] == '1': num_balls += 1
        operations += num_balls
    # number of operations to move all balls to i th position from its right side 
    operations = num_balls = 0
    for i in range(n - 1, -1, -1):
        ans[i] += operations
        if boxes[i] == '1': num_balls += 1
        operations += num_balls
    return ans

print(minOperationsV1("001011"))
print(minOperationsV2("001011"))
print(minOperationsV3("001011"))