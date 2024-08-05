from itertools import combinations

def solution(N):
  results = []

  numbers = list(range(1, N + 1))

  for i in range(1, N + 1):
    for combo in combinations(numbers, i):
      if sum(combo) == 10:
        results.append(list(combo))
  
  return results

print(solution(5))
print(solution(2))
print(solution(7))