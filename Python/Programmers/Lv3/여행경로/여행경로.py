# 오답 코드
# 경로 전체가 아니라 마지막 재귀 호출에서 만든 `route`만 반환
# 매번 재귀 호출할 때마다 `route = []`를 새로 만들고 있기 때문

# def solution(tickets):
#     def dfs(curr):
#         route = []
#         route.append(curr)
        
#         idx = 0
#         next = 'ZZZ'
#         for i in range(len(tickets)):
#             if tickets[i][0] == curr and tickets[i][1] < next:
#                 idx = i
#                 next = tickets[i][1]
        
#         tickets.pop(idx)

#         if tickets:
#             dfs(next)
#         else:
#             route.append(next)
#             return route
    
#     return dfs("ICN")


# 오답 코드
# 매 순간 알파벳순으로 가장 작은 공항을 고르는 greedy 방식 → 중간에 막힐 수 있음

# def solution(tickets):
#     route = []

#     def dfs(curr):
#         route.append(curr)

#         if not tickets:
#             return

#         idx = 0
#         next_airport = 'ZZZ'

#         for i in range(len(tickets)):
#             if tickets[i][0] == curr and tickets[i][1] < next_airport:
#                 idx = i
#                 next_airport = tickets[i][1]

#         tickets.pop(idx)
#         dfs(next_airport)

#     dfs("ICN")
#     return route


# 정답 코드

def solution(tickets):
    tickets.sort()
    used = [False] * len(tickets)
    answer = []

    def dfs(curr, route):
        # 모든 티켓을 사용
        if len(route) == len(tickets) + 1:
            answer.extend(route)
            return True

        for i in range(len(tickets)):
            start, end = tickets[i]

            # 현재 공항에서 출발하고, 아직 사용하지 않은 티켓
            if start == curr and not used[i]:
                used[i] = True
                route.append(end)

                if dfs(end, route):
                    return True
                else:   # 현재의 end로 시작하는 경로가 없어 dfs에서 False가 반환
                    route.pop()
                    used[i] = False
        
        # 티켓을 모두 확인했는데도 사용하지 못한 티켓이 있으면 False를 반환
        return False

    dfs("ICN", ["ICN"])
    return answer