def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  # 부모 비교
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


def solution(n, costs):
  answer = 0
  parent = [_ for _ in range(n)]

  # 비용 기준으로 간선 리스트 정렬
  costs.sort(key = lambda x : x[2])

  for cost in costs:
    a, b, c = cost # c는 비용
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
      answer += c
  
  return answer