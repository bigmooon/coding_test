def solution(str1, str2):
  str1_len = len(str1)
  str2_len = len(str2)

  dp = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]

  for i in range(1, str1_len + 1):
    for j in range(1, str2_len + 1):
      if str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  
  return dp[str1_len][str2_len]

print(solution("ABCBDAB", "BDCAB"))
print(solution("AGGTAB", "GXTXAYB"))
