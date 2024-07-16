def solution(genres, plays):
  best_album = []
  most_played = {}

  for music_id, (genre, play) in enumerate(zip(genres, plays)):
    if genre not in most_played:
      most_played[genre] = [0, []]  # 앞은 총 재생 횟수, 뒤는 고유 번호
    
    most_played[genre][0] += play
    most_played[genre][1].append((play, music_id))  

  # 장르 정렬
  most_played_genres = sorted(most_played.values(), key=lambda x: x[0], reverse=True)
  
  for genre_detail in most_played_genres:
    genre_detail[1].sort(key=lambda x: (-x[0], x[1]))
  
  for genre_detail in most_played_genres:
    for i in range(min(2, len(genre_detail[1]))):
      best_album.append(genre_detail[1][i][1])


  return best_album

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))