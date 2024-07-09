def solution(s):
  
  def is_correct(s):
    bracket_pairs = {
      ')':'(',
      ']':'[',
      '}':'{'
    }

    # 첫 시작이 닫는 괄호면 F
    if s[0] in bracket_pairs.keys():
      return False
    else:
      stack = []
      for i in s:
        # 닫는 괄호, stack에 pop 할 것이 있다면
        if i in bracket_pairs.keys() and stack:
          if bracket_pairs[i] != stack.pop():
            return False
        else:
          stack.append(i)
      
      # stack이 비어있으면 T
      return True if not stack else False
  
  answer = 0

  for j in range(len(s)):
    if is_correct(s[j:] + s[:j]):
      answer += 1 

  return answer

