# 실행 결과는 맞으나, 효율성 테스트 부적합
# O(n^2)

# def solution(prices):
#     answer = []
    
#     for i in range(len(prices)):
#         s = 0
#         for p in prices[i+1:]:
#             if prices[i] <= p:
#                 s += 1
#             elif p:
#                 s += 1
#                 break
#             else:
#                 break
#         answer.append(s)
    
#     return answer

# def solution(prices):
#     answer = []
    
#     for i in range(len(prices)):
#         s = 0
#         for p in prices[i+1:]:
#             s += 1
#             if p < prices[i]:
#                 break
#         answer.append(s)
    
#     return answer


# 스택 풀이를 이용하면 O(n)시간에 가능

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stay = []  # 가격이 떨어진 시점을 아직 못 찾은 인덱스

    for i, price in enumerate(prices):
        
        # 바로 전 가격보다 낮아졌다면 (가격이 바로 떨어졌다면) => 1초
        while stay and prices[stay[-1]] > price:
            j = stay.pop()
            answer[j] = i - j
        
        stay.append(i)

    # 끝까지 가격이 떨어지지 않은 것들
    while stay:
        j = stay.pop()
        answer[j] = (n - 1) - j

    return answer