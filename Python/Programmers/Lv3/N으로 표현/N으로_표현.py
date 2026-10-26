def solution(N, number):
    # dp[i]: N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]

    # N을 1번부터 8번까지 사용하는 경우 탐색
    for i in range(1, 9):
        # 1. N을 이어 붙이는 경우
        dp[i].add(int(str(N) * i))

        # 2. 이전 DP 결과와 조합하는 경우
        for j in range(1, i):

            # 두 집합의 모든 숫자 조합 탐색
            for a in dp[j]:
                for b in dp[i-j]:

                    # 사칙연산 결과 저장
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)

                    # 0으로 나누는 경우 방지
                    if b != 0:
                        dp[i].add(a // b)

        # 현재 사용 횟수로 목표 숫자를 만들 수 있다면 반환
        if number in dp[i]:
            return i

    # N을 8번 이하로 사용해서 만들 수 없는 경우
    return -1