def solution(N):
  result = 1

  while N != 1:
    if N % 2 == 0:
      N //= 2
    else:
      N -= 1
      result += 1
  
  return result

# 효율성 테스트 4 실패