def solution(array, commands):
  # answer = []
  # for cmd in commands:
  #   i, j, k = cmd
  #   sliced_array = array[i -1: j]
  #   sliced_array.sort()
  #   answer.append(sliced_array[k - 1])

  # return answer

  return [(sorted(array[i-1:j])[k - 1]) for i, j, k in commands]

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # [5, 6, 3]