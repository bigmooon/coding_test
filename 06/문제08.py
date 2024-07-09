def solution(s):
  stack = []
  
  for char in s:
    if char == "(":
      stack.append(char)

    elif char == ")":
      # 만약 stack이 비어있으면
      if len(stack) == 0:
        return False
      else:
        stack.pop()

  # 만약 마지막에 (이 존재
  if len(stack) != 0:
    return False
  return True

print(solution("(())()"))
print(solution("((())()"))      