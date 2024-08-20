def solution(n):
  # 정답을 담는 나선형 배열 초기화
  snail_array = [[0] * n for _ in range(n)]
  
  # 우하상좌
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  dir_index = 0 # 현재 방향 인덱스
  row, col = 0, 0

  for num in range(1, n * n + 1):
    snail_array[row][col] = num

    next_row = row + directions[dir_index][0]
    next_col = col + directions[dir_index][1]

    if (next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or snail_array[next_row][next_col] != 0):
      dir_index = (dir_index + 1) % 4

      next_row = row + directions[dir_index][0]
      next_col = col + directions[dir_index][1]
    
    row, col = next_row, next_col

  return snail_array

print(solution(3))
print(solution(4))