def rotate_90(arr):
  arr_len = len(arr)
  answer = [[0] * arr_len for _ in range(arr_len)]
  for i in range(arr_len):
    for j in range(arr_len):
      answer[j][arr_len - 1 - i] = arr[i][j]
  return answer

def solution(arr, n):
  for _ in range(n):
    arr = rotate_90(arr)
  return arr

print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2))
