def DFS(i, computers, visited):
  visited[i] = 1
  for j in range(len(computers)):
    if computers[i][j] and not visited[j]:  # 연결된 노드이면서 방문하지 않은 경우
      DFS(j, computers, visited)


def solution(n, computers):
  answer = 0
  visited = [0 for _ in range(n)]
  for i in  range(n):
    if not visited[i]:
      DFS(i, computers, visited)
      answer += 1
  
  return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))