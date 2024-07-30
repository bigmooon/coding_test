def solution(n, words):
  used_words = []
  player = 0
  failed_round = 0
  
  used_words.append(words[0]) # 시작 단어 추가
  last_word = words[0][-1]

  # 탈락 조건 : 이미 있거나, 앞 단어 마지막이랑 뒤의 단어 처음 일치x
  for i in range(1, len(words)):
    if words[i] not in used_words and words[i][0] == last_word:
      used_words.append(words[i])
      last_word = words[i][-1]
    else:
      player = (i % n) + 1
      failed_round = (i // n) + 1
      break

  return [player, failed_round]

