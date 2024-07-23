import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘림

class Tree:
    def __init__(self, dataList):
        # 주어진 데이터 리스트에서 가장 큰 값을 데이터로 설정
        self.data = max(dataList, key=lambda x: x[1])
        
        # 왼쪽 서브트리를 위한 데이터 리스트 필터링
        leftList = list(filter(lambda x: x[0] < self.data[0], dataList))
        # 오른쪽 서브트리를 위한 데이터 리스트 필터링
        rightList = list(filter(lambda x: x[0] > self.data[0], dataList))

        # 왼쪽 서브트리가 존재하면 Tree 객체 생성
        if leftList != []:
            self.left = Tree(leftList)
        else:
            self.left = None  # 왼쪽 서브트리가 없으면 None으로 설정

        # 오른쪽 서브트리가 존재하면 Tree 객체 생성
        if rightList != []:
            self.right = Tree(rightList)
        else:
            self.right = None  # 오른쪽 서브트리가 없으면 None으로 설정

def fix(node, postList, preList):
    # 현재 노드의 데이터를 후위 리스트에 추가
    postList.append(node.data)
    
    # 왼쪽 자식이 있으면 재귀적으로 후위 및 전위 순회를 수행
    if node.left is not None:
        fix(node.left, postList, preList)
    
    # 오른쪽 자식이 있으면 재귀적으로 후위 및 전위 순회를 수행
    if node.right is not None:
        fix(node.right, postList, preList)

    # 현재 노드의 데이터를 전위 리스트에 추가
    preList.append(node.data)

def solution(nodeinfo):
    answer = []
    # 주어진 노드 정보를 기반으로 트리 생성
    root = Tree(nodeinfo)
    
    postList = []  # 후위 순회 결과를 저장할 리스트
    preList = []   # 전위 순회 결과를 저장할 리스트
    
    # 트리를 후위 및 전위 순회하여 리스트에 저장
    fix(root, postList, preList)
    
    # 후위 순회 결과의 인덱스를 1부터 시작하는 형태로 변환하여 추가
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, postList)))
    # 전위 순회 결과의 인덱스를 1부터 시작하는 형태로 변환하여 추가
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, preList)))
    
    return answer  # 후위 및 전위 순회 결과를 반환