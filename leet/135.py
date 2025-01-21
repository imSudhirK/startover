# Candy
# https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

def minCandy(ratings):
    num_ratings = len(ratings)
    candy = [1] * num_ratings
    for i in range(1, num_ratings):
        if ratings[i] > ratings[ i - 1]:
            candy[i] = candy[i - 1] + 1
    for i in range(num_ratings - 1, 0, -1):
        if ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
            candy[i - 1] = candy[i] + 1
    return sum(candy)

print(minCandy([1,3,4,5,2]))