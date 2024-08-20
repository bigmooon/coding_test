def calculate_scores(ryan, info):
  ryan_score, apeach_score = 0, 0
  for i in range(11):
    if ryan[i] > info[i]:
      ryan_score += 10 - i
    elif info[i] > 0 and ryan[i] <= info[i]:
      apeach_score += 10 - i

  return ryan_score, apeach_score

def update_answer(answer, ryan, ryan_score, apeach_score, diff):
  if ryan_score > apeach_score:
    if diff < ryan_score - apeach_score:
      return ryan[:], ryan_score - apeach_score
    elif diff == ryan_score - apeach_score:
      for j in range(10, -1, -1):
        if ryan[j] < answer[j]:
          break
        if ryan[j] > answer[j]:
          return ryan[:], ryan_score - apeach_score
  
  return answer, diff

def dfs(shooted_arrow, idx, n, info, ryan, answer, diff):
  if shooted_arrow == n:
    ryan_score, apeach_score = calculate_scores(ryan, info)
    return update_answer(answer, ryan, ryan_score, apeach_score, diff)

  for i in range(idx, 11):
    ryan[i] += 1
    answer, diff = dfs(shooted_arrow + 1, i, n, info, ryan, answer, diff)
    ryan[i] -= 1
  
  return answer, diff


def solution(n, info):
  answer = []
  ryan = [0] * 11
  diff = 0

  answer, diff = dfs(0, 0, n, info, ryan, answre, diff)

  return answer if answer else [-1]