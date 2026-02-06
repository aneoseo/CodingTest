# DFS
# `numbers`의 각 숫자마다 + 또는 - 중 하나를 선택해서 모든 선택 조합을 다 만들어 보고, 그 결과가 `target`이 되는 경우의 수를 셈
# + 또는 - 중 한 조합을 끝까지 만듦

def solution(numbers, target):
    def dfs(cnt, current_sum):
        if cnt == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0

        # 숫자 number[cnt]에 대해
        # +를 선택했을 때 만들 수 있는 경우의 수
        # -를 선택했을 때 만들 수 있는 경우의 수
        # 이 두 경우를 모두 합친 전체 경우의 수
        return dfs(cnt + 1, current_sum + numbers[cnt]) + dfs(cnt + 1, current_sum - numbers[cnt])

    return dfs(0, 0)


# BFS
# numbers의 각 숫자에 대해 현재까지 가능한 모든 합을 한 단계씩 확장해 가며, 마지막 단계에서 target이 되는 경우의 수를 셈
# n번째 숫자까지 가능한 모든 합을 레벨별로 만듦

# def solution(numbers, target):
#     queue = [(0, 0)]  # (현재까지의 합, 인덱스)
#     cnt = 0
#     n = len(numbers)

#     while queue:
#         current_sum, idx = queue.pop(0)

#         # 모든 숫자를 다 사용한 경우
#         if idx == n:
#             if current_sum == target:
#                 cnt += 1
#             continue

#         # 다음 숫자를 + / -로 확장
#         queue.append((current_sum + numbers[idx], idx + 1))
#         queue.append((current_sum - numbers[idx], idx + 1))

#     return cnt