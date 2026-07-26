def solution(genres, plays):
    
    genre_play = {}
    songs = []

    # 장르별 총 재생 수
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_play[g] = genre_play.get(g, 0) + p
        songs.append((g, p, i))
    # 장르별 총 재생 수 기준 내림차순
    album_order = sorted(genre_play.keys(), key=lambda g: genre_play[g], reverse=True)
    
    answer = []
    
    # 장르별 노래 추출
    for genre in album_order:
        genre_songs = []
        
        for song in songs:
            if song[0] == genre:
                genre_songs.append(song)
        
        # 재생 수 내림차순, 고유번호 오름차순
        genre_songs.sort(key=lambda x: (-x[1], x[2]))

        # 최대 2곡 선택
        for song in genre_songs[:2]:
            answer.append(song[2])

    return answer