def solution(n):
  arr = [1] * n
  if n >= 2:
    arr[1] = 2
    for i in range(2, n):
      arr[i] = (arr[i - 1] + arr[i - 2])%1000000007

  return arr[-1]

print(solution(4))