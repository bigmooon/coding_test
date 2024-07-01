# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환하는 solution 함수

def solution(numbers):
  numbers_list = []

  for i in range(len(numbers)):
    # for j in range(1, len(numbers)):
    for j in range(i + 1, len(numbers)):
      # if i != j:
      numbers_list.append(numbers[i] + numbers[j])

  # sorted_numbers = list(set(numbers_list))
  # sorted_numbers.sort()
  numbers_list = sorted(set(numbers_list))

  # return sorted_numbers
  return numbers_list

# Test case
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))