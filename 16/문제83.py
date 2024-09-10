def solution(people, limit):
  people.sort()
  thin = 0
  fat = len(people) - 1
  boats = 0

  while thin <= fat:
    if people[thin] + people[fat] <= limit:
      thin += 1
    fat -= 1
    boats += 1

  return boats

print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3