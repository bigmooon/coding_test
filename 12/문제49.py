def solution(k, dungeons):
  max_cleared = 0

  def backtrack(current_k, cleared_cnt, visited):
    nonlocal max_cleared 
    max_cleared = max(max_cleared, cleared_cnt)

    for i in range(len(dungeons)):
      if not visited[i]:
        required_fatigue = dungeons[i][0]
        consumed_fatigue = dungeons[i][1]

        if current_k >= required_fatigue:
          visited[i] = True
          backtrack(current_k - consumed_fatigue, cleared_cnt + 1, visited)
          visited[i] = False
  
  visited = [False] * len(dungeons)
  backtrack(k, 0, visited)

  return max_cleared
    

print(solution(80, [[80, 20], [50, 40], [30, 10]]))