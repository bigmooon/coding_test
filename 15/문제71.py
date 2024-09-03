def solution(nums):
  if not nums:
    return 0
  
  dp = [1] * len(nums)

  for i in range(len(nums)):
    for j in range(i):
      if nums[i] > nums[j]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)

print(solution([1, 4, 2, 3, 1, 5, 7, 3]))
print(solution([3, 2, 1]))