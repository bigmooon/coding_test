def solution(participant, completion):
  hashtable = {}

  for i in participant:
    if i in hashtable:
      hashtable[i] += 1
    else:
      hashtable[i] = 1

  for j in completion:
    if hashtable[j]:
      hashtable[j] -= 1
  
  for k in hashtable:
    if hashtable[k] > 0:
      return k     

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
