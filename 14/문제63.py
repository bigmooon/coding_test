def mul_matrix(matrix1, matrix2):
  multiplied_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  for i in range(3):
    for j in range(3):
      for k in range(3):
        multiplied_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

  return multiplied_matrix


def trans_matrix(matrix):
  transposed_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  for i in range(3):
    for j in range(3):
      transposed_matrix[j][i] = matrix[i][j]

  return transposed_matrix


def solution(matrix1, matrix2):
  mul = mul_matrix(matrix1, matrix2)
  result = trans_matrix(mul)

  return result


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))




