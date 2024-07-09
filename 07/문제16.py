from collections import deque

def solution(progresses, speeds):
  answer = []
  release = 0
  
  for i in range(len(progresses)):
    if progresses[i] >= 100 :  # 개발된 기능
      release += 1
    else:
      answer.append(release)
      release = 1
      while progresses[i] < 100:
        for j in range(i, len(progresses)):
          progresses[j] += speeds[j]
    
  answer.append(release)
  answer.remove(answer[0])

  return answer

# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]