from itertools import combinations

def solution(orders, course):
  course_menu = []

  # 메뉴의 갯수에 대하여
  for num in course:
    ordered_menu = {}
    for order in orders:
      for combo in combinations(sorted(order), num):
        combo = ''.join(combo)
        if combo in ordered_menu:
          ordered_menu[combo] += 1
        else: 
          ordered_menu[combo] = 1

    if ordered_menu:
      max_menu = max(ordered_menu.values())
      
      if max_menu >= 2:
        for menu, count in ordered_menu.items():
          if count == max_menu:
            course_menu.append(menu)

  return sorted(course_menu)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))