def solution(s):
  cnt = [0] * 26
  answer = ""

  # 계수정렬 저장
  for word in s:
    cnt[ord(word) - ord("a")] += 1
  
  # cnt[i]는 문자 갯수, i는 아스키코드 - a
  for i in range(26):
    answer += chr(i + ord("a")) * cnt[i]

  return answer

print(solution("hello"))
print(solution("algorithm"))
