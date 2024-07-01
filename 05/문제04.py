def solution(answers):
  scores = [0] * 3

  patterns = [
    [1, 2, 3, 4, 5], # 1번 수포자
    [2, 1, 2, 3, 2, 4, 2, 5], # 2번 수포자
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자
  ]

  for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
      # 패턴보다 답의 길이가 넘어가면 오류 발생
      if answer == pattern[i % len(pattern)]:
        scores[j] += 1

  # 예외사항
  # 가장 높은 점수를 받은 사람이 여럿이면 반환값 오름차순 정렬
  # 동점 조건 => scores에서 가장 큰 수를 저장 후 비교해 오름차순 정렬
  max_score = max(scores)
  highest_student = []

  for k, score in enumerate(scores):
    if score == max_score:
      highest_student.append(k + 1)
  return highest_student

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))