from collections import deque

def solution(game_board, table):
    n = len(game_board)

    # BFS (연결된 영역을 추출)
    def bfs(board, sr, sc, target, visited):
        """
        game_board에서는 0(target)으로 연결된 영역을 찾아 빈칸으로 저장하고,
        table에서는 1(target)로 연결된 영역을 찾아 퍼즐 조각으로 저장
        """
        q = deque([(sr, sc)])
        visited[sr][sc] = True

        shape = []

        while q:
            r, c = q.popleft()
            shape.append((r, c))

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and not visited[nr][nc]
                    and board[nr][nc] == target
                ):
                    visited[nr][nc] = True
                    q.append((nr, nc))

        return normalize(shape)

    # 도형의 위치를 (0, 0) 기준으로 정규화
    def normalize(shape):
        """
        절대 좌표로 비교하면 같은 모양도 위치가 다르면 다르게 보임
        => 각 도형을 (0, 0)을 기준으로 이동시키는 정규화 과정 필요
            - 최소 행/열을 뺌
        """
        min_r = min(r for r, c in shape)
        min_c = min(c for r, c in shape)

        normalized = [(r - min_r, c - min_c) for r, c in shape]

        return sorted(normalized)

    # 도형을 시계 방향으로 90도 회전
    def rotate(shape):
        rotated = [(c, -r) for r, c in shape]
        return normalize(rotated)

    # 특정 값(target)으로 이루어진 모든 영역 추출
    def extract_shapes(board, target):
        visited = [[False] * n for _ in range(n)]
        shapes = []

        for r in range(n):
            for c in range(n):
                if board[r][c] == target and not visited[r][c]:
                    shapes.append(
                        bfs(board, r, c, target, visited)
                    )

        return shapes

    # game_board의 0 영역 = 빈칸
    blanks = extract_shapes(game_board, 0)
    # table의 1 영역 = 퍼즐 조각
    pieces = extract_shapes(table, 1)

    used = [False] * len(pieces)
    answer = 0
    
    # 퍼즐 조각을 최대 4번 회전하면서 빈칸과 일치하는지 확인
    for blank in blanks:
        for i, piece in enumerate(pieces):
            if used[i]:
                continue

            # 칸 수가 다르면 모양도 절대 같을 수 없음
            if len(blank) != len(piece):
                continue

            current = piece

            # 0, 90, 180, 270도 확인
            for _ in range(4):
                if blank == current:
                    used[i] = True
                    answer += len(blank)
                    break

                current = rotate(current)

            if used[i]:
                break

    return answer