def solution(n):
  arr = [1] * n
  if n >= 2:
    arr[1] = 1
    for i in range(2, n):
      arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567

  return arr[-1]

print(solution(3))
print(solution(5))