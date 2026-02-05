def solution(answers):
    answer = []
    first_score = 0
    second_score = 0
    third_score = 0
    
    # 1번 수포자 답
    first_ans = [1, 2, 3, 4, 5] * 2000
    # 2번 수포자 답
    second_ans = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    # 3번 수포자 답
    third_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    # 맞힌 개수 기록
    for i in range(len(answers)):
        if answers[i] == first_ans[i]:
            first_score += 1
        if answers[i] == second_ans[i]:
            second_score += 1
        if answers[i] == third_ans[i]:
            third_score += 1
    
    # 문제를 가장 많이 맞힌 사람
    if first_score == max(first_score, second_score, third_score):
        answer.append(1)
    if second_score == max(first_score, second_score, third_score):
        answer.append(2)
    if third_score == max(first_score, second_score, third_score):
        answer.append(3)
    
    return answer