from collections import defaultdict

def solution(graph, start):
  adj_list = defaultdict(list)
  
  for u, v in graph:
    adj_list[u].append(v)
    adj_list[v] # v가 다른 노드의 출발점일 수 있으므로

  
  def dfs(node, visited):
    visited.add(node)
    result.append(node)

    # 현재 노드와 연결된 모든 인접 노드 순회
    for neighbor in sorted(adj_list[node]):
      if neighbor not in visited:
        dfs(neighbor, visited)

  visited = set()
  result = []
  dfs(start, visited)

  return result


print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'))
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))