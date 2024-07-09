from collections import deque

def solution(N, K):
  queue = deque(range(1, N + 1))

  while len(queue) > 1:
    for i in range(K - 1):
      queue.append(queue.popleft()) # K 전까지 요소를 뒤로 보내기
      
      queue.popleft() # K번째 요소 pop
  return queue[0]

print(solution(5, 2))
