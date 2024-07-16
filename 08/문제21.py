def solution(want, number, discount):
  # want와 number dict로 연결
  shopping_list = {}
  result = 0

  for w, n in zip(want, number):
    shopping_list[w] = n

  for start_day in range(len(discount) - 9):
    tmp = shopping_list.copy()
    for day in range(start_day, start_day + 10):
      if discount[day] in tmp and tmp[discount[day]] != 0:
        tmp[discount[day]] -= 1
      else:
        break
    
    if sum(tmp.values()) == 0:
      result += 1

  return result

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))