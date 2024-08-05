def solution(board):
  def is_valid(num, row, col):

    for i in range(9):
      if board[row][i] == num or board[i][col] == num:
        return False
    
    # 3x3 박스 안에 숫자가 있는 지 체크
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(3):
      for j in range(3):
        if board[box_row + i][box_col + j] == num:
          return False

    return True
  
  # 빈 칸 찾기
  def backtrack():
    for row in range(9):
      for col in range(9):
        if board[row][col] == 0: # 만약 보드의 숫자가 0이면 
          for num in range(1, 10):
            if is_valid(num, row, col): # 유효성 검사 통과하면 숫자를 0에서 다시 바꿈
              board[row][col] = num
              if backtrack():
                return True # 성공적으로 스도쿠 완성됨
              else:
                board[row][col] = 0

          return False
    return True

  backtrack()
  return board

print(solution([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]))

