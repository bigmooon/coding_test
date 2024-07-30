from collections import defaultdict, deque

def solution(graph, start):
  adj_list = defaultdict(list)
  for u, v in graph:
    adj_list[u].append(v)
    adj_list[v]

  visited = set()
  result = []
  queue = deque([start])

  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      result.append(node)
      # 인접한 모든 노드 큐에 추가
      for neighbor in sorted(adj_list[node]):
        if neighbor not in visited:
          queue.append(neighbor)

  return result

print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1))
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))

