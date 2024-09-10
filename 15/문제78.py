def solution(board):
  answer = 0

  # 세로, 가로 길이
  for i in range(1, len(board)):
    for j in range(1, len(board[0])):
      if board[i][j] == 1:
        board[i][j] = min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]) + 1        
        answer = max(answer, board[i][j] ** 2)

  return answer

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]])) # 9
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]])) # 4