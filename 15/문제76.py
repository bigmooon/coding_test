def solution(land):
  dp = [[0] * 4 for _ in range(len(land))]
  dp[0] = land[0]

  for i in range(len(land)):
    for j in range(4):
      dp[i][j] = land[i][j] + max(dp[i - 1][:j] + dp[i - 1][j + 1:])
  return max(dp[len(land) - 1])

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])) # 16