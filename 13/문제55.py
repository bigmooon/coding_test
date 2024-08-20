import heapq

def solution(arr1, arr2):
  # result = list(heapq.merge(arr1, arr2))
  result = []
  i, j = 0, 0
  
  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      result.append(arr1[i])
      i += 1
    else:
      result.append(arr2[j])
      j += 1

  # 남은 배열 추가해주기

  while i < len(arr1):
    result.append(arr1[i])
    i += 1
  
  while j < len(arr2):
    result.append(arr2[j])
    j += 1

  return result

print(solution([1, 3, 5], [2, 4, 6]))
print(solution([1, 2, 3], [4, 5, 6]))
