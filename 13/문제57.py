def solution(n):
  change_string = list(str(n))
  change_string.sort(reverse=True)
  return int("".join(change_string))

print(solution(118372))
