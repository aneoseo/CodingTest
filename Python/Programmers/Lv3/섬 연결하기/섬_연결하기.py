def solution(n, costs):
    parent = list(range(n))

    def find(x):
        # 자기 자신이 부모인지 확인
        if parent[x] != x:
            # 재귀적으로 루트 탐색
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        # 각 섬(노드)의 루트 찾기
        a, b = find(a), find(b)

        # 이미 연결된(통행 가능한) 섬인지 확인
        if a == b:
            return False

        # 서로 다른 집합이라면 합치기
        parent[b] = a
        return True

    # 비용이 가장 적은 다리를 선택하되, 이미 연결된 섬들 사이에 불필요한 다리를 만들지 않음
    costs.sort(key=lambda x: x[2])

    answer = 0
    count = 0

    for a, b, cost in costs:
        if union(a, b):
            answer += cost
            count += 1

            if count == n - 1:
                break

    return answer