def solution(blue, white):
  width, height = 0, 3
  total = blue + white

  for height in range(3, total + 1):
    if total % height == 0:
      width = total // height

      if (width - 2) * (height - 2) == white:
        return [width, height]