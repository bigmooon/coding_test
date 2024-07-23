def solution(enroll, referral, seller, amount):
  result = [0 for _ in range(len(enroll))]
  enroll_dict = {}

  for idx, name in enumerate(enroll):
    enroll_dict[name] = idx

  # 칫솔판매 금액
  for idx in range(len(amount)):
    amount[idx] *= 100

  # 각 판매자에 대한 판매 금액
  for idx, name in enumerate(seller):
    seller_idx = enroll_dict[name]
    ref_name = referral[seller_idx]
    total = amount[idx]
    share = total // 10  # 추천인 지급 금액

    # 판매자에게 지급할 금액
    result[seller_idx] += total - share

    # 추천인 수수료
    while ref_name != "-" and share > 0:
      ref_idx = enroll_dict[ref_name] # 추천인 인덱스
      result[ref_idx] += share - (share // 10) # 추천인에게 지급할 금액 추가
      share //= 10 
      ref_name = referral[ref_idx] # 다음 추천인

  return result