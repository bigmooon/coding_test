class Node:
  # 노드 값 초기화
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    # 이진 탐색 트리 초기화
    self.root = None


  def insert(self, key):
    # 주어진 값을 이진 탐색 트리에 삽입
    if not self.root:
      # 트리가 비어 있으면 새로운 노드를 루트로 설정
      self.root = Node(key)
    else:
      # 비어있지 않으면 현재 노드를 루트로 설정하고 삽입
      curr = self.root
      while True:
        if key < curr.key:
          if not curr.left:
            curr.left = Node(key)
            break
          else:
            curr = curr.left
        else:
          if not curr.right:
            curr.right = Node(key)
            break
          else:
            curr = curr.right


  def search(self, key):
    curr = self.root
    while curr:
      if key == curr.key:
        return True
      elif key < curr.key:
        curr = curr.left
      else:
        curr = curr.right
    return False


def solution(lst, search_lst):
  bst = BST()
  
  for key in lst:
    bst.insert(key)
  
  answer = []
  for search_key in search_lst:
    answer.append(bst.search(search_key))

  return answer


print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))
print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
