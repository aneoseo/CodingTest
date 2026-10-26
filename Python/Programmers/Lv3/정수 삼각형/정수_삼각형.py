# 하향식(Top-Down)

# def solution(triangle):
#     # 각 위치까지 도달했을 때의 최대 합을 저장할 DP 배열
#     dp = [[0] * (i + 1) for i in range(len(triangle))]
#     dp[0][0] = triangle[0][0]

#     # 두 번째 행부터 마지막 행까지 순회
#     for i in range(1, len(triangle)):
#         for j in range(i + 1):
        
#             # 맨 왼쪽: 바로(오른쪽) 위에서만 내려올 수 있음
#             if j == 0:
#                 dp[i][j] = dp[i-1][j] + triangle[i][j]
#             # 맨 오른쪽: 왼쪽 위에서만 내려올 수 있음
#             elif j == i:
#                 dp[i][j] = dp[i-1][j-1] + triangle[i][j]
#             # 중간: 왼쪽 위와 오른쪽 위 중 큰 값 선택
#             else:
#                 dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

#     return max(dp[-1])


# 상향식(Bottom-Up)

def solution(triangle):
    # 마지막 행 바로 위부터 꼭대기까지 역순 순회
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            # 아래쪽 두 경로 중 최댓값을 현재 위치에 누적
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]