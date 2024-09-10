from collections import Counter

def solution(k, tangerine):
  tangerine_size = Counter(tangerine)

  cnt = sorted(tangerine_size.values(), reverse=True)
  boxes = 0
  total = 0

  for count in cnt:
    total += count
    boxes += 1
    if total >= k:
      break
    
  return boxes

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))