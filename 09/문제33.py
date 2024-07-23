class UnionFind:
  def __init__(self, size):
    self.parent = [_ for _ in range(size)]
    # 집합의 개수
    self.cnt = size

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x]) # 경로 압축 
    return self.parent[x]  


  def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)

    if rootX != rootY:
      self.parent[rootY] = rootX 
      # 집합 개수 줄이기
      self.cnt -=1


  def get_cnt(self):
    return self.cnt


def solution(k, operations):
  uf = UnionFind(k)

  for operation in operations:
    if operation[0] == 'u':
      _, x, y = operation
      uf.union(x, y)
    elif operation[0] == 'f':
      _, x = operation
      uf.find(x)
  
  return uf.get_cnt()


print(solution(3, [['u', 0, 1], ['u', 1, 2], ['f', 2]]))
print(solution(4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]))
