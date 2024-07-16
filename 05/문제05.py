# 행렬의 곱셈 구현

def solution(arr1, arr2):
  # 행렬의 열, 행 나눠보기
  arr1_row, arr1_column = len(arr1), len(arr1[0])
  arr2_row, arr2_column = len(arr2), len(arr2[0])

  # 리턴되는 행렬은 arr1_row * arr2_column
  answer_arr = [[0] * len(arr2[0]) for _ in range(len(arr1))]

  # 값 계산하기
  for i in range(len(arr1)):
    for j in range(len(arr2[0])):
      for k in range(len(arr1[0])): 
        answer_arr[i][j] += arr1[i][k] * arr2[k][j]   # k는 위치를 잡기위해 있다(문기왈)

  return answer_arr
print(solution(([1, 4], [3, 2], [4, 1]), ([3, 3], [3, 3])))
print(solution(([2, 3, 2], [4, 2, 4], [3, 1, 4]), ([5, 4, 3], [2, 4, 1], [3, 1, 1])))