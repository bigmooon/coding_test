def solution(items, weight_limit):
  items.sort(key=lambda x: x[1] / x[0], reverse=True)

  total_value = 0
  total_weight = 0

  for weight, values in items:
    if total_weight + weight <= weight_limit:
      total_weight += weight
      total_value += values
    # 무게 초과
    else:
      total_value += values * (weight_limit - total_weight) / weight
      break

  return total_value

print(solution([[10, 19], [7, 10], [6, 10]], 15))
print(solution([[10, 60], [20, 100], [30, 120]], 50))

