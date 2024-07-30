def solution(graph, source):
  # 노드의 수
  n = len(graph)

  # 초기거리 설정
  distance = [float('inf')] * n
  distance[source] = 0 # 시작 노드의 거리

  # 각 노드의 최단 경로에서 직전 노드 저장
  predecessor = [None] * n

  # 그래프의 모든 엣지 n-1번 반복
  for _ in range(n - 1):
    for u in range(n):
      for v, weight in graph[u]:
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
          distance[v] = distance[u] + weight # v까지 최단 거리 업데이트
          predecessor[v] = u
  
  # 음의 가중치 순회
  for u in range(n):
    for v, weight in graph[u]:
      if distance[u] != float('inf') and distance[u] + weight < distance[v]:
        return [-1]
  
  return [distance, predecessor]

print(solution([[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]], 0))
print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0))