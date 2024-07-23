from collections import deque

class Node:
  def __init__(self, item):
    self.item = item
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None
  
  def insert_level_order(self, items):
    if not items:
      return None

    self.root = Node(items[0])
    queue = deque([self.root])
    i = 1
  
    while queue and i < len(items):
      current = queue.popleft()
      # 왼쪽 자식 추가
      if i < len(items):
        current.left = Node(items[i])
        queue.append(current.left)
        i += 1
      # 오른쪽 자식 추가
      if i < len(items):
        current.right = Node(items[i])
        queue.append(current.right)
        i += 1


  # 전위 순회 : 노드 -> 왼섭트 -> 오섭트
  def preorder(self, node):
    if node: 
      return [node.item] + self.preorder(node.left) + self.preorder(node.right)
    return []


  # 중위 순회 : 왼섭트 -> 노드 -> 오섭트
  def inorder(self, node):
    if node:
      return self.inorder(node.left) + [node.item] + self.inorder(node.right)
    return []


  # 후위 순회 : 왼섭트 -> 오섭트 -> 노드
  def postorder(self, node):
    if node:
      return self.postorder(node.left) + self.postorder(node.right) + [node.item]
    return []


def solution(nodes):
  tree = BinaryTree()
  tree.insert_level_order(nodes)

  preorder_result = tree.preorder(tree.root)
  inorder_result = tree.inorder(tree.root)
  postorder_result = tree.postorder(tree.root)

  return [
      " ".join(map(str, preorder_result)),
      " ".join(map(str, inorder_result)),
      " ".join(map(str, postorder_result))
  ]

if __name__ == "__main__":
  result = solution([1, 2, 3, 4, 5, 6, 7])
  print(result)