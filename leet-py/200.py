# Number of Islands
# https://leetcode.com/problems/number-of-islands/description/


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

m, n = len(grid), len(grid[0])

def dfs(i, j):
    if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
        grid[i][j] = '2'
        for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
            dfs(ii, jj)

count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '1':
            count += 1
            dfs(i, j)

print(count)
