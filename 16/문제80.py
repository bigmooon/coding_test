def solution(amount):
  cashes = [100, 50, 10, 1]
  change = []

  for cash in cashes:
    while amount >= cash:
      change.append(cash)
      amount -= cash
  
  return change

print(solution(123))
print(solution(350))