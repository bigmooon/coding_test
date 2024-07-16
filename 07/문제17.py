from collections import deque

def solution(cards1, cards2, goal):
  cards1 = deque(cards1)
  cards2 = deque(cards2)
  goal = deque(goal)

  idx_cards1, idx_cards2 = 0, 0

  # 1번 덱 혹은 2번 덱에 골의 첫 번째 문장이 있는 경우
  while goal:    
    if idx_cards1 < len(cards1) and goal[0] == cards1[idx_cards1]:
        goal.popleft()
        idx_cards1 += 1
        # continue

    elif idx_cards2 < len(cards2) and goal[0] == cards2[idx_cards2]:
      goal.popleft()
      idx_cards2 += 1
      # continue
    
    else:
      return "NO"
     
  if len(goal) == 0:
    return "YES"
  else  :
    return "NO"
       
print(solution(["i", "water", "drink"], ["want, to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))