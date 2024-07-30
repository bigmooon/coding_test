import heapq

def solution(graph, start):
    # 최소 비용을 저장할 딕셔너리 초기화
    min_cost = {node: float('inf') for node in graph}
    min_cost[start] = 0  # 시작 노드의 비용은 0

    # 최단 경로를 추적하기 위한 딕셔너리
    previous = {node: None for node in graph}

    # 우선순위 큐 초기화
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (비용, 노드) 형태로 추가

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)  # 가장 비용이 적은 노드 추출

        # 현재 노드의 비용이 이미 기록된 최소 비용보다 크면 무시
        if current_cost > min_cost[current_node]:
            continue

        # 인접 노드와 가중치 확인
        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight  # 현재 노드를 통해 인접 노드로 가는 비용 계산

            # 더 작은 비용이면 업데이트
            if cost < min_cost[neighbor]:
                min_cost[neighbor] = cost
                previous[neighbor] = current_node  # 이전 노드를 업데이트
                heapq.heappush(priority_queue, (cost, neighbor))  # 우선순위 큐에 추가

    # 최단 경로 결과 생성
    shortest_paths = {}
    for node in graph:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()  # 경로를 역순으로 저장하였으므로 역으로 뒤집기
        shortest_paths[node] = {
            'cost': min_cost[node],
            'path': path
        }

    return shortest_paths
