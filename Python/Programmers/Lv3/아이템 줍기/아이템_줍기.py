from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 최대 50, 2배 확대
    board = [[0] * 102 for _ in range(102)]

    # rectangle = [[좌측하단x, 좌측하단y, 우측상단x, 우측상단y]]
    # 모든 직사각형을 2배 확대하고 영역 전체를 채움
    scaled = []
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        scaled.append((x1, y1, x2, y2))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    # 내부를 지워서 테두리만 남김
    # board[nx][ny] == 1 인 곳만 이동하면 됨
    for x1, y1, x2, y2 in scaled:
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    # 시작점과 도착점도 2배 확대
    sx, sy = characterX * 2, characterY * 2
    tx, ty = itemX * 2, itemY * 2

    # BFS
    queue = deque([(sx, sy, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[sx][sy] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, dist = queue.popleft()

        if x == tx and y == ty:
            # 좌표를 2배 확대했으므로 거리도 2배
            return dist // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < 102
                and 0 <= ny < 102
                and board[nx][ny] == 1
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))