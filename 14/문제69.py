def solution(keyinput, board):
  x, y = 0, 0 # 초기 좌표

  moves = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}

  width, height = board[0] // 2, board[1] // 2

  for key in keyinput:
    dx, dy = moves[key]
    if (-width <= x + dx <= width and -height <= y + dy <= height):
      x += dx
      y += dy
    
  return [x, y]

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))