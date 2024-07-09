# def solution(decimal):
#   binary = format(decimal, 'b')
#   return binary

def solution(decimal):
  binary = []

  while decimal != 0:
    leftover = decimal % 2
    decimal //= 2

    binary.append(str(leftover))
    
  binary.reverse()
  return "".join(binary)


print(solution(10))
print(solution(27))
print(solution(12345))
