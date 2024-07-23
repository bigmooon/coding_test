def solution(nums):
  set_nums = set(nums)
  max_selectable = len(nums) // 2

  return min(len(set_nums), max_selectable)

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))

  