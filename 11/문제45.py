import heapq

def is_valid(x, y, n, board):
  return 0 <= x < n and 0 <= y < n and board[x][y] == 0


def calculate_cost(current_cost, prev_direction, new_direction):
  # if prev_direction == new_direction:
  if prev_direction == -1 or prev_direction == new_direction:
    return current_cost + 100
  else:
    return current_cost + 600


def min_cost(board):
  n = len(board)
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상

  # 비용 저장 배열
  cost = [[float('inf')] * n for _ in range(n)]
  cost[0][0] = 0 # 시작점 비용 

  heap = []
  heapq.heappush(heap, (0, 0, 0, -1)) # 비용, x, y, 이전 방향
  

  while heap:
    current_cost, x, y, prev_direction = heapq.heappop(heap)

    # 현재 위치의 비용이 이미 더 크면 무시
    if current_cost > cost[x][y]: 
      continue
    
    # 모든 방향으로 이동 시도
    for i, (dx, dy) in enumerate(directions):
      # 새 위치 계산
      nx, ny = x + dx, y + dy

      if is_valid(nx, ny, n, board):
        new_cost = calculate_cost(current_cost, prev_direction, i)

        if new_cost < cost[nx][ny]:
          cost[nx][ny] = new_cost
          heapq.heappush(heap, (new_cost, nx, ny, i))

  # 목적지의 최소 비용 반환
  return cost[n-1][n-1]


def solution(board):
  return min_cost(board)


print(solution([    
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]))