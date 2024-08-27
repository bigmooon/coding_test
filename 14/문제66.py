def solution(topping):
  result = 0
  left = {}
  right = {}

  # 각 토핑 갯수 저장
  for i in range(len(topping)):
    topping_idx = topping[i]
    right[topping_idx] = right.get(topping_idx, 0) + 1

  for i in range(len(topping)):
    topping_idx = topping[i]
    left[topping_idx] = left.get(topping_idx, 0) + 1
    
    right_item = right.get(topping_idx)
    if right_item - 1 == 0:
      right.pop(topping_idx)
    else:
      right[topping_idx] = right_item - 1

    if len(left.keys()) == len(right.keys()):
      result += 1
  
  return result