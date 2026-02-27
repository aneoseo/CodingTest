from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    # 거리 배열 (방문 여부)
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1

    q = deque([(0, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()

        # 도착 지점이면 즉시 반환
        if x == n - 1 and y == m - 1:
            return dist[x][y]

        # 상하좌우 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                # 길이 있고(1) 아직 미방문이면 방문
                if maps[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    # 끝까지 못 갔으면 실패
    return -1