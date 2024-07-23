def solution(N, A, B):
  round = 0
  while A != B:
    A, B = (A + 1) // 2, (B + 1) //2
    round += 1

  return round