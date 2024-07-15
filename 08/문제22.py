def solution(record):
  user_id = {}
  cmd = []

  for message in record:
    message_list = message.split(" ")

    if message_list[0] == "Enter" or message_list[0] == "Change":
      user_id[message_list[1]] = message_list[2]

  # 출력
  for message in record:
    message_list = message.split(" ")
    if message_list[0] == "Enter":
      cmd.append(f"{user_id[message_list[1]]}님이 들어왔습니다.")
    elif message_list[0] == "Leave":
      cmd.append(f"{user_id[message_list[1]]}님이 나갔습니다.")
      
  return cmd

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))